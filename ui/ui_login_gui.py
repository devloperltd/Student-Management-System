# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_guiVjVIHY.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
from PySide6 import QtCore
from resources.ico_rc import *
import sys

class Ui_login_gui(object):
    def setupUi(self, login_gui):
        if not login_gui.objectName():
            login_gui.setObjectName(u"login_gui")
        login_gui.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        login_gui.setAttribute(QtCore.Qt.WA_TranslucentBackground)    
        login_gui.resize(964, 618)
        login_gui.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#login_container{\n"
"	border-image: url(:/png/icons/background.jpg) 0 0 0 0 stretch stretch;\n"
"	border-radius:10px;\n"
"}\n"
"#centralwidget{}\n"
"\n"
"#widget{\n"
"	background-color: rgb(23, 21, 59);\n"
"	border-radius:20px;\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid #006080;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(52, 43, 124);\n"
"	padding:10px 5px;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(65, 57, 156);\n"
"}\n"
"#to_register, #to_login, #back_to_login, #to_forget_pass, #close_btn{\n"
"	background-color: transparent;\n"
"	color: rgb(81, 129, 195);\n"
"	padding:0 5px;\n"
"}\n"
"#to_register::pressed{\n"
"	color: rgb(100, 101, 175);\n"
"}")
        self.centralwidget = QWidget(login_gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.login_container = QFrame(self.centralwidget)
        self.login_container.setObjectName(u"login_container")
        self.login_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_container.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.login_container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(298, 60, 350, 480))
        self.widget.setMinimumSize(QSize(350, 480))
        self.widget.setMaximumSize(QSize(350, 480))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.to_register = QPushButton(self.login_page)
        self.to_register.setObjectName(u"to_register")
        self.to_register.setGeometry(QRect(70, 390, 181, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        self.to_register.setFont(font)
        self.to_register.setStyleSheet(u"")
        self.frame_2 = QFrame(self.login_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 160, 271, 131))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.user_lineEdit = QLineEdit(self.frame_2)
        self.user_lineEdit.setObjectName(u"user_lineEdit")
        self.user_lineEdit.setGeometry(QRect(10, 20, 251, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.user_lineEdit.setFont(font1)
        self.user_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); \n"
"")
        self.pass_lineEdit = QLineEdit(self.frame_2)
        self.pass_lineEdit.setObjectName(u"pass_lineEdit")
        self.pass_lineEdit.setGeometry(QRect(10, 70, 251, 41))
        self.pass_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); \n"
