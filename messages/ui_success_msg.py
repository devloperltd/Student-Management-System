# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'success_msgQNXmHi.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton,)
from PySide6 import QtCore
from resources.ico_rc import *
import sys

class Ui_success_msg(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(365, 70)
        self.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"}\n"
"QFrame {\n"
"	background-color: rgb(78, 255, 167);\n"
"	border-radius: 5px;\n"
"}\n"
"#success_msg_text{\n"
"	color: rgb(41, 135, 88);\n"
"}")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.success_messageBox = QFrame(self)
        self.success_messageBox.setObjectName(u"success_messageBox")
        self.success_messageBox.setEnabled(True)
        self.success_messageBox.setMinimumSize(QSize(0, 51))
        self.success_messageBox.setMaximumSize(QSize(16777215, 51))
        self.success_messageBox.setStyleSheet(u"")
        self.success_messageBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.success_messageBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.success_messageBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_success_msg = QLabel(self.success_messageBox)
        self.logo_success_msg.setObjectName(u"logo_success_msg")
        self.logo_success_msg.setMinimumSize(QSize(35, 35))
        self.logo_success_msg.setMaximumSize(QSize(35, 35))
        self.logo_success_msg.setPixmap(QPixmap(u":/png/icons/check.png"))
        self.logo_success_msg.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_success_msg)

        self.success_msg_text = QLabel(self.success_messageBox)
        self.success_msg_text.setObjectName(u"success_msg_text")
        font = QFont()
        font.setPointSize(10)
        self.success_msg_text.setFont(font)

        self.horizontalLayout.addWidget(self.success_msg_text)

        self.close_success_messageBox = QPushButton(self.success_messageBox)
        self.close_success_messageBox.setObjectName(u"close_success_messageBox")
        self.close_success_messageBox.setMinimumSize(QSize(21, 21))
        self.close_success_messageBox.setMaximumSize(QSize(21, 21))
        self.close_success_messageBox.setStyleSheet(u"QPushButton{\n"
"	padding:15px;\n"
"	border:0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/png/icons/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_success_messageBox.setIcon(icon)
        self.close_success_messageBox.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.close_success_messageBox, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.success_messageBox, 0, 0, 1, 1)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        self.close_success_messageBox.clicked.connect(self.close_success_message)

    # setupUi

    def retranslateUi(self, success_msg):
        success_msg.setWindowTitle(QCoreApplication.translate("success_msg", u"Dialog", None))
        self.logo_success_msg.setText("")
        self.success_msg_text.setText(QCoreApplication.translate("success_msg", u"", None))
        self.close_success_messageBox.setText("")
    # retranslateUi

    def show_success(self, message):
        """Show the success message and start the auto-close timer."""
        self.success_msg_text.setText(message)
        self.show()

    # Define the close function
    def close_success_message(self):
        """Close the success message box and stop the timer."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_success_msg()
    win.show_success("This is a success message.")
    # Run loop the app
    app.exec()