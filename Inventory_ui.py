# Form implementation generated from reading ui file 'c:\Users\hp\Documents\Third Semester\DBS\Project\DBS_Project_GameManageSys\Inventory.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 537)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 280, 631, 231))
        self.groupBox.setObjectName("groupBox")
        self.inventorytable = QtWidgets.QTableWidget(parent=self.groupBox)
        self.inventorytable.setGeometry(QtCore.QRect(10, 30, 521, 171))
        self.inventorytable.setObjectName("inventorytable")
        self.inventorytable.setColumnCount(5)
        self.inventorytable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventorytable.setItem(3, 4, item)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 110, 47, 13))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 140, 511, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 80, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 10, 241, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Leg = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.Leg.setGeometry(QtCore.QRect(10, 80, 91, 17))
        self.Leg.setObjectName("Leg")
        self.Com = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.Com.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.Com.setObjectName("Com")
        self.Rar = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.Rar.setGeometry(QtCore.QRect(10, 60, 70, 17))
        self.Rar.setObjectName("Rar")
        self.Weap = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.Weap.setGeometry(QtCore.QRect(130, 80, 70, 17))
        self.Weap.setObjectName("Weap")
        self.Arm = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.Arm.setGeometry(QtCore.QRect(130, 40, 91, 17))
        self.Arm.setObjectName("Arm")
        self.Cos = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.Cos.setGeometry(QtCore.QRect(130, 60, 70, 17))
        self.Cos.setObjectName("Cos")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(130, 20, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_7.setObjectName("label_7")
        self.pName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pName.setEnabled(False)
        self.pName.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.pName.setObjectName("pName")
        self.HP = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.HP.setEnabled(False)
        self.HP.setGeometry(QtCore.QRect(120, 50, 81, 20))
        self.HP.setObjectName("HP")
        self.Mana = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Mana.setEnabled(False)
        self.Mana.setGeometry(QtCore.QRect(120, 80, 51, 20))
        self.Mana.setObjectName("Mana")
        self.Class = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Class.setEnabled(False)
        self.Class.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.Class.setObjectName("Class")
        self.Gold = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Gold.setEnabled(False)
        self.Gold.setGeometry(QtCore.QRect(290, 20, 113, 20))
        self.Gold.setObjectName("Gold")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 50, 47, 21))
        self.label_8.setObjectName("label_8")
        self.Level = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Level.setEnabled(False)
        self.Level.setGeometry(QtCore.QRect(290, 50, 41, 20))
        self.Level.setObjectName("Level")
        self.Stamina = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Stamina.setEnabled(False)
        self.Stamina.setGeometry(QtCore.QRect(290, 80, 61, 20))
        self.Stamina.setObjectName("Stamina")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 80, 47, 13))
        self.label_9.setObjectName("label_9")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(370, 50, 211, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.Multiplay = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.Multiplay.setGeometry(QtCore.QRect(70, 30, 75, 23))
        self.Multiplay.setObjectName("Multiplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Player Inventory"))
        item = self.inventorytable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Name "))
        item = self.inventorytable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.inventorytable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rarity "))
        item = self.inventorytable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount "))
        item = self.inventorytable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Value "))
        __sortingEnabled = self.inventorytable.isSortingEnabled()
        self.inventorytable.setSortingEnabled(False)
        item = self.inventorytable.item(0, 0)
        item.setText(_translate("MainWindow", "Iron Sword"))
        item = self.inventorytable.item(0, 1)
        item.setText(_translate("MainWindow", "Weapon"))
        item = self.inventorytable.item(0, 2)
        item.setText(_translate("MainWindow", "Rare"))
        item = self.inventorytable.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.inventorytable.item(0, 4)
        item.setText(_translate("MainWindow", "10500"))
        item = self.inventorytable.item(1, 0)
        item.setText(_translate("MainWindow", "Healing Potion"))
        item = self.inventorytable.item(1, 1)
        item.setText(_translate("MainWindow", "Consumable "))
        item = self.inventorytable.item(1, 2)
        item.setText(_translate("MainWindow", "Common"))
        item = self.inventorytable.item(1, 3)
        item.setText(_translate("MainWindow", "10"))
        item = self.inventorytable.item(1, 4)
        item.setText(_translate("MainWindow", "500"))
        item = self.inventorytable.item(2, 0)
        item.setText(_translate("MainWindow", "Babarian Boots"))
        item = self.inventorytable.item(2, 1)
        item.setText(_translate("MainWindow", "Armour"))
        item = self.inventorytable.item(2, 2)
        item.setText(_translate("MainWindow", "Common"))
        item = self.inventorytable.item(2, 3)
        item.setText(_translate("MainWindow", "4"))
        item = self.inventorytable.item(2, 4)
        item.setText(_translate("MainWindow", "1550"))
        item = self.inventorytable.item(3, 0)
        item.setText(_translate("MainWindow", "Mage Robe"))
        item = self.inventorytable.item(3, 1)
        item.setText(_translate("MainWindow", "Armour"))
        item = self.inventorytable.item(3, 2)
        item.setText(_translate("MainWindow", "Legendary"))
        item = self.inventorytable.item(3, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.inventorytable.item(3, 4)
        item.setText(_translate("MainWindow", "75000"))
        self.inventorytable.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Player Name"))
        self.label_2.setText(_translate("MainWindow", "Gold"))
        self.label_3.setText(_translate("MainWindow", "HP"))
        self.label_4.setText(_translate("MainWindow", "Mana"))
        self.label_5.setText(_translate("MainWindow", "Class"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Item Search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Drop Item "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Filter"))
        self.Leg.setText(_translate("MainWindow", "Legendary"))
        self.Com.setText(_translate("MainWindow", "Common"))
        self.Rar.setText(_translate("MainWindow", "Rare"))
        self.Weap.setText(_translate("MainWindow", "Weapon"))
        self.Arm.setText(_translate("MainWindow", "Consumable"))
        self.Cos.setText(_translate("MainWindow", "Armour"))
        self.label_6.setText(_translate("MainWindow", "Type"))
        self.label_7.setText(_translate("MainWindow", "Rarity"))
        self.pName.setText(_translate("MainWindow", "Boldiblox"))
        self.HP.setText(_translate("MainWindow", "1200/1500"))
        self.Mana.setText(_translate("MainWindow", "5/90"))
        self.Class.setText(_translate("MainWindow", "Sorcerer"))
        self.Gold.setText(_translate("MainWindow", "6000"))
        self.label_8.setText(_translate("MainWindow", "Level"))
        self.Level.setText(_translate("MainWindow", "5"))
        self.label_9.setText(_translate("MainWindow", "Stamina"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Multiplayer"))
        self.Multiplay.setText(_translate("MainWindow", "Connect"))
