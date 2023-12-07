# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Multiplayer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import Kafkabg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(891, 514)
        MainWindow.setStyleSheet(u" /*background-color: qconicalgradient(cx:1, cy:0.5, angle:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); */\n"
"background-image: url(:/newPrefix/Kafka.webp);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(250, 40, 621, 261))
        self.groupBox.setStyleSheet(u"color:white;\n"
"font: 63 9pt \"Bahnschrift SemiBold\";\n"
"background:transparent;\n"
"\n"
"    background-attachment: fixed;\n"
"    background-origin: content;")
        self.tableWidget_2 = QTableWidget(self.groupBox)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 20, 601, 171))
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(69, 28, 53);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"background-color:rgb(62, 43, 63);\n"
"color:white;\n"
"}\n"
"")
        self.TradeConfirm = QPushButton(self.groupBox)
        self.TradeConfirm.setObjectName(u"TradeConfirm")
        self.TradeConfirm.setGeometry(QRect(510, 220, 75, 23))
        self.TradeConfirm.setStyleSheet(u"background-color:rgb(70, 27, 55);\n"
"color: white;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 261, 21))
        self.label.setStyleSheet(u"color:white;\n"
"font: 63 9pt \"Bahnschrift SemiBold\";")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(50, 40, 181, 301))
        self.groupBox_2.setStyleSheet(u"font: 63 9pt \"Bahnschrift SemiBold\";\n"
"color:white;\n"
"background:transparent;\n"
"\n"
"    background-attachment: fixed;\n"
"    background-origin: content;")
        self.factionTable = QTableWidget(self.groupBox_2)
        if (self.factionTable.columnCount() < 1):
            self.factionTable.setColumnCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.factionTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        self.factionTable.setObjectName(u"factionTable")
        self.factionTable.setGeometry(QRect(10, 20, 111, 261))
        self.factionTable.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: rgb(71, 30, 55);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"\n"
"color:white;\n"
"}\n"
"")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(470, 340, 341, 111))
        self.groupBox_3.setStyleSheet(u"font: 25 9pt \"Bahnschrift Light\";\n"
"\n"
"font: 63 10pt \"Bahnschrift SemiBold\";\n"
"background:transparent;\n"
"\n"
"    background-attachment: fixed;\n"
"    background-origin: content;")
        self.MarketButton = QPushButton(self.groupBox_3)
        self.MarketButton.setObjectName(u"MarketButton")
        self.MarketButton.setGeometry(QRect(80, 40, 181, 28))
        self.MarketButton.setStyleSheet(u"background-color:rgb(70, 27, 55);\n"
"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 891, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Trades", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"TradeID", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Trader", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Item Rarity", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Want Item", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Want Rarity", None));
        self.TradeConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Multiplayer", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Faction", None))
        ___qtablewidgetitem6 = self.factionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Members", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Market Place", None))
        self.MarketButton.setText(QCoreApplication.translate("MainWindow", u"GO TO MARKET ->", None))
    # retranslateUi

