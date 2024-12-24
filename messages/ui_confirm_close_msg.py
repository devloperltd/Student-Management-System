# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_close_msgFbHrFq.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, Signal, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
from PySide6 import QtCore
from resources.ico_rc import *
import sys

class Ui_Confirm_close_msg(QDialog):
    # Define a custom signal to be emitted when confirmation is accepted
    confirmed = Signal()

    def __init__(self, parent = None):
        super().__init__(parent)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(480, 261)
        self.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(26, 24, 66);\n"
"	color: rgb(117, 112, 153);\n"
"	border:0;\n"
"}\n"
"QLabel, QTextEdit, QFrame{\n"
"	background-color: transparent;\n"
"	color: rgb(117, 112, 153);\n"
"	border:0;\n"
"}\n"
"#confirm_close_btn{\n"
"	background-color: rgb(231, 143, 129);\n"
"	color: rgb(18, 17, 47);\n"
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
"}")
        self.confirm_close_btn = QPushButton(self)
        self.confirm_close_btn.setObjectName(u"confirm_close_btn")
        self.confirm_close_btn.setGeometry(QRect(20, 200, 241, 41))
        self.confirm_close_btn.setStyleSheet(u"")
        self.cancel_btn = QPushButton(self)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(280, 200, 181, 41))
        self.cancel_btn.setStyleSheet(u"")
        self.dialog_nav = QFrame(self)
        self.dialog_nav.setObjectName(u"dialog_nav")
        self.dialog_nav.setGeometry(QRect(-1, 0, 480, 41))
        self.dialog_nav.setStyleSheet(u"#dialog_nav{\n"
"	background-color: rgb(18, 17, 47);\n"
"    border: none;\n"
"}\n"
"")
        self.dialog_nav.setFrameShape(QFrame.Shape.StyledPanel)
        self.dialog_nav.setFrameShadow(QFrame.Shadow.Raised)
        self.close_dialog_btn = QPushButton(self.dialog_nav)
        self.close_dialog_btn.setObjectName(u"close_dialog_btn")
        self.close_dialog_btn.setGeometry(QRect(450, 10, 21, 21))
        self.close_dialog_btn.setStyleSheet(u"QPushButton{\n"
"    background-color: transparent;\n"
"	padding:15px;\n"
"	border:0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/png/icons/close_red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_dialog_btn.setIcon(icon)
        self.close_dialog_btn.setIconSize(QSize(10, 10))
        self.label_8 = QLabel(self.dialog_nav)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 141, 21))
        self.label_8.setStyleSheet(u"")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 60, 60, 60))
        self.label.setPixmap(QPixmap(u":/png/icons/warning.png"))
        self.label.setScaledContents(True)
        self.textEdit = QTextEdit(self)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 130, 291, 51))
        self.textEdit.setStyleSheet(u"line-height: 50px;")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Assing Exit Button
        self.close_dialog_btn.clicked.connect(self.close)
        self.cancel_btn.clicked.connect(self.close)
        self.confirm_close_btn.clicked.connect(self.on_confirm) 

    # setupUi

    def retranslateUi(self, confirm_close_msg):
        confirm_close_msg.setWindowTitle(QCoreApplication.translate("confirm_close_msg", u"Dialog", None))
        self.confirm_close_btn.setText(QCoreApplication.translate("confirm_close_msg", u"Continue with Close", None))
        self.cancel_btn.setText(QCoreApplication.translate("confirm_close_msg", u"Cancel", None))
        self.close_dialog_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("confirm_close_msg", u"Comfirm close Message!", None))
        self.label.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("confirm_close_msg", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\"> </span><span style=\" font-size:14pt; font-weight:700;\">You will close this window !</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Are you sure you want to close this window?</span></p></body></h"
                        "tml>", None))
    # retranslateUi

    def on_confirm(self):
        self.accept()  # Close the dialog
        self.confirmed.emit()  # Emit the custom signal


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_Confirm_close_msg()
    win.show()
    # Run loop the app
    app.exec()