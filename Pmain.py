from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView
import sys
import pyodbc

server = ''
database = ''  # Name of your Northwind database
use_windows_authentication = False  # Set to True to use Windows Authentication
username = ''  # Specify a username if not using Windows Authentication
password = ''  # Specify a password if not using Windows Authentication


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
        em = self.REmail.text()
        pswd = self.RPassword.text()
        loginid = self.RLoginID.text()
        print(em," ",pswd," ",loginid)
        if not self.check_available_email_login:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            query = "INSERT INTO LoginCredentials ([loginid], [email], [password])VALUES (?, ?, ?)"
            result = cursor.execute(query, loginid, em,pswd)
        else:
             QtWidgets.QMessageBox.critical(self, "Error", "Email/LoginID already exists")


        connection.close()            
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
        result = cursor.execute(query, email, Login).fetchone()

        connection.close()  # Close the connection explicitly
    
        return result is not None


    def check_emailpass(self,email,password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT loginid FROM Login_Credentials WHERE email = ? AND password = ?"
        result = cursor.execute(query, email, password).fetchone()

        connection.close()  # Close the connection explicitly

        if result:
            login_id = result[0]
            return login_id
        else:
            return None
        
class Inventory(QtWidgets.QMainWindow):
    def __init__(self,loginid):
        super(Inventory, self).__init__()

        # Load the .ui file
        uic.loadUi('Inventory.ui', self)

        self.loginid = loginid

    




def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
