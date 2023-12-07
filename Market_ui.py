# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Market.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)
import Bladebg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(482, 597)
        MainWindow.setStyleSheet(u"background-image: url(:/newPrefix/Blade.webp);\n"
"background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-attachment: fixed;\n"
"    background-origin: content;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 441, 541))
        self.groupBox.setStyleSheet(u"background: transparent;\n"
"color:white;")
        self.M_table = QTableWidget(self.groupBox)
        if (self.M_table.columnCount() < 4):
            self.M_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.M_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.M_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.M_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.M_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.M_table.setObjectName(u"M_table")
        self.M_table.setGeometry(QRect(20, 30, 401, 461))
        self.M_table.setStyleSheet(u"QHeaderView::section {\n"
"    background-color:rgb(112, 58, 53);\n"
"}\n"
"")
        self.buy = QPushButton(self.groupBox)
        self.buy.setObjectName(u"buy")
        self.buy.setGeometry(QRect(20, 500, 75, 23))
        self.buy.setStyleSheet(u"font: 63 9pt \"Bahnschrift SemiBold\";\n"
"\n"
"color: white;\n"
"background-color:rgb(112, 58, 53);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 482, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Market Listing", None))
        ___qtablewidgetitem = self.M_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem1 = self.M_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.M_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Rarity", None));
        ___qtablewidgetitem3 = self.M_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gold", None));
        self.buy.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
    # retranslateUi

