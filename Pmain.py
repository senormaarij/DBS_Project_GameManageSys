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

        # Load Orders data
        # self.populate_table()

        # Connect Submit Button to Event Handling Code
        self.login.clicked.connect(self.open_player_int)

    

    def open_player_int(self):
        self.Inventory_win = Inventory()
        self.Inventory_win.show()


class Inventory(QtWidgets.QMainWindow):
    def __init__(self):
        super(Inventory, self).__init__()

        # Load the .ui file
        uic.loadUi('Inventory.ui', self)

    




def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
