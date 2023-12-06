from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc
import re
import bladebg
import Kafkabg
import shbg
# from generated_ui import Ui_MainWindow

server = 'DESKTOP-1GNB7TH\SPARTA'
database = 'GAME'  # Name of your Northwind database
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

        #----------------------helper function---------------------------
        def validate_email(email):
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return True
            return False
        #----------------------------------------------------------------
            
        r_em = self.REmail.text()
        r_pswd = self.RPassword.text()
        r_username = self.RUsername.text()

        def_lvl = 1
        def_gold = 0 
        def_mana = 30
        def_health = 100 


        print(r_em," ",r_pswd," ",r_username)


        if self.check_available_email_login:
            if validate_email(r_em):

                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                query = "INSERT INTO Login_Credentials ([username], [email], [password])VALUES (?, ?, ?)"
                result = cursor.execute(query, r_username, r_em,r_pswd)
                connection.commit()
                connection.close()     

                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                i_query = "INSERT INTO Player ([username], [health], [gold], [mana], [level]) VALUES (?,?,?,?,?)"
                result = cursor.execute(i_query, (r_username, def_health, def_gold, def_mana, def_lvl))
                connection.commit()
                connection.close()


                QtWidgets.QMessageBox.critical(self, "Success", "Registered successfully")
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Please enter a correct Email")
        else:
             QtWidgets.QMessageBox.critical(self, "Error", "Email/LoginID already exists")

        self.REmail.clear()
        self.RPassword.clear()
        self.RUsername.clear()
        

    
    def closed_clicked(self):
        sys.exit()


    def check_emailpass(self,email,password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT username FROM Login_Credentials WHERE email = ? AND password = ?"
        result = cursor.execute(query, email, password).fetchone()

        connection.close()

        if result:
            username = result[0]
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
        uic.loadUi('Inventory.ui', self)  


        self.Username = Username 

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

        if playerClassresult is not None:
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
        self.Multiplayer_win = Multiplayer(self.Username)
        self.Multiplayer_win.show()
        self.hide()


    
class Multiplayer(QtWidgets.QMainWindow):
      def __init__(self,Username):
        super(Multiplayer, self).__init__()

        # Load the .ui file
        uic.loadUi('Multiplayer.ui', self)
        print(Username)

        


    
        
        








































def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


