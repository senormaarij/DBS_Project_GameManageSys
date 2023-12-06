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
#DESKTOP-DF4VK8E\DATABASE_WORK
server = 'DESKTOP-DF4VK8E\DATABASE_WORK'
database = 'Game'  # Name of your Northwind database
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


    #----------------------helper function--------------------------- 

    def check_available_email_login(self,email,username):
        print(email,username)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT * FROM Login_Credentials WHERE email = ? or  username = ?"
        result = cursor.execute(query, email, username).fetchone()

        connection.close()  
        print("checked")
        if result is None:
            return True
        else:
            return False


    def validate_email(self,email):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return True
        return False

    
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

    #----------------------------------------------------------------


    def register_player(self):
        r_em = self.REmail.text()
        r_pswd = self.RPassword.text()
        r_username = self.RUsername.text()

        #---default values for new player-----
        def_lvl = 1
        def_gold = 0 
        def_mana = 30
        def_health = 100 

        #print(r_em," ",r_pswd," ",r_username)

        if self.check_available_email_login(r_em,r_username):
            if self.validate_email(r_em):

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


                QtWidgets.QMessageBox.information(self, "Success", "Registered successfully")
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Please enter a correct Email")
        else:
             QtWidgets.QMessageBox.critical(self, "Error", "Email/Username already exists")

        self.REmail.clear()
        self.RPassword.clear()
        self.RUsername.clear()
        

    
    def closed_clicked(self):
        sys.exit()


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
        self.inventorytable.cellClicked.connect(self.on_table_cell_clicked)
        self.pushButton.clicked.connect(self.load_AddTrade)
        self.selected_row = None
        
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
        
        # print(self.inventory_lst)

        
        
        
    
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

    def on_table_cell_clicked(self, row, col):
        self.selected_row = row

    def load_AddTrade(self):
        if self.selected_row is not None:
            self.ItemName = self.inventorytable.item(self.selected_row, 0).text()
            self.ItemRarity = self.inventorytable.item(self.selected_row, 1).text()
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            query = "select itemId from items where itemname = ? and rarity = ?"
            result = cursor.execute(query, self.ItemName, self.ItemRarity).fetchone()
            Itemid = result[0]
            
            self.AddTrade_win = AddTrade(self.Username, Itemid)
            self.AddTrade_win.show()
            self.hide()
        else:
            QtWidgets.QMessageBox.critical(self, "Error!" ,"No row selected. Please click on a row in the table before confirming the trade!")


    
