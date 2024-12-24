# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warning_msglqHvmy.ui'
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

class Ui_warning_msg(QDialog):
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
"	background-color: rgb(255, 219, 160);\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"#warning_msg_text{\n"
"	color: rgb(194, 132, 8);\n"
"}")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.warning_messageBox = QFrame(self)
        self.warning_messageBox.setObjectName(u"warning_messageBox")
        self.warning_messageBox.setEnabled(True)
        self.warning_messageBox.setMinimumSize(QSize(0, 51))
        self.warning_messageBox.setMaximumSize(QSize(16777215, 51))
        self.warning_messageBox.setStyleSheet(u"")
        self.warning_messageBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.warning_messageBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.warning_messageBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_warning_msg = QLabel(self.warning_messageBox)
        self.logo_warning_msg.setObjectName(u"logo_warning_msg")
        self.logo_warning_msg.setMinimumSize(QSize(35, 35))
        self.logo_warning_msg.setMaximumSize(QSize(35, 35))
        self.logo_warning_msg.setPixmap(QPixmap(u":/png/icons/alert.png"))
        self.logo_warning_msg.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_warning_msg)

        self.warning_msg_text = QLabel(self.warning_messageBox)
        self.warning_msg_text.setObjectName(u"warning_msg_text")
        font = QFont()
        font.setPointSize(10)
        self.warning_msg_text.setFont(font)

        self.horizontalLayout.addWidget(self.warning_msg_text)

        self.close_warning_messageBox = QPushButton(self.warning_messageBox)
        self.close_warning_messageBox.setObjectName(u"close_warning_messageBox")
        self.close_warning_messageBox.setMinimumSize(QSize(21, 21))
        self.close_warning_messageBox.setMaximumSize(QSize(21, 21))
        self.close_warning_messageBox.setStyleSheet(u"QPushButton{\n"
"	padding:15px;\n"
"	border:0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/png/icons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_warning_messageBox.setIcon(icon)
        self.close_warning_messageBox.setIconSize(QSize(10, 10))

        self.horizontalLayout.addWidget(self.close_warning_messageBox, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.warning_messageBox, 0, 0, 1, 1)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        self.close_warning_messageBox.clicked.connect(self.close_warning_message)

    # setupUi

    def retranslateUi(self, warning_msg):
        warning_msg.setWindowTitle(QCoreApplication.translate("warning_msg", u"Dialog", None))
        self.logo_warning_msg.setText("")
        self.warning_msg_text.setText(QCoreApplication.translate("warning_msg", u"", None))
        self.close_warning_messageBox.setText("")
    # retranslateUi

    def show_warning(self, message):
        """Show the warning message and start the auto-close timer."""
        self.warning_msg_text.setText(message)
        self.show()

    # Define the close function
    def close_warning_message(self):
        """Close the warning message box and stop the timer."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_warning_msg()
    win.show_warning("This is a warning message.")
    # Run loop the app
    app.exec()