# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_delete_msgdftLUE.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, Signal, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel, QPushButton)
from PySide6 import QtCore
from resources.ico_rc import *
import sys

class Ui_confirm_delete_msg(QDialog):
    # Define a custom signal to be emitted when confirmation is accepted
    confirmed = Signal()
   
    def __init__(self, parent = None):
        super().__init__(parent)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(479, 261)
        self.setStyleSheet(u"*{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	background: transparent;\n"
"	padding:0;\n"
"	margin :0;\n"
"}")
        self.dialog_nav = QFrame(self)
        self.dialog_nav.setObjectName(u"dialog_nav")
        self.dialog_nav.setGeometry(QRect(0, 0, 479, 40))
        self.dialog_nav.setMinimumSize(QSize(0, 40))
        self.dialog_nav.setMaximumSize(QSize(16777215, 40))
        self.dialog_nav.setStyleSheet(u"#dialog_nav{\n"
"	background-color: rgb(18, 17, 47);\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: rgb(117, 112, 153);\n"
"}\n"
"#close_dialog_btn{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.dialog_nav.setFrameShape(QFrame.Shape.StyledPanel)
        self.dialog_nav.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.dialog_nav)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(14, 10, 111, 21))
        self.label_8.setStyleSheet(u"")
        self.close_dialog_btn = QPushButton(self.dialog_nav)
        self.close_dialog_btn.setObjectName(u"close_dialog_btn")
        self.close_dialog_btn.setGeometry(QRect(450, 10, 21, 21))
        self.close_dialog_btn.setStyleSheet(u"QPushButton{\n"
"	padding:15px;\n"
"	border:0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/png/icons/close_red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_dialog_btn.setIcon(icon)
        self.close_dialog_btn.setIconSize(QSize(10, 10))
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 40, 479, 221))
        self.frame.setAcceptDrops(False)
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(26, 24, 66);\n"
"	color: rgb(117, 112, 153);\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(38, 33, 91);\n"
"	color: rgb(117, 112, 153);\n"
"    border-radius: 3px;\n"
"    border-color: rgb(222, 70, 72);\n"
"    font: bold 12px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(44, 34, 104);\n"
"}\n"
"#warning_btn{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.content_msg_label = QLabel(self.frame)
        self.content_msg_label.setObjectName(u"content_msg_label")
        self.content_msg_label.setGeometry(QRect(30, 115, 361, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.content_msg_label.setFont(font)
        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(289, 160, 171, 41))
        self.cancel_btn.setStyleSheet(u"")
        self.confirm_close_btn = QPushButton(self.frame)
        self.confirm_close_btn.setObjectName(u"confirm_close_btn")
        self.confirm_close_btn.setGeometry(QRect(30, 160, 231, 41))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.confirm_close_btn.setFont(font1)
        self.confirm_close_btn.setStyleSheet(u"background-color: rgb(231, 143, 129);\n"
"color: rgb(18, 17, 47);\n"
"")
        self.title_msg_label = QLabel(self.frame)
        self.title_msg_label.setObjectName(u"title_msg_label")
        self.title_msg_label.setGeometry(QRect(10, 80, 451, 31))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.title_msg_label.setFont(font2)
        self.title_msg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 20, 50, 50))
        self.label.setPixmap(QPixmap(u":/png/icons/database1.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Assing Exit Button
        self.close_dialog_btn.clicked.connect(self.close)
        self.cancel_btn.clicked.connect(self.close)
        self.confirm_close_btn.clicked.connect(self.on_confirm)

    # setupUi

    def retranslateUi(self, confirm_delete_msg):
        confirm_delete_msg.setWindowTitle(QCoreApplication.translate("confirm_delete_msg", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("confirm_delete_msg", u"Confirm deletion!", None))
        self.close_dialog_btn.setText("")
        self.content_msg_label.setText(QCoreApplication.translate("confirm_delete_msg", u"Are you sure you want to delete this student from database?", None))
        self.cancel_btn.setText(QCoreApplication.translate("confirm_delete_msg", u"Cancel", None))
        self.confirm_close_btn.setText(QCoreApplication.translate("confirm_delete_msg", u"Continue with delete", None))
        self.title_msg_label.setText(QCoreApplication.translate("confirm_delete_msg", u" You will delete this student permanently!", None))
        self.label.setText("")
    # retranslateUi

    def on_confirm(self):
        self.accept()  # Close the dialog
        self.confirmed.emit()  # Emit the custom signal

    # Set the deletion message label
    def show_deletion(self, message):
        """Show the delete message."""
        self.title_msg_label.setText(message)
        self.content_msg_label.setText(message)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_confirm_delete_msg()
    win.show_deletion("This is a deletion message.")
    # Run loop the app
    app.exec()