class Multiplayer(QtWidgets.QMainWindow):
    def __init__(self,Username):
        super(Multiplayer, self).__init__()

        # Load the .ui file
        uic.loadUi('Multiplayer.ui', self)
        # print(Username)
        self.Username = Username

        # Trade display.
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT TradeID, (SELECT Username FROM Player WHERE PlayerID = Trade.BelongsTo) AS BelongsToUsername, (SELECT ItemName FROM Items WHERE ItemID = Trade.ItemToTradeID) AS ItemToTrade, (SELECT Rarity FROM Items WHERE ItemID = Trade.ItemToTradeID) AS TradeItemRarity, (SELECT ItemName FROM Items WHERE ItemID = Trade.ItemNeedID) AS ItemNeeded, (SELECT Rarity FROM Items WHERE ItemID = Trade.ItemNeedID) AS NeededItemRarity FROM Trade"

        cursor.execute(query)
        rows = cursor.fetchall()

        #Faction display.

        faction_query = "select username from player where playerid in (select playerid from player where factionid in (select factionid from player where username = ?))"
        cursor.execute(faction_query, self.Username)
        faction_rows = cursor.fetchall()

        self.tableWidget_2.setRowCount(len(rows))
        self.tableWidget_2.setColumnCount(6)

        self.factionTable.setRowCount(len(faction_rows))
        self.factionTable.setColumnCount(1)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget_2.setItem(i, j, item)

        for i, row in enumerate(faction_rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.factionTable.setItem(i, j, item)
        

        self.tableWidget_2.cellClicked.connect(self.on_table_cell_clicked)
        self.TradeConfirm.clicked.connect(self.confirm_trade)
        self.selected_row = None

    def on_table_cell_clicked(self, row, col):
        self.selected_row = row

    def confirm_trade(self):
        self.select_lst = []
        if self.selected_row is not None:
            # Collect data
            for i in range(6):
                self.select_lst.append(self.tableWidget_2.item(self.selected_row, i).text())

            # Check if the user has the item needed for the trade
            if self.check_inventory_for_trade(self.Username, self.select_lst[4]):
                if self.Username == self.select_lst[1]:
                    QtWidgets.QMessageBox.critical(self, "Error!" ,"Why brother Why!")
                else:
                    connection = pyodbc.connect(connection_string)
                    cursor = connection.cursor()

                    # ned to update item into the user's inventory.
                    insert_query = "INSERT INTO Inventory (Playerid, ItemID) VALUES ((SELECT Top 1 PlayerID FROM Player WHERE Username = ?), (SELECT ItemID FROM Items WHERE ItemName = ? and Rarity = ?))"
                    cursor.execute(insert_query, (self.Username, self.select_lst[2], self.select_lst[3]))

                    #need to update item into the Traders inventory.
                    insert_query = "INSERT INTO Inventory (Playerid, ItemID) VALUES ((SELECT Top 1 PlayerID FROM Player WHERE Username = ?), (SELECT ItemID FROM Items WHERE ItemName = ? and Rarity = ?))"
                    cursor.execute(insert_query, (self.select_lst[1], self.select_lst[4], self.select_lst[5]))

                    # now I need to delete the item needed from user's inventory.
                    delete_query = " DELETE FROM Inventory  WHERE Playerid = (SELECT PlayerID FROM Player WHERE Username = ?) AND ItemID = (SELECT ItemID FROM Items WHERE ItemName = ? and Rarity = ?)"
                    cursor.execute(delete_query, (self.Username, self.select_lst[4], self.select_lst[5]))

                    #now I need to delete from Trades inventory.
                    delete_query = " DELETE FROM Inventory  WHERE Playerid = (SELECT PlayerID FROM Player WHERE Username = ?) AND ItemID = (SELECT ItemID FROM Items WHERE ItemName = ? and Rarity = ?)"
                    cursor.execute(delete_query, (self.select_lst[1], self.select_lst[2], self.select_lst[3]))

                    # Commit the transaction
                    connection.commit()
                    QtWidgets.QMessageBox.information(self, "Success" ,"Trade was successful!")
            else:
                QtWidgets.QMessageBox.critical(self, "Error!" ,"You don't have the item in your inventory!")
        else:
            QtWidgets.QMessageBox.critical(self, "Error!" ,"No row selected. Please click on a row in the table before confirming the trade!")

    def check_inventory_for_trade(self, username, item_needed):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        inventory_query = "SELECT COUNT(*) FROM Inventory WHERE Playerid = (SELECT PlayerID FROM Player WHERE Username = ?) AND ItemID IN (SELECT ItemID FROM Items WHERE ItemName = ?)"

        cursor.execute(inventory_query, (username, item_needed))
        count = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return count > 0
    
class AddTrade(QtWidgets.QMainWindow):
    def __init__(self, Username, itemid):
        super(AddTrade, self).__init__()

        # Load the .ui file
        uic.loadUi('Trade Confirm.ui', self)

        self.Username = Username
        self.itemid = itemid

        # Items display.
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        query = "SELECT ItemName, Rarity, Type FROM Items"

        cursor.execute(query)
        items = cursor.fetchall()

        self.tableWidget.setRowCount(len(items))
        self.tableWidget.setColumnCount(3)

        for i, item in enumerate(items):
            for j, value in enumerate(item):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.cellClicked.connect(self.on_table_cell_clicked)
        self.pushButton.clicked.connect(self.add_trade)
        self.selected_row = None

    def on_table_cell_clicked(self, row, col):
        self.selected_row = row
    
    def add_trade(self):
        self.select_lst = []
        if self.selected_row is not None:
            # Collect data
            for i in range(3):
                self.select_lst.append(self.tableWidget.item(self.selected_row, i).text())
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            query = "select itemId from items where itemname = ? and rarity = ?"
            result = cursor.execute(query, self.select_lst[0], self.select_lst[1]).fetchone()
            needId = result[0]

            #insert data into Trade.
            insert_query = "Insert INTO Trade(BelongsTo, ItemToTradeID, ItemNeedID) values ((select playerid from player where username = ?), ?, ?)"
            cursor.execute(insert_query, self.Username, self.itemid, needId)
            connection.commit()
            QtWidgets.QMessageBox.information(self, "Success" ,"Trade added successfully!")
            
        else:
            QtWidgets.QMessageBox.critical(self, "Error!" ,"No row selected. Please click on a row in the table before confirming the trade!")

def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


