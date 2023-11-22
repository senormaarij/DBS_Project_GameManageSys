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

        

    def check_available_email_login(self,email,Login):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT loginid FROM Login_Credentials WHERE email = ? or loginid = ?"
        result = cursor.execute(query, email, Login)

        connection.close()  # Close the connection explicitly
    
        return result is None


    def check_emailpass(self,email,password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT loginid FROM Login_Credentials WHERE email = ? AND password = ?"
        result = cursor.execute(query, email, password).fetchone()

        connection.close()  # Close the connection explicitly

        if result:
            login_id = result[0]
            print(login_id)
            return login_id
        else:
            return None
        
class Inventory(QtWidgets.QMainWindow):
    def __init__(self,playerID):
        super(Inventory, self).__init__()

        # Load the .ui file
        uic.loadUi('Inventory.ui', self)
        print(playerID)
        #call login function with a unique playerID
        self.load_inventory(playerID)
        
    def load_inventory(self,playerID):
        #self.setWindowTitle('Inventory of ',playerID)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        playername = "Select PlayerUserName from player where loginid = ?"
        playernameresult = cursor.execute(playername, playerID).fetchone()
        self.lineEdit_2.setText(playernameresult[0])
        
        playerHP = "Select Expfor_next_level from player where loginid = ?"
        playerHPresult = cursor.execute(playerHP,playerID).fetchone()
        self.lineEdit_3.setText(str(playerHPresult[0]))
        
        playerMana = "Select TotalManaCap from player where loginid = ?"
        playerManaresult = cursor.execute(playerMana , playerID).fetchone()
        self.lineEdit_4.setText(str(playerManaresult[0]))
        
        playerClass = "Select classtype from classes  where classid in (select classid from player where loginid = ?)"
        playerClassresult = cursor.execute(playerClass , playerID).fetchone()
        self.lineEdit_5.setText(playerClassresult[0])
        
        playerGold = "Select gold from player where loginid = ?"
        playerGoldresult = cursor.execute(playerGold,playerID).fetchone()
        self.lineEdit_6.setText(str(playerGoldresult[0]))
        
        playerLevel = "select explevel from player where loginid = ?"
        playerLevelresult = cursor.execute(playerLevel,playerID).fetchone()
        self.lineEdit_7.setText(str(playerLevelresult[0]))
        
        
    def search(self):
        search_text = self.lineEdit.search.text()
        rarity=""
        #rarity defined below is done by the ui we made if the database has different rarity change accordingly.
        if self.checkBox_2.isChecked():
            rarity = "Common"
        elif self.checkBox_3.isChecked():
            rarity = "Rare"
        elif self.checkBox_4.isChecked():
            rarity = "Legendary"
        
        type = ""
        if self.checkBox_5.isChecked():
            type = "Consumable"
        elif self.checkBox_6.isChecked():
            type = "Armour"
        elif self.checkBox_7.isChecked():
            type = "Weapon"
        
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        #complete this query as per the SQL i do not know how we are implemrnting the SQL so i can not do this.
        query = "Select "
        
    def update_inventory():
        pass
    
    
        
        

def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


