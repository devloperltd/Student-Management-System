# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Addstudents_DialogLvmGXS.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDateTimeEdit, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from PySide6 import QtCore
from resources.ico_rc import *

class Ui_Addstudents_Dialog(object):
    def setupUi(self, Addstudents_Dialog):
        if not Addstudents_Dialog.objectName():
            Addstudents_Dialog.setObjectName(u"Addstudents_Dialog")

        Addstudents_Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Addstudents_Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Addstudents_Dialog.resize(813, 522)
        Addstudents_Dialog.setMinimumSize(QSize(813, 522))
        Addstudents_Dialog.setMaximumSize(QSize(813, 522))
        Addstudents_Dialog.setStyleSheet(u"QDialog{\n"
"	color: rgb(203, 192, 222);\n"
"	background: transparent;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(134, 136, 223);\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(37, 30, 84);\n"
"	padding:5px 5px;\n"
"	border-radius:8px;\n"
"	font: 12pt \"Segoe UI\";\n"
"	selection-background-color: rgb(29, 23, 67); \n"
" 	 focus {  \n"
" 	 background-color:rgb(192, 192, 255)};\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid #006080;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(52, 43, 124);\n"
"	color: rgb(203, 192, 222);\n"
"	padding:10px;\n"
"	height:30;\n"
"	border:none;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(65, 57, 156);\n"
"}")
        self.layoutWidget = QWidget(Addstudents_Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 811, 521))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.add_stud_nav = QWidget(self.layoutWidget)
        self.add_stud_nav.setObjectName(u"add_stud_nav")
        self.add_stud_nav.setMinimumSize(QSize(0, 50))
        self.add_stud_nav.setMaximumSize(QSize(16777215, 50))
        self.add_stud_nav.setStyleSheet(u"QWidget#add_stud_nav{\n"
"	background-color: rgb(23, 21, 59);\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"	border-bottom: 3px solid rgb(16, 14, 40);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.add_stud_nav)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.add_stud_nav)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(25, 25))
        self.label_10.setMaximumSize(QSize(25, 25))
        self.label_10.setStyleSheet(u"background-color: transparent;")
        self.label_10.setPixmap(QPixmap(u":/png/icons/sign-up.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label = QLabel(self.add_stud_nav)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(203, 192, 222);\n"
"background-color: transparent;")

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer = QSpacerItem(468, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(19)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.minimize_btn = QPushButton(self.add_stud_nav)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	border:0;\n"
"	padding:10px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/png/icons/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.add_stud_nav)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(30, 30))
        self.close_btn.setMaximumSize(QSize(16777215, 16777215))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	border:0;\n"
"	padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(235, 59, 90);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/png/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_11.addWidget(self.add_stud_nav)

        self.container = QWidget(self.layoutWidget)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"QWidget#container{\n"
"	background-color:rgb(23, 21, 59);\n"
"    border-top-left-radius: 0;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.container)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.container)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	color: rgb(53, 46, 126);\n"
"	border:1px solid rgb(53, 46, 126);\n"
"	border-radius:5px;\n"
"}")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(648, 8, 136, 156))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border:1px solid rgb(53, 46, 126);\n"
"	border-radius:5px;\n"
"}")
        self.groupBox_2.setFlat(False)
        self.up_std_btn = QPushButton(self.groupBox_2)
        self.up_std_btn.setObjectName(u"up_std_btn")
        self.up_std_btn.setGeometry(QRect(12, 10, 20, 20))
        self.up_std_btn.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setBold(True)
        self.up_std_btn.setFont(font1)
        self.up_std_btn.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(52, 168, 83);\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(63, 204, 101);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(52, 168, 83);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/png/icons/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.up_std_btn.setIcon(icon2)
        self.up_std_btn.setIconSize(QSize(10, 10))
        self.delete_std_btn = QPushButton(self.groupBox_2)
        self.delete_std_btn.setObjectName(u"delete_std_btn")
        self.delete_std_btn.setGeometry(QRect(105, 10, 20, 20))
        self.delete_std_btn.setFont(font1)
        self.delete_std_btn.setStyleSheet(u"QPushButton{\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(179, 55, 113, 255), stop:1 rgba(219, 78, 117, 255));\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(255, 89, 144);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:2px;\n"
"	padding-top: 1px;\n"
"	background-color: rgb(220, 69, 134);\n"
"}")
        self.delete_std_btn.setIcon(icon1)
        self.delete_std_btn.setIconSize(QSize(16, 16))
        self.default_photo = QLabel(self.groupBox_2)
        self.default_photo.setObjectName(u"default_photo")
        self.default_photo.setGeometry(QRect(44, 54, 51, 51))
        self.default_photo.setStyleSheet(u"")
        self.default_photo.setPixmap(QPixmap(u":/png/icons/no-photo.png"))
        self.default_photo.setScaledContents(True)
        self.photo_label = QLabel(self.groupBox_2)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setGeometry(QRect(8, 7, 121, 141))
        self.photo_label.setScaledContents(True)
        self.default_photo.raise_()
        self.photo_label.raise_()
        self.delete_std_btn.raise_()
        self.up_std_btn.raise_()
        self.line = QWidget(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 177, 769, 1))
        self.line.setStyleSheet(u"background-color: rgb(54, 44, 130);")
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(13, 280, 771, 65))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_3)

        self.address_lineEdit = QLineEdit(self.layoutWidget1)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(0, 35))
        self.address_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.address_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_11)

        self.city_lineEdit = QLineEdit(self.layoutWidget1)
        self.city_lineEdit.setObjectName(u"city_lineEdit")
        self.city_lineEdit.setMinimumSize(QSize(0, 35))
        self.city_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_10.addWidget(self.city_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 380, 771, 52))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_student_btn = QPushButton(self.layoutWidget2)
        self.add_student_btn.setObjectName(u"add_student_btn")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.add_student_btn.setFont(font3)
        self.add_student_btn.setStyleSheet(u"")
        icon3 = QIcon(QIcon.fromTheme(u"list-add"))
        self.add_student_btn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.add_student_btn)

        self.clear_student_btn = QPushButton(self.layoutWidget2)
        self.clear_student_btn.setObjectName(u"clear_student_btn")
        self.clear_student_btn.setFont(font3)
        self.clear_student_btn.setStyleSheet(u"")
        icon4 = QIcon(QIcon.fromTheme(u"system-reboot"))
        self.clear_student_btn.setIcon(icon4)

        self.horizontalLayout.addWidget(self.clear_student_btn)

        self.cancel_student_btn = QPushButton(self.layoutWidget2)
        self.cancel_student_btn.setObjectName(u"cancel_student_btn")
        self.cancel_student_btn.setFont(font3)
        self.cancel_student_btn.setStyleSheet(u"")
        icon5 = QIcon(QIcon.fromTheme(u"edit-clear"))
        self.cancel_student_btn.setIcon(icon5)

        self.horizontalLayout.addWidget(self.cancel_student_btn)

        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 10, 631, 151))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_2)

        self.first_name_lineEdit = QLineEdit(self.layoutWidget3)
        self.first_name_lineEdit.setObjectName(u"first_name_lineEdit")
        self.first_name_lineEdit.setMinimumSize(QSize(0, 35))
        self.first_name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.first_name_lineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_9)

        self.last_name_lineEdit = QLineEdit(self.layoutWidget3)
        self.last_name_lineEdit.setObjectName(u"last_name_lineEdit")
        self.last_name_lineEdit.setMinimumSize(QSize(0, 35))
        self.last_name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_5.addWidget(self.last_name_lineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.layoutWidget3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_4)

        self.phone_lineEdit = QLineEdit(self.layoutWidget3)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 35))
        self.phone_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.phone_lineEdit.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.phone_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_5)

        self.email_lineEdit = QLineEdit(self.layoutWidget3)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_12.addWidget(self.email_lineEdit)


        self.verticalLayout_9.addLayout(self.verticalLayout_12)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.layoutWidget4 = QWidget(self.groupBox)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(11, 190, 771, 77))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget4)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setMaximumSize(QSize(16777215, 35))
        self.gender_comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(37, 30, 84);\n"
