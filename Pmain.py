from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc
import re

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

        query = "SELECT loginid FROM Login_Credentials WHERE email = ? AND password = ?"
        result = cursor.execute(query, email, password).fetchone()

        connection.close()  # Close the connection explicitly

        if result:
            login_id = result[0]
            # print(login_id)
            return login_id
        else:
            return None    

    def check_available_email_login(self,email,Login):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT loginid FROM Login_Credentials WHERE email = ? or loginid = ?"
        result = cursor.execute(query, email, Login)

        connection.close()  # Close the connection explicitly
    
        return result is None

    def open_player_int(self):
            em = self.Email.text()
            pswd = self.Password.text()
            login_id = self.check_emailpass(em,pswd) 
            if login_id is not None and "@" in em:
                self.Inventory_win = Inventory(login_id)
                self.Inventory_win.show()
                self.hide()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Email/Password might be incorrect")

    
        
class Inventory(QtWidgets.QMainWindow):
    def __init__(self,playerID):
        super(Inventory, self).__init__()
        self.login_id = playerID
        # Load the .ui file
        uic.loadUi('Inventory.ui', self)
        # print(playerID)


        #call login function with a unique playerID
        self.load_inventory(playerID)

        self.Multiplay.clicked.connect(self.load_Multiplayer)

        
    def load_inventory(self,playerID):
       
        self.setWindowTitle('Inventory of '+playerID)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        query = "Select PlayerUserName, health, Mana, stamina , gold, explevel from player where loginid = ?"
        result = cursor.execute(query, playerID).fetchone()
        self.pName.setText(result[0])
        self.HP.setText(str(result[1]))
        self.Mana.setText(str(result[2]))
        self.Stamina.setText(str(result[3]))
        self.Gold.setText(str(result[4]))
        self.Level.setText(str(result[5]))

        
        playerClass = "Select classtype from classes  where classid in (select classid from player where loginid = ?)"
        playerClassresult = cursor.execute(playerClass , playerID).fetchone()
        self.Class.setText(playerClassresult[0])

        
        
        
    def search(self):
        queryforinventoryid = "Select inventoryid from player where playerid = ?"
        
        inventoryid = cursor.execute(queryforinventoryid , self.login_id)
        search_text = self.lineEdit.search.text()
        if not (self.Com.isChecked() or self.Rar.isChecked() or self.Leg.isChecked()):
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select Rarity')
            return

        if not (self.Cos.isChecked() or self.Arm.isChecked() or self.Weap.isChecked()):
            QtWidgets.QMessageBox.warning(self, 'Warning', 'Please select Type')
            return
        
        rarity=""
        #rarity defined below is done by the ui we made if the database has different rarity change accordingly.
        
        if self.Com.isChecked():
            rarity = "Common"
        elif self.Rar.isChecked():
            rarity = "Rare"
        elif self.Leg.isChecked():
            rarity = "Legendary"
        
        type = ""
        if self.Cos.isChecked():
            type = "Consumable"
        elif self.Arm.isChecked():
            type = "Armour"
        elif self.Weap.isChecked():
            type = "Weapon"
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        #complete this query as per the SQL i do not know how we are implemrnting the SQL so i can not do this.
        query = "Select ItemName , Rarity , Type from Items where ItemName = ? and Rarity = ? and Type = ? and itemid in(select itemid from Inventory where InventoryID = ? )"
        cursor.execute(query , search_text , rarity , type , inventoryid)
    
        rows = cursor.fetchall()
        
        self.inventorytable.setRowCount(len(rows))
        self.inventorytable.setColumnCount(3)
        
        for i,row in enumerate(rows):
            for j,col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.inventorytable.setItem(i,j,item)
                    
    

        
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


