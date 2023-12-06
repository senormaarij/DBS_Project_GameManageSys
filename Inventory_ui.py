# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Inventory.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import Kafkabg_rc
import shbg_rc
import Bladebg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 575)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 71, 16))
        self.label.setStyleSheet(u"color:white;\n"
"\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 20, 51, 21))
        self.label_2.setStyleSheet(u"color:white;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 50, 47, 13))
        self.label_3.setStyleSheet(u"color:white;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 80, 47, 13))
        self.label_4.setStyleSheet(u"color: white;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 110, 47, 13))
        self.label_5.setStyleSheet(u"color: white;")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 140, 631, 131))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(u"background-image: url(:/newPrefix/Kafka.webp);\n"
"background-position: top center;\n"
"\n"
"color: white;")
        self.groupBox_2.setFlat(False)
        self.searchbar = QLineEdit(self.groupBox_2)
        self.searchbar.setObjectName(u"searchbar")
        self.searchbar.setGeometry(QRect(20, 40, 211, 20))
        self.searchbar.setStyleSheet(u"background-color: #e0e0e0;")
        self.search_button = QPushButton(self.groupBox_2)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(20, 80, 81, 23))
        self.search_button.setStyleSheet(u"background-color: #e0e0e0;\n"
"color: white;\n"
"")
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 80, 91, 23))
        self.pushButton_2.setStyleSheet(u"color: white;\n"
"")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(250, 10, 241, 111))
        self.groupBox_3.setStyleSheet(u"color: white;")
        self.Leg = QCheckBox(self.groupBox_3)
        self.Leg.setObjectName(u"Leg")
        self.Leg.setGeometry(QRect(10, 80, 91, 17))
        self.Com = QCheckBox(self.groupBox_3)
        self.Com.setObjectName(u"Com")
        self.Com.setGeometry(QRect(10, 40, 81, 17))
        self.Rar = QCheckBox(self.groupBox_3)
        self.Rar.setObjectName(u"Rar")
        self.Rar.setGeometry(QRect(10, 60, 70, 17))
        self.Weap = QCheckBox(self.groupBox_3)
        self.Weap.setObjectName(u"Weap")
        self.Weap.setGeometry(QRect(130, 80, 70, 17))
        self.Cos = QCheckBox(self.groupBox_3)
        self.Cos.setObjectName(u"Cos")
        self.Cos.setGeometry(QRect(130, 40, 91, 17))
        self.Arm = QCheckBox(self.groupBox_3)
        self.Arm.setObjectName(u"Arm")
        self.Arm.setGeometry(QRect(130, 60, 70, 17))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 20, 47, 13))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 47, 13))
        self.pName = QLineEdit(self.centralwidget)
        self.pName.setObjectName(u"pName")
        self.pName.setEnabled(False)
        self.pName.setGeometry(QRect(120, 20, 113, 20))
        self.HP = QLineEdit(self.centralwidget)
        self.HP.setObjectName(u"HP")
        self.HP.setEnabled(False)
        self.HP.setGeometry(QRect(120, 50, 81, 20))
        self.Mana = QLineEdit(self.centralwidget)
        self.Mana.setObjectName(u"Mana")
        self.Mana.setEnabled(False)
        self.Mana.setGeometry(QRect(120, 80, 51, 20))
        self.Class = QLineEdit(self.centralwidget)
        self.Class.setObjectName(u"Class")
        self.Class.setEnabled(False)
        self.Class.setGeometry(QRect(120, 110, 113, 20))
        self.Gold = QLineEdit(self.centralwidget)
        self.Gold.setObjectName(u"Gold")
        self.Gold.setEnabled(False)
        self.Gold.setGeometry(QRect(290, 20, 113, 20))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 50, 47, 21))
        self.label_8.setStyleSheet(u"color: white;")
        self.Level = QLineEdit(self.centralwidget)
        self.Level.setObjectName(u"Level")
        self.Level.setEnabled(False)
        self.Level.setGeometry(QRect(290, 50, 41, 20))
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 771, 531))
        self.frame_5.setStyleSheet(u"background-image: url(:/newPrefix/sh.webp);\n"
"background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-attachment: fixed;\n"
"    background-origin: content;")
        self.groupBox = QGroupBox(self.frame_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 290, 491, 231))
        self.groupBox.setStyleSheet(u"background-image: url(:/newPrefix/Blade.webp);\n"
"background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-attachment: fixed;\n"
"    background-origin: content;\n"
"border: 2px solid;\n"
"color: white;")
        self.inventorytable = QTableWidget(self.groupBox)
        if (self.inventorytable.columnCount() < 3):
            self.inventorytable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.inventorytable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.inventorytable.rowCount() < 5):
            self.inventorytable.setRowCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.inventorytable.setVerticalHeaderItem(4, __qtablewidgetitem7)
        self.inventorytable.setObjectName(u"inventorytable")
        self.inventorytable.setGeometry(QRect(40, 30, 391, 171))
        self.inventorytable.setStyleSheet(u"background: rgb(70, 77, 117);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"color: black;\n"
"border: 1px solid;\n"
"")
        self.groupBox_5 = QGroupBox(self.frame_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(520, 410, 211, 81))
        self.groupBox_5.setStyleSheet(u"background-position:middle right;\n"
"color:white;")
        self.pushButton = QPushButton(self.groupBox_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 30, 93, 28))
        self.groupBox_4 = QGroupBox(self.frame_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(520, 290, 211, 81))
        self.groupBox_4.setStyleSheet(u"\n"
"border: 1px solid;\n"
"color:white;\n"
"")
        self.Multiplay = QPushButton(self.groupBox_4)
        self.Multiplay.setObjectName(u"Multiplay")
        self.Multiplay.setGeometry(QRect(70, 30, 75, 23))
        self.Multiplay.setStyleSheet(u"color:white;\n"
"background: middle right;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_5.raise_()
        self.groupBox_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pName.raise_()
        self.HP.raise_()
        self.Mana.raise_()
        self.Class.raise_()
        self.Gold.raise_()
        self.label_8.raise_()
        self.Level.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 21))
        self.menuInventory_Display = QMenu(self.menubar)
        self.menuInventory_Display.setObjectName(u"menuInventory_Display")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuInventory_Display.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Player Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gold", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HP", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mana", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Item Search", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Drop Item ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.Leg.setText(QCoreApplication.translate("MainWindow", u"Legendary", None))
        self.Com.setText(QCoreApplication.translate("MainWindow", u"Common", None))
        self.Rar.setText(QCoreApplication.translate("MainWindow", u"Rare", None))
        self.Weap.setText(QCoreApplication.translate("MainWindow", u"Weapon", None))
        self.Cos.setText(QCoreApplication.translate("MainWindow", u"Consumable", None))
        self.Arm.setText(QCoreApplication.translate("MainWindow", u"Armour", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Rarity", None))
        self.pName.setText("")
        self.HP.setText("")
        self.Mana.setText("")
        self.Class.setText("")
        self.Gold.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.Level.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Player Inventory", None))
        ___qtablewidgetitem = self.inventorytable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem1 = self.inventorytable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Rarity", None));
        ___qtablewidgetitem2 = self.inventorytable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Add Trade", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"List Item", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Multiplayer", None))
        self.Multiplay.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.menuInventory_Display.setTitle(QCoreApplication.translate("MainWindow", u"Inventory Display", None))
    # retranslateUi