"	color: rgb(134, 136, 223);\n"
"	border: 1px solid rgb(44, 38, 100);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	height:25px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 1px solid rgb(52, 84, 153);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 35px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(38, 33, 91);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/png/icons/arrow-down.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(134, 136, 223);	\n"
"	background-color: rgb(37, 30, 84);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(23, 21, 59); \n"
"	margin-top:3px;\n"
"	border-radius: 5px;\n"
"}\n"
"QComboBox::down-arrow { 	\n"
"	image: url(:/png/icons/arrow-down.png);\n"
"	width:"
                        "25px;\n"
"	height:25px;\n"
"}")
        self.gender_comboBox.setEditable(False)

        self.verticalLayout.addWidget(self.gender_comboBox)


        self.horizontalLayout_10.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.layoutWidget4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_7)

        self.class_comboBox = QComboBox(self.layoutWidget4)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setMaximumSize(QSize(16777215, 35))
        self.class_comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(37, 30, 84);\n"
"	color: rgb(134, 136, 223);\n"
"	border: 1px solid rgb(44, 38, 100);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	height:25px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 1px solid rgb(52, 84, 153);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 35px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(38, 33, 91);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/png/icons/arrow-down.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(134, 136, 223);	\n"
"	background-color: rgb(37, 30, 84);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(23, 21, 59); \n"
"	margin-top:3px;\n"
"	border-radius: 5px;\n"
"}\n"
"QComboBox::down-arrow { 	\n"
"	image: url(:/png/icons/arrow-down.png);\n"
"	width:"
                        "25px;\n"
