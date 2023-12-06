from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc
import re
# from generated_ui import Ui_MainWindow

server = 'DESKTOP-1GNB7TH\SPARTA'
database = 'GAME_N'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication
username = 'sa'  # Specify a username if not using Windows Authentication
password = 'maarij0314'  # Specify a password if not using Windows Authentication


# Create the connection string based on the authentication method chosen
if use_windows_authentication:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
else:
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


# Main Window Class
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Login, self).__init__()

        

        # Load the .ui file
        uic.loadUi('Login.ui', self)
        
        # Connect Submit Button to Event Handling Code
        self.setWindowTitle('Login')
        self.login.clicked.connect(self.open_player_int)
        self.Register.clicked.connect(self.register_player)
        self.close.clicked.connect(self.closed_clicked)

    def register_player(self):
        def validate_email(email):
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return True
            return False
            
        em = self.REmail.text()
        pswd = self.RPassword.text()
        loginid = self.RLoginID.text()
        print(em," ",pswd," ",loginid)
        if self.check_available_email_login:

            if validate_email(em):
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                query = "INSERT INTO Login_Credentials ([loginid], [email], [password])VALUES (?, ?, ?)"
                result = cursor.execute(query, loginid, em,pswd)
                connection.commit()
                QtWidgets.QMessageBox.critical(self, "Success", "Registered successfully")
                connection.close()        
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Please enter a correct Email")
        else:
             QtWidgets.QMessageBox.critical(self, "Error", "Email/LoginID already exists")
        pass

    
    def closed_clicked(self):
        sys.exit()


    def check_emailpass(self,email,password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT username FROM Login_Credentials WHERE email = ? AND password = ?"
        result = cursor.execute(query, email, password).fetchone()

        connection.close()  # Close the connection explicitly

        if result:
            username = result[0]
            # print(login_id)
            return username
        else:
            return None    

    def check_available_email_login(self,email,Login):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT username FROM Login_Credentials WHERE email = ? or loginid = ?"
        result = cursor.execute(query, email, Login)

        connection.close()  # Close the connection explicitly
    
        return result is None

    def open_player_int(self):
            em = self.Email.text()
            pswd = self.Password.text()
            username = self.check_emailpass(em,pswd) 
            if username is not None and "@" in em:
                self.Inventory_win = Inventory(username)
                self.Inventory_win.show()
                self.hide()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Email/Password might be incorrect")

    
#-------------------------------------------------------------------------------------------- 
class Inventory(QtWidgets.QMainWindow):
    def __init__(self,Username):
        super(Inventory, self).__init__()
        # Load the .ui file
        # uic.loadUi('Inventory.ui', self)  
        from  Inventory_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        

        self.inventory_lst = []

        #call login function with a unique playerID
        self.load_inventory(Username)

        self.search_button.clicked.connect(self.search)

        self.Multiplay.clicked.connect(self.load_Multiplayer)

        
    def load_inventory(self, Username):
       
        self.setWindowTitle('Inventory of '+ Username)


        #getting Player Details

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        query = "Select UserName, health, Mana , gold, level from player where username  = ?"
        result = cursor.execute(query, Username).fetchone()
        self.pName.setText(result[0])
        self.HP.setText(str(result[1]))
        self.Mana.setText(str(result[2]))
        self.Gold.setText(str(result[3]))
        self.Level.setText(str(result[4]))

        
        playerClass = "Select classtype from classes  where classid in (select classid from player where username = ?)"
        playerClassresult = cursor.execute(playerClass , Username).fetchone()
        self.Class.setText(playerClassresult[0])

        #getting player inventory
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
   
        query = "SELECT Items.ItemName,Items.Rarity, Items.Type FROM Inventory JOIN Player ON Inventory.Playerid = Player.Playerid JOIN Items ON Inventory.ItemID = Items.ItemID WHERE Player.Username = ?"
        cursor.execute(query , Username)
    
        rows = cursor.fetchall()

        self.inventorytable.setRowCount(len(rows))
        self.inventorytable.setColumnCount(3)

        for i,row in enumerate(rows):
            for j,col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.inventorytable.setItem(i,j,item)

          
        for row in rows:
            inventory_item = {
                'ItemName': row[0],
                'Rarity': row[1],
                'Type': row[2]
            }
            self.inventory_lst.append(inventory_item)
        
        print(self.inventory_lst)

        
        
        
    
    def search(self):
        username = self.pName.text()
        itemname = self.searchbar.text().lower()

        rarity = None
        if self.Com.isChecked():
            rarity = "Common"
        elif self.Rar.isChecked():
            rarity = "Rare"
        elif self.Leg.isChecked():
            rarity = "Legendary"

        item_type = None
        if self.Cos.isChecked():
            item_type = "Consumable"
        elif self.Arm.isChecked():
            item_type = "Armour"
        elif self.Weap.isChecked():
            item_type = "Weapon"

        filtered_inventory = self.filter_inventory(itemname, rarity, item_type)
        self.update_table(filtered_inventory)

    def filter_inventory(self, itemname, rarity, item_type):
        filtered_inventory = []

        for item in self.inventory_lst:
            if (not itemname or itemname in item['ItemName'].lower()) and \
               (rarity is None or item['Rarity'] == rarity) and \
               (item_type is None or item['Type'] == item_type):
                filtered_inventory.append(item)

        return filtered_inventory

    def update_table(self, inventory):
        self.inventorytable.setRowCount(len(inventory))
        self.inventorytable.setColumnCount(3)

        for i, item in enumerate(inventory):
            item_name = QTableWidgetItem(item['ItemName'])
            rarity = QTableWidgetItem(item['Rarity'])
            item_type = QTableWidgetItem(item['Type'])

            self.inventorytable.setItem(i, 0, item_name)
            self.inventorytable.setItem(i, 1, rarity)
            self.inventorytable.setItem(i, 2, item_type)

        





        
                    
    

        
    def update_inventory():
        pass

    def load_Multiplayer(self):
        self.Multiplayer_win = Multiplayer(self.login_id)
        self.Multiplayer_win.show()


    
class Multiplayer(QtWidgets.QMainWindow):
      def __init__(self,playerID):
        super(Multiplayer, self).__init__()

        # Load the .ui file
        uic.loadUi('Multiplayer.ui', self)
        print(playerID)


    
        
        

def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


