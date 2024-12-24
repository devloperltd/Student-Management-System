# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_msgEfVwWw.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton)
from PySide6 import QtCore
from resources.ico_rc import *
import sys

class Ui_error_msg(QDialog):
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
"	background-color: rgb(241, 148, 138);\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"#error_msg_text{\n"
"	color: rgb(192, 57, 43);\n"
"}")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.error_messageBox = QFrame(self)
        self.error_messageBox.setObjectName(u"error_messageBox")
        self.error_messageBox.setEnabled(True)
        self.error_messageBox.setMinimumSize(QSize(0, 51))
        self.error_messageBox.setMaximumSize(QSize(16777215, 51))
        self.error_messageBox.setStyleSheet(u"")
        self.error_messageBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.error_messageBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.error_messageBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_error_msg = QLabel(self.error_messageBox)
        self.logo_error_msg.setObjectName(u"logo_error_msg")
        self.logo_error_msg.setMinimumSize(QSize(35, 35))
        self.logo_error_msg.setMaximumSize(QSize(35, 35))
        self.logo_error_msg.setPixmap(QPixmap(u":/png/icons/error.png"))
        self.logo_error_msg.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_error_msg)

        self.error_msg_text = QLabel(self.error_messageBox)
        self.error_msg_text.setObjectName(u"error_msg_text")
        font = QFont()
        font.setPointSize(10)
        self.error_msg_text.setFont(font)

        self.horizontalLayout.addWidget(self.error_msg_text)

        self.close_error_messageBox = QPushButton(self.error_messageBox)
        self.close_error_messageBox.setObjectName(u"close_error_messageBox")
        self.close_error_messageBox.setMinimumSize(QSize(21, 21))
        self.close_error_messageBox.setMaximumSize(QSize(21, 21))
        self.close_error_messageBox.setStyleSheet(u"QPushButton{\n"
"	padding:15px;\n"
"	border:0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/png/icons/close_red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_error_messageBox.setIcon(icon)
        self.close_error_messageBox.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.close_error_messageBox, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.error_messageBox, 0, 0, 1, 1)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        self.close_error_messageBox.clicked.connect(self.close_error_message)

    # setupUi

    def retranslateUi(self, error_msg):
        error_msg.setWindowTitle(QCoreApplication.translate("error_msg", u"Dialog", None))
        self.logo_error_msg.setText("")
        self.error_msg_text.setText(QCoreApplication.translate("error_msg", u"", None))
        self.close_error_messageBox.setText("")
    # retranslateUi

    def show_error(self, message):
        """Show the error message and start the auto-close timer."""
        self.error_msg_text.setText(message)
        self.show()

    # Define the close function
    def close_error_message(self):
        """Close the error message box and stop the timer."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_error_msg()
    win.show_error("This is a warning message.")
    # Run loop the app
    app.exec()