"	height:25px;\n"
"}")

        self.verticalLayout_2.addWidget(self.class_comboBox)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_12 = QLabel(self.layoutWidget4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_12)

        self.birth_dateEdit = QDateEdit(self.layoutWidget4)
        self.birth_dateEdit.setObjectName(u"birth_dateEdit")
        self.birth_dateEdit.setAcceptDrops(False)
        self.birth_dateEdit.setAutoFillBackground(False)
        self.birth_dateEdit.setStyleSheet(u"QDateEdit{\n"
"	background-color: rgb(37, 30, 84);\n"
"	color: rgb(134, 136, 223);\n"
"	border-radius:6px;\n"
"	padding-left:5px;\n"
"	height:35px;\n"
"	border:none;\n"
"}\n"
"QDateEdit::down-arrow {\n"
"	image: url(:/png/icons/calendar.png);\n"
"	width:20px;\n"
"	height:20px;\n"
"	margin-right:10px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"#calendarWidget QWidget{\n"
"	alternate-background-color: rgb(52, 168, 83);\n"
"}\n"
"#qt_calendar_navigationbar{\n"
"	background-color: rgb(16, 14, 40);\n"
"}\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth{\n"
"	border:none;\n"
"	qproperty-icon:none;\n"
"	min-width:13px;\n"
"	max-width:13px;\n"
"	min-height:13px;\n"
"	min-height:13px;\n"
"	border-radius:5px;\n"
"	background-color: transparent;\n"
"	padding:5px;\n"
"}\n"
"#qt_calendar_prevmonth{\n"
"	margin-rig"
                        "ht:5px;\n"
"	image: url(:/newPrefix/icons/left-arrow.png);\n"
"}\n"
"#qt_calendar_nextmonth{\n"
"	margin-left:5px;	\n"
"	image: url(:/newPrefix/icons/right-arrow.png);\n"
"}\n"
"#qt_calendar_prevmonth:hover, \n"
"#qt_calendar_nextmonth:hover\n"
"{\n"
"	background-color: rgb(37, 30, 84);\n"
"}\n"
"#qt_calendar_prevmonth:pressed, \n"
"#qt_calendar_nextmonth:pressed\n"
"{\n"
"	background-color: rgb(37, 30, 84);\n"
"}\n"
"#qt_calendar_yearbutton{\n"
"	color: rgb(203, 192, 222);\n"
"	width: 50px;\n"
"	margin:5px;\n"
"	border-radius:5px;\n"
"	font-size:13px;\n"
"	padding:0 10px;\n"
"}\n"
"#qt_calendar_monthbutton{\n"
"	color: rgb(203, 192, 222);\n"
"	margin:5px 5px;\n"
"	border-radius:5px;\n"
"	font-size:14px;\n"
"	padding:0 5px;\n"
"}\n"
"#qt_calendar_yearbutton:hover,\n"
"#qt_calendar_monthbutton:hover\n"
"{\n"
"	background-color: rgb(37, 30, 84);\n"
"}\n"
"#qt_calendar_yearbutton:pressed,\n"
"#qt_calendar_monthbutton:pressed\n"
"{\n"
"	background-color: rgb(193, 104, 128);\n"
"}\n"
"#qt_calendar_yearedit{\n"
"	mi"
                        "n-width:90px;\n"
"	color: rgb(203, 192, 222);\n"
"	background: transparent;\n"
"	font-size:14px;\n"
"}\n"
"#calendarWidget QToolButton QMenu{\n"
"	background-color: rgb(37, 30, 84);\n"
"}\n"
"#calendarWidget QToolButton QMenu:item{\n"
"	padding:5px;\n"
"}\n"
"#calendarWidget QToolButton QMenu::item:selected:enabled{\n"
"	background-color: rgb(255, 255, 0);\n"
"}\n"
"#calendarWidget QToolButton::menu-indicator{\n"
"	nosubcontrol-origin:margin;\n"
"	subcontrol-position:right center;\n"
"	margin-top:10px;\n"
"	width:20px;\n"
"}\n"
"/* header row */\n"
"QCalendarWidget QWidget { alternate-background-color:rgb(52, 43, 124); }\n"
"QCalendarWidget QAbstractItemView:enabled\n"
"{\n"
"	font-size:14px;\n"
"	color: rgb(222, 222, 222);\n"
"	background-color: rgb(23, 21, 59);\n"
"	selection-background-color: rgb(64, 64, 64);\n"
"	selection-color: rgb(0, 255, 0);\n"
"}")
        self.birth_dateEdit.setWrapping(False)
        self.birth_dateEdit.setFrame(True)
        self.birth_dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.birth_dateEdit.setAccelerated(False)
        self.birth_dateEdit.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.birth_dateEdit.setProperty(u"showGroupSeparator", False)
        self.birth_dateEdit.setDateTime(QDateTime(QDate(1999, 12, 23), QTime(0, 0, 0)))
        self.birth_dateEdit.setMaximumDateTime(QDateTime(QDate(9999, 12, 29), QTime(23, 59, 59)))
        self.birth_dateEdit.setMinimumDate(QDate(1970, 9, 1))
        self.birth_dateEdit.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.birth_dateEdit.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.birth_dateEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.container)


        self.retranslateUi(Addstudents_Dialog)

        QMetaObject.connectSlotsByName(Addstudents_Dialog)
    # setupUi

    def retranslateUi(self, Addstudents_Dialog):
        Addstudents_Dialog.setWindowTitle(QCoreApplication.translate("Addstudents_Dialog", u"Dialog", None))
        self.label_10.setText("")
        self.label.setText(QCoreApplication.translate("Addstudents_Dialog", u" Add New Student", None))
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")
#if QT_CONFIG(tooltip)
        self.up_std_btn.setToolTip(QCoreApplication.translate("Addstudents_Dialog", u"Upload Photo", None))
