from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc
import re



server = 'DESKTOP-DF4VK8E\DATABASE_WORK'
database = 'GAME_DEV'  # Name of your Northwind database
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
                query = "INSERT INTO LoginCredentials ([playerID], [email], [password])VALUES (?, ?, ?)"
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

        query = "SELECT loginid FROM LoginCredentials WHERE email = ? or playerid = ?"
        result = cursor.execute(query, email, Login)

        connection.close()  # Close the connection explicitly
    
        return result is None


    def check_emailpass(self,email,password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT playerid FROM LoginCredentials WHERE email = ? AND password = ?"
        result = cursor.execute(query, email, password).fetchone()

        connection.close()  # Close the connection explicitly

        if result:
            login_id = result[0]
            return login_id
        else:
            return None
        
class Inventory(QtWidgets.QMainWindow):
    def __init__(self,playerID):
        super(Inventory, self).__init__()

        # Load the .ui file
        uic.loadUi('Inventory.ui', self)

        #call login function with a unique playerID
        self.load_inventry(playerID)
        
    def load_inventory(self,playerID):
        self.setWindowTitle('Inventory of ',playerID)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        
        playername = "Select playerusername from player where playerid = ?"
        playernameresult = cursor.execute(playername, playerID)
        self.lineEdit_2.setText(playernameresult)
        
        playerHP = "Select playerhp from player where playerid = ?"
        playerHPresult = cursor.execute(playerHP,playerID)
        self.lineEdit_3.setText(playerHPresult)
        
        playerMana = "Select playermana from player where playerid = ?"
        playerManaresult = cursor.execute(playerMana , playerID)
        self.lineEdit_4.setText(playerManaresult)
        
        playerClass = "Select classtype from classes  where classid in (select classid from player where playerid = ?)"
        playerClassresult = cursor.execute(playerClass , playerID)
        self.lineEdit_5.setText(playerClassresult)
        
        playerGold = "Select gold from player where playerid = ?"
        playerGoldresult = cursor.execute(playerGold,playerID)
        self.lineEdit_6.setText(playerGoldresult)
        
        playerLevel = "select explevel from player where playerid = ?"
        playerLevelresult = cursor.execute(playerLevel,playerID)
        self.lineEdit_7.setText(playerLevelresult)
        
    
        
        
        
        
    
    def update_inventory():
        pass
    
    
        
        

def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


