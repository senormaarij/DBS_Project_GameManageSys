# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import Bladebg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(392, 486)
        MainWindow.setStyleSheet(u"background-image: url(:/newPrefix/Blade.webp);\n"
"\n"
"background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-attachment: fixed;\n"
"    background-origin: content;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 371, 161))
        self.groupBox.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"font: 63 9pt \"Bahnschrift SemiBold\";")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 47, 21))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 61, 21))
        self.Email = QLineEdit(self.groupBox)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(70, 30, 291, 20))
        self.Email.setStyleSheet(u"color:white;")
        self.Password = QLineEdit(self.groupBox)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(70, 60, 291, 20))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.Password.setFont(font)
        self.Password.setStyleSheet(u"color:white;")
        self.Password.setEchoMode(QLineEdit.Password)
        self.login = QPushButton(self.groupBox)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(280, 110, 75, 23))
        self.login.setStyleSheet(u"background-color: rgb(156, 61, 54);\n"
"color:white;\n"
"font: 63 9pt \"Bahnschrift SemiBold\";")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 190, 371, 211))
        self.groupBox_2.setStyleSheet(u"background: transparent;\n"
"color:white;\n"
"font: 63 9pt \"Bahnschrift SemiBold\";")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 47, 21))
        self.REmail = QLineEdit(self.groupBox_2)
        self.REmail.setObjectName(u"REmail")
        self.REmail.setGeometry(QRect(70, 30, 291, 20))
        self.REmail.setStyleSheet(u"color:white;")
        self.Register = QPushButton(self.groupBox_2)
        self.Register.setObjectName(u"Register")
        self.Register.setGeometry(QRect(280, 150, 75, 23))
        self.Register.setStyleSheet(u"background-color: rgb(156, 61, 54);\n"
"color:white;\n"
"font: 63 9pt \"Bahnschrift SemiBold\";")
        self.RUsername = QLineEdit(self.groupBox_2)
        self.RUsername.setObjectName(u"RUsername")
        self.RUsername.setGeometry(QRect(70, 70, 291, 20))
        self.RUsername.setStyleSheet(u"color:white;")
        self.RPassword = QLineEdit(self.groupBox_2)
        self.RPassword.setObjectName(u"RPassword")
        self.RPassword.setGeometry(QRect(70, 110, 291, 20))
        self.RPassword.setStyleSheet(u"color:white;")
        self.RPassword.setEchoMode(QLineEdit.Password)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 60, 91, 41))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 110, 71, 21))
        self.close = QPushButton(self.centralwidget)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(290, 410, 81, 23))
        self.close.setStyleSheet(u"background:transparent;\n"
"background-color: rgb(156, 61, 54);\n"
"color:white;\n"
"font: 63 9pt \"Bahnschrift SemiBold\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 392, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Username ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