#endif // QT_CONFIG(tooltip)
        self.up_std_btn.setText("")
#if QT_CONFIG(tooltip)
        self.delete_std_btn.setToolTip(QCoreApplication.translate("Addstudents_Dialog", u"Delete Photo", None))
#endif // QT_CONFIG(tooltip)
        self.delete_std_btn.setText("")
        self.default_photo.setText("")
        self.photo_label.setText("")
        self.label_3.setText(QCoreApplication.translate("Addstudents_Dialog", u"Address", None))
        self.address_lineEdit.setPlaceholderText(QCoreApplication.translate("Addstudents_Dialog", u"XXX City, Algeria", None))
        self.label_11.setText(QCoreApplication.translate("Addstudents_Dialog", u"Current City", None))
        self.city_lineEdit.setPlaceholderText(QCoreApplication.translate("Addstudents_Dialog", u"Ouled Djellal, Algeria", None))
        self.add_student_btn.setText(QCoreApplication.translate("Addstudents_Dialog", u"Add Student", None))
        self.clear_student_btn.setText(QCoreApplication.translate("Addstudents_Dialog", u" Clear", None))
        self.cancel_student_btn.setText(QCoreApplication.translate("Addstudents_Dialog", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("Addstudents_Dialog", u" First Name", None))
        self.first_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Addstudents_Dialog", u"Type first name here ", None))
        self.label_9.setText(QCoreApplication.translate("Addstudents_Dialog", u"Last Name", None))
        self.last_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Addstudents_Dialog", u"Type last name here ", None))
        self.label_4.setText(QCoreApplication.translate("Addstudents_Dialog", u"Phone Number", None))
        self.phone_lineEdit.setPlaceholderText(QCoreApplication.translate("Addstudents_Dialog", u"+213 00 00 00 00", None))
        self.label_5.setText(QCoreApplication.translate("Addstudents_Dialog", u"Email", None))
        self.email_lineEdit.setPlaceholderText(QCoreApplication.translate("Addstudents_Dialog", u"XXXX@mail.com", None))
        self.label_6.setText(QCoreApplication.translate("Addstudents_Dialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("Addstudents_Dialog", u"_____ Select _____", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("Addstudents_Dialog", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("Addstudents_Dialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("Addstudents_Dialog", u"Select Class", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("Addstudents_Dialog", u"_____ Select _____", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("Addstudents_Dialog", u"Grade 01", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("Addstudents_Dialog", u"Grade 02", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("Addstudents_Dialog", u"Grade 03", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("Addstudents_Dialog", u"Grade 04", None))

        self.label_12.setText(QCoreApplication.translate("Addstudents_Dialog", u"Date Of Birth", None))
        self.birth_dateEdit.setDisplayFormat(QCoreApplication.translate("Addstudents_Dialog", u"yyyy-MM-dd", None))
    # retranslateUi