"")
        self.pass_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.hide_pass_btn = QPushButton(self.frame_2)
        self.hide_pass_btn.setObjectName(u"hide_pass_btn")
        self.hide_pass_btn.setGeometry(QRect(220, 80, 31, 21))
        self.hide_pass_btn.setStyleSheet(u"background-color: transparent;;")
        icon = QIcon()
        icon.addFile(u":/png/icons/hide.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hide_pass_btn.setIcon(icon)
        self.hide_pass_btn.setIconSize(QSize(24, 24))
        self.hide_pass_btn.setCheckable(True)
        self.hide_pass_btn.setChecked(False)
        self.hide_pass_btn.setAutoRepeat(False)
        self.hide_pass_btn.setAutoExclusive(False)
        self.hide_pass_btn.setFlat(False)
        self.show_pass_btn = QPushButton(self.frame_2)
        self.show_pass_btn.setObjectName(u"show_pass_btn")
        self.show_pass_btn.setGeometry(QRect(220, 80, 31, 21))
        self.show_pass_btn.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/png/icons/view.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_pass_btn.setIcon(icon1)
        self.show_pass_btn.setIconSize(QSize(24, 24))
        self.show_pass_btn.setCheckable(True)
        self.show_pass_btn.setChecked(False)
        self.show_pass_btn.setAutoRepeat(False)
        self.show_pass_btn.setAutoExclusive(False)
        self.show_pass_btn.setFlat(False)
        self.pass_lineEdit.raise_()
        self.user_lineEdit.raise_()
        self.show_pass_btn.raise_()
        self.hide_pass_btn.raise_()
        self.remember_me = QCheckBox(self.login_page)
        self.remember_me.setObjectName(u"remember_me")
        self.remember_me.setGeometry(QRect(40, 290, 111, 20))
        self.remember_me.setStyleSheet(u"color: rgb(117, 112, 153);")
        self.to_forget_pass = QPushButton(self.login_page)
        self.to_forget_pass.setObjectName(u"to_forget_pass")
        self.to_forget_pass.setGeometry(QRect(160, 284, 141, 31))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setUnderline(True)
        self.to_forget_pass.setFont(font2)
        self.to_forget_pass.setStyleSheet(u"color: rgb(125, 127, 255);")
        self.label_3 = QLabel(self.login_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 140, 191, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(117, 112, 153);")
        self.login_btn = QPushButton(self.login_page)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(40, 340, 251, 41))
        self.login_btn.setFont(font3)
        self.login_btn.setStyleSheet(u"color: rgb(146, 143, 170);")
        self.label_4 = QLabel(self.login_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 30, 101, 101))
        self.label_4.setPixmap(QPixmap(u":/png/icons/profile.png"))
        self.label_4.setScaledContents(True)
        self.close_btn = QPushButton(self.login_page)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(307, 5, 16, 16))
        icon2 = QIcon()
        icon2.addFile(u":/png/icons/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon2)
        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.to_login = QPushButton(self.register_page)
        self.to_login.setObjectName(u"to_login")
        self.to_login.setGeometry(QRect(70, 410, 181, 31))
        self.to_login.setFont(font2)
        self.label_2 = QLabel(self.register_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 90, 191, 20))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(117, 112, 153);")
        self.checkBox = QCheckBox(self.register_page)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(40, 324, 141, 20))
        self.checkBox.setStyleSheet(u"color: rgb(117, 112, 153);")
        self.frame = QFrame(self.register_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 110, 271, 211))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.add_user_lineEdit = QLineEdit(self.frame)
        self.add_user_lineEdit.setObjectName(u"add_user_lineEdit")
        self.add_user_lineEdit.setGeometry(QRect(10, 10, 251, 41))
        self.add_user_lineEdit.setFont(font1)
        self.add_user_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.add_pass_lineEdit = QLineEdit(self.frame)
        self.add_pass_lineEdit.setObjectName(u"add_pass_lineEdit")
        self.add_pass_lineEdit.setGeometry(QRect(10, 60, 251, 41))
        self.add_pass_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.add_pass_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_pass_lineEdit = QLineEdit(self.frame)
        self.confirm_pass_lineEdit.setObjectName(u"confirm_pass_lineEdit")
        self.confirm_pass_lineEdit.setGeometry(QRect(10, 110, 251, 41))
        self.confirm_pass_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.confirm_pass_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.add_mail_lineEdit = QLineEdit(self.frame)
        self.add_mail_lineEdit.setObjectName(u"add_mail_lineEdit")
        self.add_mail_lineEdit.setGeometry(QRect(10, 160, 251, 41))
        self.add_mail_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.add_mail_lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.label = QLabel(self.register_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 61, 61))
        self.label.setPixmap(QPixmap(u":/png/icons/register.png"))
        self.label.setScaledContents(True)
        self.register_btn = QPushButton(self.register_page)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(40, 360, 251, 41))
        self.register_btn.setFont(font3)
        self.register_btn.setStyleSheet(u"color: rgb(146, 143, 170);")
        self.stackedWidget.addWidget(self.register_page)
        self.forget_page = QWidget()
        self.forget_page.setObjectName(u"forget_page")
        self.frame_3 = QFrame(self.forget_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 120, 271, 211))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.reset_user_lineEdit = QLineEdit(self.frame_3)
        self.reset_user_lineEdit.setObjectName(u"reset_user_lineEdit")
        self.reset_user_lineEdit.setGeometry(QRect(10, 10, 251, 41))
        self.reset_user_lineEdit.setFont(font1)
        self.reset_user_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.reset_pass_lineEdit = QLineEdit(self.frame_3)
        self.reset_pass_lineEdit.setObjectName(u"reset_pass_lineEdit")
        self.reset_pass_lineEdit.setGeometry(QRect(10, 110, 251, 41))
        self.reset_pass_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.reset_pass_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.comfirm_reset_pass = QLineEdit(self.frame_3)
        self.comfirm_reset_pass.setObjectName(u"comfirm_reset_pass")
        self.comfirm_reset_pass.setGeometry(QRect(10, 160, 251, 41))
        self.comfirm_reset_pass.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.comfirm_reset_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.reset_mail_lineEdit = QLineEdit(self.frame_3)
        self.reset_mail_lineEdit.setObjectName(u"reset_mail_lineEdit")
        self.reset_mail_lineEdit.setGeometry(QRect(10, 60, 251, 41))
        self.reset_mail_lineEdit.setStyleSheet(u"background-color: rgb(37, 30, 84);\n"
"padding:5px 5px;\n"
"border-radius:5px;\n"
"font: 12pt \"Segoe UI\";\n"
"selection-background-color: rgb(175, 169, 255); ")
        self.reset_mail_lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.reset_pass_btn = QPushButton(self.forget_page)
        self.reset_pass_btn.setObjectName(u"reset_pass_btn")
        self.reset_pass_btn.setGeometry(QRect(40, 360, 251, 41))
        self.reset_pass_btn.setFont(font3)
        self.reset_pass_btn.setStyleSheet(u"\n"
"color: rgb(24, 20, 57);\n"
"background-color: rgb(21, 158, 200);")
        self.back_to_login = QPushButton(self.forget_page)
        self.back_to_login.setObjectName(u"back_to_login")
        self.back_to_login.setGeometry(QRect(70, 410, 181, 21))
        self.back_to_login.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/png/icons/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_to_login.setIcon(icon3)
        self.label_6 = QLabel(self.forget_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 20, 100, 100))
        self.label_6.setPixmap(QPixmap(u":/png/icons/password-manager.png"))
        self.label_6.setScaledContents(True)
        self.checkBox_3 = QCheckBox(self.forget_page)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(40, 330, 141, 20))
        self.checkBox_3.setStyleSheet(u"color: rgb(117, 112, 153);")
        self.stackedWidget.addWidget(self.forget_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.gridLayout_2.addWidget(self.login_container, 0, 0, 1, 1)

        login_gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_gui)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(login_gui)
    # setupUi

    def retranslateUi(self, login_gui):
        login_gui.setWindowTitle(QCoreApplication.translate("login_gui", u"MainWindow", None))
        self.to_register.setText(QCoreApplication.translate("login_gui", u"Don't have account? Register", None))
        self.user_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"Username", None))
        self.pass_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"Password", None))
        self.hide_pass_btn.setText("")
        self.show_pass_btn.setText("")
        self.remember_me.setText(QCoreApplication.translate("login_gui", u"Remember Me", None))
        self.to_forget_pass.setText(QCoreApplication.translate("login_gui", u"Forgotten password? ", None))
        self.label_3.setText(QCoreApplication.translate("login_gui", u"Enter your information below", None))
        self.login_btn.setText(QCoreApplication.translate("login_gui", u"Login", None))
        self.label_4.setText("")
        self.close_btn.setText("")
        self.to_login.setText(QCoreApplication.translate("login_gui", u" Already registered? Login", None))
        self.label_2.setText(QCoreApplication.translate("login_gui", u"Enter your information below", None))
        self.checkBox.setText(QCoreApplication.translate("login_gui", u"Agree with our terms", None))
        self.add_user_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"Username", None))
        self.add_pass_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"Password", None))
        self.confirm_pass_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"Confirm Password", None))
        self.add_mail_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"XXXX@mail.com", None))
        self.label.setText("")
        self.register_btn.setText(QCoreApplication.translate("login_gui", u"Register", None))
        self.reset_user_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"Username", None))
        self.reset_pass_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"New Password", None))
        self.comfirm_reset_pass.setPlaceholderText(QCoreApplication.translate("login_gui", u"Confirm New Password", None))
        self.reset_mail_lineEdit.setPlaceholderText(QCoreApplication.translate("login_gui", u"XXXX@mail.com", None))
        self.reset_pass_btn.setText(QCoreApplication.translate("login_gui", u"Reset Password", None))
        self.back_to_login.setText(QCoreApplication.translate("login_gui", u" Back to Login", None))
        self.label_6.setText("")
        self.checkBox_3.setText(QCoreApplication.translate("login_gui", u"Agree with our terms", None))
    # retranslateUi

