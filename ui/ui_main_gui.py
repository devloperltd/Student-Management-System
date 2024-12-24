# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_guiuwsgIh.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)
from resources.ico_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 698)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"*{\n"
"margin:0;\n"
"padding:0;\n"
"border:0;\n"
"}")
        self.styles = QWidget(MainWindow)
        self.styles.setObjectName(u"styles")
        sizePolicy.setHeightForWidth(self.styles.sizePolicy().hasHeightForWidth())
        self.styles.setSizePolicy(sizePolicy)
        self.styles.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(44, 38, 100);\n"
"	color: rgb(203, 192, 247);\n"
"}\n"
"QLabel, QFrame{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////\n"
"SideBar QWidget  */\n"
"\n"
"#left_sideBar{\n"
"	background-color: rgb(23, 21, 59);\n"
"	color: rgb(203, 192, 247);\n"
"}\n"
"#left_sideBar QPushButton {\n"
"	padding:10px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#left_sideBar  QPushButton::checked{\n"
"	background-color: rgb(56, 49, 130);\n"
"	color: rgb(0, 170, 127);\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"#main_nav{\n"
"	background-color:rgb(18, 15, 45);\n"
"	color: rgb(124, 132, 219);\n"
"}\n"
"#piechart_view{\n"
"	background-color: rgb(44, 38, 100);\n"
"}\n"
"#top_container{\n"
"	background-color: rgb(38, 33, 91);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////\n"
"Main Nav QPushButton  */\n"
"\n"
"#minimize_btn, #restore_btn, #close_btn{\n"
"	background-color:transparent;\n"
""
                        "	border:0;\n"
"}\n"
"#close_btn:hover{\n"
"	background-color:rgb(235, 59, 90);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* ////////////////////////////////////////////////////////\n"
"SearchBox QLineEdit  */\n"
"\n"
"#searchBox {\n"
"	image: url(:/png/icons/loupe.png);\n"
"	image-position:right;\n"
"	border:1px solid rgb(58, 52, 139);\n"
"	padding:5px;\n"
"	background-color: transparent;\n"
"	color: rgb(168, 152, 247);\n"
"	border-radius:5px;\n"
"}\n"
"#searchBox:focus{\n"
"    border: 1px solid #006080;\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: rgb(51, 45, 121);\n"
"	background-color:rgb(38, 33, 91);\n"
"	border-radius:10px;\n"
"    outline: none;\n"
"	padding: 10px;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color:rgb(23, 21, 59);\n"
"	color: rgb(134, 136, 223);\n"
"	height:35px;\n"
"	max-width: 30px;\n"
"	padding: 3px;\n"
"	border-top-l"
                        "eft-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	color: rgb(170, 146, 236);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color:rgb(13, 146, 244);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(51, 45, 121);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(23, 21, 59);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(71, 78, 147);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QSc"
                        "rollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(71, 78, 147);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(51, 45, 121);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(23, 21, 59);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(71, 78, 147);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subco"
                        "ntrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(71, 78, 147);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.gridLayout = QGridLayout(self.styles)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.main_nav = QWidget(self.styles)
        self.main_nav.setObjectName(u"main_nav")
        self.main_nav.setMinimumSize(QSize(0, 45))
        self.main_nav.setMaximumSize(QSize(16777215, 45))
        self.main_nav.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.main_nav)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.main_nav)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(35, 30))
        self.label.setMaximumSize(QSize(35, 30))
        self.label.setPixmap(QPixmap(u":/png/icons/frames.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.main_nav)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer = QSpacerItem(344, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minimize_btn = QPushButton(self.main_nav)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(30, 30))
        self.minimize_btn.setMaximumSize(QSize(30, 30))
        self.minimize_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/png/icons/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.minimize_btn)

        self.restore_btn = QPushButton(self.main_nav)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setMinimumSize(QSize(30, 30))
        self.restore_btn.setMaximumSize(QSize(30, 30))
        self.restore_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/png/icons/restore-maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_btn.setIcon(icon1)
        self.restore_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.restore_btn)

        self.close_btn = QPushButton(self.main_nav)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(30, 30))
        self.close_btn.setMaximumSize(QSize(30, 30))
        self.close_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/png/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.close_btn)


        self.horizontalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout.addWidget(self.main_nav, 0, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.left_sideBar = QWidget(self.styles)
        self.left_sideBar.setObjectName(u"left_sideBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_sideBar.sizePolicy().hasHeightForWidth())
        self.left_sideBar.setSizePolicy(sizePolicy2)
        self.left_sideBar.setMinimumSize(QSize(70, 0))
        self.left_sideBar.setMaximumSize(QSize(70, 16777215))
        self.left_sideBar.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.left_sideBar)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, 9, -1)
        self.label_3 = QLabel(self.left_sideBar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 35))
        self.label_3.setMaximumSize(QSize(55, 35))
        self.label_3.setPixmap(QPixmap(u":/png/icons/LB_1.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.dashboard_btn = QPushButton(self.left_sideBar)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dashboard_btn.sizePolicy().hasHeightForWidth())
        self.dashboard_btn.setSizePolicy(sizePolicy3)
        self.dashboard_btn.setMinimumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/png/icons/layout_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/png/icons/layout.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_btn.setIcon(icon3)
        self.dashboard_btn.setIconSize(QSize(28, 28))
        self.dashboard_btn.setCheckable(True)
        self.dashboard_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.dashboard_btn)

        self.institution_btn = QPushButton(self.left_sideBar)
        self.institution_btn.setObjectName(u"institution_btn")
        sizePolicy3.setHeightForWidth(self.institution_btn.sizePolicy().hasHeightForWidth())
        self.institution_btn.setSizePolicy(sizePolicy3)
        self.institution_btn.setMinimumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u":/png/icons/bank_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/png/icons/bank1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_btn.setIcon(icon4)
        self.institution_btn.setIconSize(QSize(28, 28))
        self.institution_btn.setCheckable(True)
        self.institution_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.institution_btn)

        self.manage_student_btn = QPushButton(self.left_sideBar)
        self.manage_student_btn.setObjectName(u"manage_student_btn")
        sizePolicy3.setHeightForWidth(self.manage_student_btn.sizePolicy().hasHeightForWidth())
        self.manage_student_btn.setSizePolicy(sizePolicy3)
        self.manage_student_btn.setMinimumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u":/png/icons/group1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/png/icons/group.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.manage_student_btn.setIcon(icon5)
        self.manage_student_btn.setIconSize(QSize(28, 28))
        self.manage_student_btn.setCheckable(True)
        self.manage_student_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.manage_student_btn)

        self.manage_teacher_btn = QPushButton(self.left_sideBar)
        self.manage_teacher_btn.setObjectName(u"manage_teacher_btn")
        sizePolicy3.setHeightForWidth(self.manage_teacher_btn.sizePolicy().hasHeightForWidth())
        self.manage_teacher_btn.setSizePolicy(sizePolicy3)
        self.manage_teacher_btn.setMinimumSize(QSize(50, 50))
        icon6 = QIcon()
        icon6.addFile(u":/png/icons/school1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/png/icons/school.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.manage_teacher_btn.setIcon(icon6)
        self.manage_teacher_btn.setIconSize(QSize(28, 28))
        self.manage_teacher_btn.setCheckable(True)
        self.manage_teacher_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.manage_teacher_btn)

        self.manage_finances_btn = QPushButton(self.left_sideBar)
        self.manage_finances_btn.setObjectName(u"manage_finances_btn")
        sizePolicy3.setHeightForWidth(self.manage_finances_btn.sizePolicy().hasHeightForWidth())
        self.manage_finances_btn.setSizePolicy(sizePolicy3)
        self.manage_finances_btn.setMinimumSize(QSize(50, 50))
        icon7 = QIcon()
        icon7.addFile(u":/png/icons/trend1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/png/icons/trend.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.manage_finances_btn.setIcon(icon7)
        self.manage_finances_btn.setIconSize(QSize(28, 28))
        self.manage_finances_btn.setCheckable(True)
        self.manage_finances_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.manage_finances_btn)

        self.fee_btn = QPushButton(self.left_sideBar)
        self.fee_btn.setObjectName(u"fee_btn")
        sizePolicy3.setHeightForWidth(self.fee_btn.sizePolicy().hasHeightForWidth())
        self.fee_btn.setSizePolicy(sizePolicy3)
        self.fee_btn.setMinimumSize(QSize(50, 50))
        icon8 = QIcon()
        icon8.addFile(u":/png/icons/wallet1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/png/icons/wallet.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.fee_btn.setIcon(icon8)
        self.fee_btn.setIconSize(QSize(28, 28))
        self.fee_btn.setCheckable(True)
        self.fee_btn.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.fee_btn)


        self.verticalLayout_11.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.settings_btn = QPushButton(self.left_sideBar)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy3.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy3)
        self.settings_btn.setMinimumSize(QSize(50, 50))
        icon9 = QIcon()
        icon9.addFile(u":/png/icons/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/png/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_btn.setIcon(icon9)
        self.settings_btn.setIconSize(QSize(28, 28))
        self.settings_btn.setCheckable(True)
        self.settings_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.settings_btn)

        self.help_btn = QPushButton(self.left_sideBar)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy3.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy3)
        self.help_btn.setMinimumSize(QSize(50, 50))
        icon10 = QIcon()
        icon10.addFile(u":/png/icons/help1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/png/icons/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.help_btn.setIcon(icon10)
        self.help_btn.setIconSize(QSize(28, 28))
        self.help_btn.setCheckable(True)
        self.help_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.help_btn)


        self.verticalLayout_11.addLayout(self.verticalLayout_3)


        self.horizontalLayout_6.addWidget(self.left_sideBar)

        self.expand_sidBar = QWidget(self.styles)
        self.expand_sidBar.setObjectName(u"expand_sidBar")
        sizePolicy2.setHeightForWidth(self.expand_sidBar.sizePolicy().hasHeightForWidth())
        self.expand_sidBar.setSizePolicy(sizePolicy2)
        self.expand_sidBar.setMinimumSize(QSize(200, 0))
        self.expand_sidBar.setMaximumSize(QSize(200, 16777215))
        self.expand_sidBar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(23, 21, 59);\n"
"	color: rgb(203, 192, 247);\n"
"}\n"
"QPushButton{\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.expand_sidBar)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 9, 9, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.label_4 = QLabel(self.expand_sidBar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 35))
        self.label_4.setMaximumSize(QSize(55, 35))
        self.label_4.setPixmap(QPixmap(u":/png/icons/LB_1.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.expand_sidBar)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)

        self.verticalLayout_14.addWidget(self.label_5)

        self.label_6 = QLabel(self.expand_sidBar)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_14.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.dashboard2_btn = QPushButton(self.expand_sidBar)
        self.dashboard2_btn.setObjectName(u"dashboard2_btn")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.dashboard2_btn.setFont(font1)
        self.dashboard2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton::checked{\n"
"	background-color: rgb(56, 49, 130);\n"
"	color: rgb(198, 187, 241);\n"
"	border-radius:3px;\n"
"}")
        self.dashboard2_btn.setIcon(icon3)
        self.dashboard2_btn.setIconSize(QSize(18, 18))
        self.dashboard2_btn.setCheckable(True)
        self.dashboard2_btn.setAutoRepeat(False)
        self.dashboard2_btn.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.dashboard2_btn)

        self.institution2_btn = QPushButton(self.expand_sidBar)
        self.institution2_btn.setObjectName(u"institution2_btn")
        font2 = QFont()
        font2.setPointSize(11)
        self.institution2_btn.setFont(font2)
        self.institution2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton::checked{\n"
"	background-color: rgb(56, 49, 130);\n"
"	color: rgb(198, 187, 241);\n"
"	border-radius:3px;\n"
"}")
        self.institution2_btn.setIcon(icon4)
        self.institution2_btn.setIconSize(QSize(18, 18))
        self.institution2_btn.setCheckable(True)
        self.institution2_btn.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.institution2_btn)

        self.dropdown_menu1 = QFrame(self.expand_sidBar)
        self.dropdown_menu1.setObjectName(u"dropdown_menu1")
        self.dropdown_menu1.setStyleSheet(u"")
        self.dropdown_menu1.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_menu1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.dropdown_menu1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.manage_student2_btn = QPushButton(self.dropdown_menu1)
        self.manage_student2_btn.setObjectName(u"manage_student2_btn")
        font3 = QFont()
        font3.setPointSize(10)
        self.manage_student2_btn.setFont(font3)
        self.manage_student2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	image: url(:/png/icons/arrow-up.png);\n"
"	image-position:right;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton:checked{	\n"
"	image: url(:/png/icons/arrow-down.png);\n"
"	image-position:right;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/png/icons/group.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/png/icons/group1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.manage_student2_btn.setIcon(icon11)
        self.manage_student2_btn.setIconSize(QSize(18, 18))
        self.manage_student2_btn.setCheckable(True)
        self.manage_student2_btn.setChecked(False)
        self.manage_student2_btn.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.manage_student2_btn)

        self.subMenu1 = QFrame(self.dropdown_menu1)
        self.subMenu1.setObjectName(u"subMenu1")
        sizePolicy2.setHeightForWidth(self.subMenu1.sizePolicy().hasHeightForWidth())
        self.subMenu1.setSizePolicy(sizePolicy2)
        self.subMenu1.setStyleSheet(u"QPushButton{\n"
"	padding-left: 40px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(241, 114, 213);\n"
"}")
        self.subMenu1.setFrameShape(QFrame.Shape.StyledPanel)
        self.subMenu1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.subMenu1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.student_info_btn = QPushButton(self.subMenu1)
        self.student_info_btn.setObjectName(u"student_info_btn")
        self.student_info_btn.setStyleSheet(u"")
        self.student_info_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.student_info_btn)

        self.student_pay_btn = QPushButton(self.subMenu1)
        self.student_pay_btn.setObjectName(u"student_pay_btn")
        self.student_pay_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.student_pay_btn)

        self.student_trans_btn = QPushButton(self.subMenu1)
        self.student_trans_btn.setObjectName(u"student_trans_btn")
        self.student_trans_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.student_trans_btn)


        self.verticalLayout_4.addWidget(self.subMenu1)


        self.verticalLayout_12.addWidget(self.dropdown_menu1)

        self.dropdown_menu2 = QFrame(self.expand_sidBar)
        self.dropdown_menu2.setObjectName(u"dropdown_menu2")
        self.dropdown_menu2.setStyleSheet(u"")
        self.dropdown_menu2.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_menu2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.dropdown_menu2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.manage_teacher2_btn = QPushButton(self.dropdown_menu2)
        self.manage_teacher2_btn.setObjectName(u"manage_teacher2_btn")
        self.manage_teacher2_btn.setFont(font3)
        self.manage_teacher2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	image: url(:/png/icons/arrow-up.png);\n"
"	image-position:right;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton::checked{\n"
"	image: url(:/png/icons/arrow-down.png);\n"
"	image-position:right;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/png/icons/school.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/png/icons/school1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.manage_teacher2_btn.setIcon(icon12)
        self.manage_teacher2_btn.setIconSize(QSize(18, 18))
        self.manage_teacher2_btn.setCheckable(True)
        self.manage_teacher2_btn.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.manage_teacher2_btn)

        self.subMenu2 = QFrame(self.dropdown_menu2)
        self.subMenu2.setObjectName(u"subMenu2")
        sizePolicy2.setHeightForWidth(self.subMenu2.sizePolicy().hasHeightForWidth())
        self.subMenu2.setSizePolicy(sizePolicy2)
        self.subMenu2.setStyleSheet(u"QPushButton{\n"
"	padding-left: 45px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(241, 114, 213);\n"
"}")
        self.subMenu2.setFrameShape(QFrame.Shape.StyledPanel)
        self.subMenu2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.subMenu2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.teacher_info_btn = QPushButton(self.subMenu2)
        self.teacher_info_btn.setObjectName(u"teacher_info_btn")
        self.teacher_info_btn.setCheckable(True)

        self.verticalLayout_7.addWidget(self.teacher_info_btn)

        self.teacher_salar_btn = QPushButton(self.subMenu2)
        self.teacher_salar_btn.setObjectName(u"teacher_salar_btn")
        self.teacher_salar_btn.setCheckable(True)

        self.verticalLayout_7.addWidget(self.teacher_salar_btn)

        self.teacher_trans_btn = QPushButton(self.subMenu2)
        self.teacher_trans_btn.setObjectName(u"teacher_trans_btn")
        self.teacher_trans_btn.setCheckable(True)

        self.verticalLayout_7.addWidget(self.teacher_trans_btn)


        self.verticalLayout_8.addWidget(self.subMenu2)


        self.verticalLayout_12.addWidget(self.dropdown_menu2)

        self.dropdown_menu3 = QFrame(self.expand_sidBar)
        self.dropdown_menu3.setObjectName(u"dropdown_menu3")
        self.dropdown_menu3.setStyleSheet(u"")
        self.dropdown_menu3.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_menu3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.dropdown_menu3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.manage_finances2_btn = QPushButton(self.dropdown_menu3)
        self.manage_finances2_btn.setObjectName(u"manage_finances2_btn")
        self.manage_finances2_btn.setFont(font3)
        self.manage_finances2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	image: url(:/png/icons/arrow-up.png);\n"
"	image-position:right;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton::checked{\n"
"	image: url(:/png/icons/arrow-down.png);\n"
"	image-position:right;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/png/icons/trend.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/png/icons/trend1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.manage_finances2_btn.setIcon(icon13)
        self.manage_finances2_btn.setIconSize(QSize(18, 18))
        self.manage_finances2_btn.setCheckable(True)
        self.manage_finances2_btn.setAutoExclusive(False)

        self.verticalLayout_9.addWidget(self.manage_finances2_btn)

        self.subMenu3 = QFrame(self.dropdown_menu3)
        self.subMenu3.setObjectName(u"subMenu3")
        sizePolicy2.setHeightForWidth(self.subMenu3.sizePolicy().hasHeightForWidth())
        self.subMenu3.setSizePolicy(sizePolicy2)
        self.subMenu3.setStyleSheet(u"QPushButton{\n"
"	padding-left: 45px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(241, 114, 213);\n"
"}")
        self.subMenu3.setFrameShape(QFrame.Shape.StyledPanel)
        self.subMenu3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.subMenu3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.budgets_btn = QPushButton(self.subMenu3)
        self.budgets_btn.setObjectName(u"budgets_btn")
        self.budgets_btn.setCheckable(True)

        self.verticalLayout_10.addWidget(self.budgets_btn)

        self.expenses_btn = QPushButton(self.subMenu3)
        self.expenses_btn.setObjectName(u"expenses_btn")
        self.expenses_btn.setCheckable(True)

        self.verticalLayout_10.addWidget(self.expenses_btn)

        self.business_over_btn = QPushButton(self.subMenu3)
        self.business_over_btn.setObjectName(u"business_over_btn")
        self.business_over_btn.setCheckable(True)

        self.verticalLayout_10.addWidget(self.business_over_btn)


        self.verticalLayout_9.addWidget(self.subMenu3)


        self.verticalLayout_12.addWidget(self.dropdown_menu3)

        self.fee2_btn = QPushButton(self.expand_sidBar)
        self.fee2_btn.setObjectName(u"fee2_btn")
        self.fee2_btn.setFont(font2)
        self.fee2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton::checked{\n"
"	background-color: rgb(56, 49, 130);\n"
"	color: rgb(198, 187, 241);\n"
"	border-radius:3px;\n"
"}")
        self.fee2_btn.setIcon(icon8)
        self.fee2_btn.setIconSize(QSize(18, 18))
        self.fee2_btn.setCheckable(True)
        self.fee2_btn.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.fee2_btn)


        self.verticalLayout_15.addLayout(self.verticalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 95, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.settings2_btn = QPushButton(self.expand_sidBar)
        self.settings2_btn.setObjectName(u"settings2_btn")
        self.settings2_btn.setFont(font2)
        self.settings2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton::checked{\n"
"	background-color: rgb(56, 49, 130);\n"
"	color: rgb(198, 187, 241);\n"
"	border-radius:3px;\n"
"}")
        self.settings2_btn.setIcon(icon9)
        self.settings2_btn.setIconSize(QSize(18, 18))
        self.settings2_btn.setCheckable(True)
        self.settings2_btn.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.settings2_btn)

        self.help2_btn = QPushButton(self.expand_sidBar)
        self.help2_btn.setObjectName(u"help2_btn")
        self.help2_btn.setFont(font2)
        self.help2_btn.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"	padding-left:15px;\n"
"}\n"
"QPushButton::checked{\n"
"	background-color: rgb(56, 49, 130);\n"
"	color: rgb(198, 187, 241);\n"
"	border-radius:3px;\n"
"}")
        self.help2_btn.setIcon(icon10)
        self.help2_btn.setIconSize(QSize(22, 22))
        self.help2_btn.setCheckable(True)
        self.help2_btn.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.help2_btn)


        self.verticalLayout_15.addLayout(self.verticalLayout_13)


        self.horizontalLayout_6.addWidget(self.expand_sidBar)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.body = QWidget(self.styles)
        self.body.setObjectName(u"body")
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.body)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.body)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(38, 33, 91);\n"
"	color: rgb(203, 192, 247);\n"
"}\n"
"#logout_btn{\n"
"	background-color: rgb(83, 92, 145);\n"
"	border-radius:5px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#logout_btn:hover{\n"
"	background-color: rgb(179, 85, 132);\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.header)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.toggle_btn = QPushButton(self.header)
        self.toggle_btn.setObjectName(u"toggle_btn")
        sizePolicy3.setHeightForWidth(self.toggle_btn.sizePolicy().hasHeightForWidth())
        self.toggle_btn.setSizePolicy(sizePolicy3)
        self.toggle_btn.setMinimumSize(QSize(40, 40))
        self.toggle_btn.setMaximumSize(QSize(45, 45))
        icon14 = QIcon()
        icon14.addFile(u":/png/icons/menu_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggle_btn.setIcon(icon14)
        self.toggle_btn.setIconSize(QSize(38, 38))
        self.toggle_btn.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.toggle_btn)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.header)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(self.header)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setPointSize(9)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(116, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logout_btn = QPushButton(self.header)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy3.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy3)
        self.logout_btn.setMinimumSize(QSize(151, 35))
        self.logout_btn.setMaximumSize(QSize(16777215, 35))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.logout_btn.setFont(font6)
        self.logout_btn.setStyleSheet(u"color: rgb(145, 162, 254);")

        self.horizontalLayout_2.addWidget(self.logout_btn)

        self.avatar = QLabel(self.header)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setMinimumSize(QSize(35, 35))
        self.avatar.setMaximumSize(QSize(40, 40))
        self.avatar.setPixmap(QPixmap(u":/png/icons/profile.png"))
        self.avatar.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.avatar)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.Dashboard_0 = QWidget()
        self.Dashboard_0.setObjectName(u"Dashboard_0")
        self.verticalLayout_22 = QVBoxLayout(self.Dashboard_0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.student_card = QFrame(self.Dashboard_0)
        self.student_card.setObjectName(u"student_card")
        sizePolicy3.setHeightForWidth(self.student_card.sizePolicy().hasHeightForWidth())
        self.student_card.setSizePolicy(sizePolicy3)
        self.student_card.setMinimumSize(QSize(0, 200))
        self.student_card.setMaximumSize(QSize(16777215, 300))
        self.student_card.setStyleSheet(u"background-color: rgb(35, 30, 80);")
        self.student_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.student_card.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.student_card)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_12 = QLabel(self.student_card)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 40))
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.label_12.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.total_students = QFrame(self.student_card)
        self.total_students.setObjectName(u"total_students")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.total_students.sizePolicy().hasHeightForWidth())
        self.total_students.setSizePolicy(sizePolicy4)
        self.total_students.setMinimumSize(QSize(150, 0))
        self.total_students.setMaximumSize(QSize(215, 130))
        self.total_students.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(107, 187, 245);\n"
"	padding-left:5px;\n"
"}\n"
"#total_students{\n"
"	background-color: rgb(13, 146, 244);\n"
"	border-radius:10px;\n"
"	image: url(:/png/icons/classmates.png);\n"
"	image-position:right;\n"
"}")
        self.total_students.setFrameShape(QFrame.Shape.StyledPanel)
        self.total_students.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.total_students)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.total_student_label = QLabel(self.total_students)
        self.total_student_label.setObjectName(u"total_student_label")
        font8 = QFont()
        font8.setPointSize(25)
        font8.setBold(True)
        self.total_student_label.setFont(font8)
        self.total_student_label.setStyleSheet(u"")
        self.total_student_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.total_student_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.label_28 = QLabel(self.total_students)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font4)
        self.label_28.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.label_28, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.show_more_students_btn = QToolButton(self.total_students)
        self.show_more_students_btn.setObjectName(u"show_more_students_btn")
        self.show_more_students_btn.setMinimumSize(QSize(150, 0))
        self.show_more_students_btn.setMaximumSize(QSize(215, 25))
        self.show_more_students_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_more_students_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.show_more_students_btn.setStyleSheet(u"#show_more_students_btn{\n"
"	background-color: rgb(10, 106, 175);\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	color: rgb(107, 187, 245);\n"
"	padding: 0  5px  0  5px;\n"
"}\n"
"#show_more_students_btn:hover{\n"
"	background-color: rgb(9, 96, 158);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/png/icons/arrow-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_more_students_btn.setIcon(icon15)
        self.show_more_students_btn.setIconSize(QSize(20, 20))
        self.show_more_students_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_17.addWidget(self.show_more_students_btn, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_9.addWidget(self.total_students)

        self.total_male = QFrame(self.student_card)
        self.total_male.setObjectName(u"total_male")
        sizePolicy4.setHeightForWidth(self.total_male.sizePolicy().hasHeightForWidth())
        self.total_male.setSizePolicy(sizePolicy4)
        self.total_male.setMinimumSize(QSize(150, 0))
        self.total_male.setMaximumSize(QSize(215, 130))
        self.total_male.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color:rgb(252, 206, 99);\n"
"	padding-left:5px;\n"
"}\n"
"#total_male{\n"
"	background-color: rgb(255, 178, 0);\n"
"	border-radius:10px;\n"
"	image: url(:/png/icons/male.png);\n"
"	image-position:right;\n"
"}")
        self.total_male.setFrameShape(QFrame.Shape.StyledPanel)
        self.total_male.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.total_male)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.total_male_label = QLabel(self.total_male)
        self.total_male_label.setObjectName(u"total_male_label")
        self.total_male_label.setFont(font8)
        self.total_male_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_18.addWidget(self.total_male_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.label_31 = QLabel(self.total_male)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font4)

        self.verticalLayout_18.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.show_more_male_btn = QToolButton(self.total_male)
        self.show_more_male_btn.setObjectName(u"show_more_male_btn")
        self.show_more_male_btn.setMinimumSize(QSize(150, 0))
        self.show_more_male_btn.setMaximumSize(QSize(215, 25))
        self.show_more_male_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_more_male_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.show_more_male_btn.setAutoFillBackground(False)
        self.show_more_male_btn.setStyleSheet(u"#show_more_male_btn{\n"
"	background-color: rgb(202, 138, 0);\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	color: rgb(252, 206, 99);\n"
"	padding: 0  5px  0  5px;\n"
"}\n"
"#show_more_male_btn:hover{\n"
"	background-color: rgb(184, 123, 0);\n"
"}")
        self.show_more_male_btn.setIcon(icon15)
        self.show_more_male_btn.setIconSize(QSize(20, 20))
        self.show_more_male_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.show_more_male_btn.setAutoRaise(False)

        self.verticalLayout_18.addWidget(self.show_more_male_btn, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_9.addWidget(self.total_male)

        self.total_female = QFrame(self.student_card)
        self.total_female.setObjectName(u"total_female")
        sizePolicy4.setHeightForWidth(self.total_female.sizePolicy().hasHeightForWidth())
        self.total_female.setSizePolicy(sizePolicy4)
        self.total_female.setMinimumSize(QSize(150, 0))
        self.total_female.setMaximumSize(QSize(215, 130))
        self.total_female.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(243, 153, 175);\n"
"	padding-left:5px;\n"
"}\n"
"#total_female{\n"
"	background-color: rgb(240, 90, 126);\n"
"	border-radius:10px;\n"
"	image: url(:/png/icons/female.png);\n"
"	image-position:right;\n"
"}")
        self.total_female.setFrameShape(QFrame.Shape.StyledPanel)
        self.total_female.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.total_female)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.total_female_label = QLabel(self.total_female)
        self.total_female_label.setObjectName(u"total_female_label")
        self.total_female_label.setFont(font8)
        self.total_female_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_19.addWidget(self.total_female_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.label_36 = QLabel(self.total_female)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font4)

        self.verticalLayout_19.addWidget(self.label_36, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.show_more_female_btn = QToolButton(self.total_female)
        self.show_more_female_btn.setObjectName(u"show_more_female_btn")
        sizePolicy4.setHeightForWidth(self.show_more_female_btn.sizePolicy().hasHeightForWidth())
        self.show_more_female_btn.setSizePolicy(sizePolicy4)
        self.show_more_female_btn.setMinimumSize(QSize(150, 0))
        self.show_more_female_btn.setMaximumSize(QSize(215, 25))
        self.show_more_female_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_more_female_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.show_more_female_btn.setStyleSheet(u"#show_more_female_btn{\n"
"	background-color: rgb(150, 56, 80);\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	color: rgb(243, 153, 175);\n"
"	padding: 0  5px  0  5px;\n"
"}\n"
"#show_more_female_btn:hover{\n"
"	background-color: rgb(136, 51, 73);\n"
"}")
        self.show_more_female_btn.setIcon(icon15)
        self.show_more_female_btn.setIconSize(QSize(20, 20))
        self.show_more_female_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_19.addWidget(self.show_more_female_btn, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_9.addWidget(self.total_female)

        self.students_marks = QFrame(self.student_card)
        self.students_marks.setObjectName(u"students_marks")
        sizePolicy4.setHeightForWidth(self.students_marks.sizePolicy().hasHeightForWidth())
        self.students_marks.setSizePolicy(sizePolicy4)
        self.students_marks.setMinimumSize(QSize(150, 0))
        self.students_marks.setMaximumSize(QSize(215, 130))
        self.students_marks.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(130, 198, 191);\n"
"	padding-left:5px;\n"
"}\n"
"#students_marks{\n"
"	background-color: rgb(33, 156, 144);\n"
"	border-radius:10px;\n"
"	image: url(:/png/icons/notepad.png);\n"
"	image-position:right;\n"
"}")
        self.students_marks.setFrameShape(QFrame.Shape.StyledPanel)
        self.students_marks.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.students_marks)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.total_marks_label = QLabel(self.students_marks)
        self.total_marks_label.setObjectName(u"total_marks_label")
        self.total_marks_label.setFont(font8)
        self.total_marks_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_20.addWidget(self.total_marks_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.label_37 = QLabel(self.students_marks)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)

        self.verticalLayout_20.addWidget(self.label_37, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.show_more_marks_btn = QToolButton(self.students_marks)
        self.show_more_marks_btn.setObjectName(u"show_more_marks_btn")
        sizePolicy4.setHeightForWidth(self.show_more_marks_btn.sizePolicy().hasHeightForWidth())
        self.show_more_marks_btn.setSizePolicy(sizePolicy4)
        self.show_more_marks_btn.setMinimumSize(QSize(150, 0))
        self.show_more_marks_btn.setMaximumSize(QSize(215, 25))
        self.show_more_marks_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_more_marks_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.show_more_marks_btn.setStyleSheet(u"#show_more_marks_btn{\n"
"	background-color: rgb(22, 103, 95);\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	color: rgb(130, 198, 191);\n"
"	padding: 0  5px  0  5px;\n"
"}\n"
"#show_more_marks_btn:hover{\n"
"	background-color: rgb(20, 93, 86);\n"
"}")
        self.show_more_marks_btn.setIcon(icon15)
        self.show_more_marks_btn.setIconSize(QSize(20, 20))
        self.show_more_marks_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_20.addWidget(self.show_more_marks_btn, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_9.addWidget(self.students_marks)

        self.eliminate_list = QFrame(self.student_card)
        self.eliminate_list.setObjectName(u"eliminate_list")
        sizePolicy4.setHeightForWidth(self.eliminate_list.sizePolicy().hasHeightForWidth())
        self.eliminate_list.setSizePolicy(sizePolicy4)
        self.eliminate_list.setMinimumSize(QSize(150, 0))
        self.eliminate_list.setMaximumSize(QSize(215, 130))
        self.eliminate_list.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(131, 117, 117);\n"
"	padding-left:5px;\n"
"}\n"
"#eliminate_list{\n"
"	background-color: rgb(80, 60, 60);\n"
"	border-radius:10px;\n"
"	image: url(:/png/icons/paper.png);\n"
"	image-position:right;\n"
"}")
        self.eliminate_list.setFrameShape(QFrame.Shape.StyledPanel)
        self.eliminate_list.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.eliminate_list)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.total_eliminate_label = QLabel(self.eliminate_list)
        self.total_eliminate_label.setObjectName(u"total_eliminate_label")
        self.total_eliminate_label.setFont(font8)
        self.total_eliminate_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.total_eliminate_label.setWordWrap(False)
        self.total_eliminate_label.setMargin(0)

        self.verticalLayout_21.addWidget(self.total_eliminate_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.label_38 = QLabel(self.eliminate_list)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font4)

        self.verticalLayout_21.addWidget(self.label_38, 0, Qt.AlignmentFlag.AlignLeft)

        self.show_more_eliminate_btn = QToolButton(self.eliminate_list)
        self.show_more_eliminate_btn.setObjectName(u"show_more_eliminate_btn")
        sizePolicy4.setHeightForWidth(self.show_more_eliminate_btn.sizePolicy().hasHeightForWidth())
        self.show_more_eliminate_btn.setSizePolicy(sizePolicy4)
        self.show_more_eliminate_btn.setMinimumSize(QSize(150, 0))
        self.show_more_eliminate_btn.setMaximumSize(QSize(215, 25))
        self.show_more_eliminate_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_more_eliminate_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.show_more_eliminate_btn.setStyleSheet(u"#show_more_eliminate_btn{\n"
"	background-color: rgb(61, 46, 46);\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	color: rgb(131, 117, 117);\n"
"	padding: 0  5px  0  5px;\n"
"}\n"
"#show_more_eliminate_btn:hover{\n"
"	background-color: rgb(56, 42, 42);\n"
"}")
        self.show_more_eliminate_btn.setIcon(icon15)
        self.show_more_eliminate_btn.setIconSize(QSize(20, 20))
        self.show_more_eliminate_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_21.addWidget(self.show_more_eliminate_btn)


        self.horizontalLayout_9.addWidget(self.eliminate_list)


        self.verticalLayout_23.addLayout(self.horizontalLayout_9)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.verticalLayout_22.addWidget(self.student_card)

        self.matplotlib_chart = QFrame(self.Dashboard_0)
        self.matplotlib_chart.setObjectName(u"matplotlib_chart")
        sizePolicy2.setHeightForWidth(self.matplotlib_chart.sizePolicy().hasHeightForWidth())
        self.matplotlib_chart.setSizePolicy(sizePolicy2)
        self.matplotlib_chart.setStyleSheet(u"background-color: rgb(35, 30, 80);")
        self.matplotlib_chart.setFrameShape(QFrame.Shape.StyledPanel)
        self.matplotlib_chart.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.matplotlib_chart)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.students_piechart = QChartView(self.matplotlib_chart)
        self.students_piechart.setObjectName(u"students_piechart")
        self.students_piechart.setStyleSheet(u"background-color: rgb(57, 50, 131);")

        self.horizontalLayout_12.addWidget(self.students_piechart)

        self.students_barchart = QChartView(self.matplotlib_chart)
        self.students_barchart.setObjectName(u"students_barchart")
        self.students_barchart.setStyleSheet(u"background-color: rgb(57, 50, 131);")

        self.horizontalLayout_12.addWidget(self.students_barchart)


        self.verticalLayout_22.addWidget(self.matplotlib_chart)

        self.stackedWidget.addWidget(self.Dashboard_0)
        self.Institution_1 = QWidget()
        self.Institution_1.setObjectName(u"Institution_1")
        self.label_13 = QLabel(self.Institution_1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(160, 50, 141, 31))
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        self.label_13.setFont(font9)
        self.stackedWidget.addWidget(self.Institution_1)
        self.StudentInfo_2 = QWidget()
        self.StudentInfo_2.setObjectName(u"StudentInfo_2")
        self.verticalLayout_16 = QVBoxLayout(self.StudentInfo_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.top_container = QWidget(self.StudentInfo_2)
        self.top_container.setObjectName(u"top_container")
        self.top_container.setMaximumSize(QSize(16777215, 150))
        self.top_container.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.top_container)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_3 = QFrame(self.top_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 191, 19))
        self.label_9.setFont(font7)
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 20, 211, 16))
        self.add_student_btn = QToolButton(self.frame_3)
        self.add_student_btn.setObjectName(u"add_student_btn")
        self.add_student_btn.setGeometry(QRect(10, 50, 141, 81))
        font10 = QFont()
        font10.setBold(False)
        self.add_student_btn.setFont(font10)
        self.add_student_btn.setStyleSheet(u"QToolButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.138889, y1:0.136, x2:1, y2:1, stop:0 rgba(42, 213, 65, 255), stop:1 rgba(0, 158, 88, 255));\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"	padding:10px 0 10px 0;\n"
"}\n"
"QToolButton::hover{\n"
"	background-color: rgb(2, 105, 31);\n"
"}\n"
"QToolButton::pressed{\n"
"	background-color: rgb(65, 57, 156);\n"
"}")
        icon16 = QIcon(QIcon.fromTheme(u"contact-new"))
        self.add_student_btn.setIcon(icon16)
        self.add_student_btn.setIconSize(QSize(28, 28))
        self.add_student_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.add_student_btn.setAutoRaise(False)
        self.to_excel_btn = QToolButton(self.frame_3)
        self.to_excel_btn.setObjectName(u"to_excel_btn")
        self.to_excel_btn.setGeometry(QRect(160, 50, 101, 81))
        self.to_excel_btn.setStyleSheet(u"QToolButton {\n"
"	background-color:rgb(13, 146, 244);\n"
"	border-radius:5px;\n"
"	padding:10px 0 10px 0;\n"
"}\n"
"QToolButton::hover{\n"
"	background-color: rgb(3, 92, 158);\n"
"}\n"
"QToolButton::pressed{\n"
"	background-color: rgb(65, 57, 156);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/png/icons/_excel-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_excel_btn.setIcon(icon17)
        self.to_excel_btn.setIconSize(QSize(28, 28))
        self.to_excel_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.to_excel_btn.setAutoRaise(False)
        self.to_pdf_btn = QToolButton(self.frame_3)
        self.to_pdf_btn.setObjectName(u"to_pdf_btn")
        self.to_pdf_btn.setGeometry(QRect(270, 50, 101, 81))
        self.to_pdf_btn.setStyleSheet(u"QToolButton {\n"
"	background-color: rgb(196, 12, 12);\n"
"	border-radius:5px;\n"
"	padding:10px 0 10px 0;\n"
"}\n"
"QToolButton::hover{\n"
"	background-color: rgb(186, 34, 34);\n"
"}\n"
"QToolButton::pressed{\n"
"	background-color: rgb(65, 57, 156);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/png/icons/_pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.to_pdf_btn.setIcon(icon18)
        self.to_pdf_btn.setIconSize(QSize(28, 28))
        self.to_pdf_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.to_pdf_btn.setAutoRaise(False)

        self.horizontalLayout_11.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.top_container)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(252, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.card_id = QWidget(self.frame_4)
        self.card_id.setObjectName(u"card_id")
        self.card_id.setGeometry(QRect(0, 0, 251, 131))
        self.card_id.setStyleSheet(u"#card_id{\n"
"	background-color: rgb(29, 26, 74);\n"
"	border-radius:15px;\n"
"	image: url(:/png/icons/_edit-info.png);\n"
"	image-position:left;\n"
"}\n"
"QLabel{\n"
"	text-transform: uppercase;\n"
"}")
        self.id_label = QLabel(self.card_id)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(180, 10, 63, 72))
        font11 = QFont()
        font11.setFamilies([u"Segoe MDL2 Assets"])
        self.id_label.setFont(font11)
        self.id_label.setStyleSheet(u"#id_label{\n"
"	border:1px solid rgb(48, 76, 143);\n"
"	border-radius:5px;\n"
"	background-color: rgb(36, 33, 93);\n"
"}")
        self.id_label.setPixmap(QPixmap(u":/png/icons/anyrgb.com.png"))
        self.id_label.setScaledContents(True)
        self.id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_name_label = QLabel(self.card_id)
        self.first_name_label.setObjectName(u"first_name_label")
        self.first_name_label.setGeometry(QRect(60, 14, 111, 21))
        self.first_name_label.setFont(font6)
        self.first_name_label.setStyleSheet(u"text-transform: uppercase;")
        self.first_name_label.setPixmap(QPixmap(u":/png/icons/line.png"))
        self.last_name_label = QLabel(self.card_id)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setGeometry(QRect(82, 43, 91, 16))
        self.last_name_label.setFont(font6)
        self.last_name_label.setPixmap(QPixmap(u":/png/icons/line.png"))
        self.age_label = QLabel(self.card_id)
        self.age_label.setObjectName(u"age_label")
        self.age_label.setGeometry(QRect(50, 66, 31, 21))
        self.age_label.setFont(font7)
        self.age_label.setPixmap(QPixmap(u":/png/icons/line.png"))
        self.frame = QFrame(self.card_id)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 250, 31))
        self.frame.setStyleSheet(u"background-color: rgb(20, 18, 52);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(194, 0, 49, 31))
        self.label_33.setPixmap(QPixmap(u":/png/icons/product-code.png"))
        self.label_33.setScaledContents(True)
        self.year_label = QLabel(self.card_id)
        self.year_label.setObjectName(u"year_label")
        self.year_label.setGeometry(QRect(10, 65, 41, 16))
        self.year_label.setFont(font)
        self.year_label.setStyleSheet(u"color: rgb(66, 61, 170);")
        self.year_label_2 = QLabel(self.card_id)
        self.year_label_2.setObjectName(u"year_label_2")
        self.year_label_2.setGeometry(QRect(10, 40, 71, 16))
        self.year_label_2.setFont(font)
        self.year_label_2.setStyleSheet(u"color: rgb(66, 61, 170);")
        self.year_label_3 = QLabel(self.card_id)
        self.year_label_3.setObjectName(u"year_label_3")
        self.year_label_3.setGeometry(QRect(10, 14, 51, 16))
        self.year_label_3.setFont(font)
        self.year_label_3.setStyleSheet(u"color: rgb(66, 61, 170);")

        self.horizontalLayout_11.addWidget(self.frame_4)


        self.verticalLayout_16.addWidget(self.top_container)

        self.frame_2 = QFrame(self.StudentInfo_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color: rgb(23, 21, 59);\n"
"border-radius:5px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.filter_gender_comboBox = QComboBox(self.frame_2)
        icon19 = QIcon()
        icon19.addFile(u":/png/icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filter_gender_comboBox.addItem(icon19, "")
        self.filter_gender_comboBox.addItem("")
        self.filter_gender_comboBox.addItem("")
        self.filter_gender_comboBox.setObjectName(u"filter_gender_comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.filter_gender_comboBox.sizePolicy().hasHeightForWidth())
        self.filter_gender_comboBox.setSizePolicy(sizePolicy5)
        self.filter_gender_comboBox.setMaximumSize(QSize(170, 16777215))
        self.filter_gender_comboBox.setFont(font3)
        self.filter_gender_comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(37, 30, 84);\n"
"	color: rgb(134, 136, 223);\n"
"	border: 1px solid rgb(44, 38, 100);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
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
"margin-top:3px;\n"
"border-radius: 5px;\n"
"}\n"
"QComboBox::down-arrow { 	\n"
"	image: url(:/png/icons/arrow-down.png);\n"
"	width:25px;\n"
"	height:25"
                        "px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.filter_gender_comboBox)

        self.filter_class_comboBox = QComboBox(self.frame_2)
        self.filter_class_comboBox.addItem(icon19, "")
        self.filter_class_comboBox.addItem("")
        self.filter_class_comboBox.addItem("")
        self.filter_class_comboBox.addItem("")
        self.filter_class_comboBox.addItem("")
        self.filter_class_comboBox.setObjectName(u"filter_class_comboBox")
        sizePolicy5.setHeightForWidth(self.filter_class_comboBox.sizePolicy().hasHeightForWidth())
        self.filter_class_comboBox.setSizePolicy(sizePolicy5)
        self.filter_class_comboBox.setMaximumSize(QSize(170, 16777215))
        self.filter_class_comboBox.setFont(font3)
        self.filter_class_comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(37, 30, 84);\n"
"	color: rgb(134, 136, 223);\n"
"	border: 1px solid rgb(44, 38, 100);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
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
"margin-top:3px;\n"
"border-radius: 5px;\n"
"}\n"
"QComboBox::down-arrow { 	\n"
"	image: url(:/png/icons/arrow-down.png);\n"
"	width:25px;\n"
"	height:25"
                        "px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.filter_class_comboBox)

        self.horizontalSpacer_3 = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.searchBox = QLineEdit(self.frame_2)
        self.searchBox.setObjectName(u"searchBox")
        sizePolicy4.setHeightForWidth(self.searchBox.sizePolicy().hasHeightForWidth())
        self.searchBox.setSizePolicy(sizePolicy4)
        self.searchBox.setMaximumSize(QSize(200, 16777215))
        self.searchBox.setFont(font3)
        self.searchBox.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.searchBox)


        self.verticalLayout_16.addWidget(self.frame_2)

        self.students_table = QTableWidget(self.StudentInfo_2)
        if (self.students_table.columnCount() < 12):
            self.students_table.setColumnCount(12)
        font12 = QFont()
        font12.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font12);
        self.students_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font12);
        self.students_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font12);
        self.students_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font12);
        self.students_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font12);
        self.students_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font12);
        self.students_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font12);
        self.students_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font12);
        self.students_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font12);
        self.students_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font12);
        self.students_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font12);
        self.students_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font12);
        self.students_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.students_table.rowCount() < 7):
            self.students_table.setRowCount(7)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.students_table.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.students_table.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.students_table.setVerticalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.students_table.setVerticalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.students_table.setVerticalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.students_table.setVerticalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.students_table.setVerticalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.students_table.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.students_table.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.students_table.setItem(0, 2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.students_table.setItem(0, 3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.students_table.setItem(1, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.students_table.setItem(1, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.students_table.setItem(1, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.students_table.setItem(2, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.students_table.setItem(2, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.students_table.setItem(2, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.students_table.setItem(3, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.students_table.setItem(3, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.students_table.setItem(3, 2, __qtablewidgetitem31)
        self.students_table.setObjectName(u"students_table")
        sizePolicy3.setHeightForWidth(self.students_table.sizePolicy().hasHeightForWidth())
        self.students_table.setSizePolicy(sizePolicy3)
        self.students_table.setStyleSheet(u"")
        self.students_table.setFrameShape(QFrame.Shape.NoFrame)
        self.students_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.students_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.students_table.setTabKeyNavigation(True)
        self.students_table.setProperty(u"showDropIndicator", True)
        self.students_table.setAlternatingRowColors(True)
        self.students_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.students_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.students_table.setCornerButtonEnabled(False)
        self.students_table.horizontalHeader().setVisible(True)
        self.students_table.horizontalHeader().setCascadingSectionResizes(False)
        self.students_table.horizontalHeader().setHighlightSections(True)
        self.students_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.students_table.horizontalHeader().setStretchLastSection(False)
        self.students_table.verticalHeader().setVisible(False)

        self.verticalLayout_16.addWidget(self.students_table)

        self.stackedWidget.addWidget(self.StudentInfo_2)
        self.StudentPay_3 = QWidget()
        self.StudentPay_3.setObjectName(u"StudentPay_3")
        self.label_14 = QLabel(self.StudentPay_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(320, 210, 231, 31))
        self.label_14.setFont(font9)
        self.stackedWidget.addWidget(self.StudentPay_3)
        self.StudentTrans_4 = QWidget()
        self.StudentTrans_4.setObjectName(u"StudentTrans_4")
        self.label_15 = QLabel(self.StudentTrans_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(320, 210, 271, 31))
        self.label_15.setFont(font9)
        self.stackedWidget.addWidget(self.StudentTrans_4)
        self.TeacherInfo_5 = QWidget()
        self.TeacherInfo_5.setObjectName(u"TeacherInfo_5")
        self.label_16 = QLabel(self.TeacherInfo_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(320, 210, 271, 31))
        self.label_16.setFont(font9)
        self.stackedWidget.addWidget(self.TeacherInfo_5)
        self.TeacherSalar_6 = QWidget()
        self.TeacherSalar_6.setObjectName(u"TeacherSalar_6")
        self.label_17 = QLabel(self.TeacherSalar_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(320, 210, 211, 31))
        self.label_17.setFont(font9)
        self.stackedWidget.addWidget(self.TeacherSalar_6)
        self.TeacherTrans_7 = QWidget()
        self.TeacherTrans_7.setObjectName(u"TeacherTrans_7")
        self.label_18 = QLabel(self.TeacherTrans_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(320, 210, 271, 31))
        self.label_18.setFont(font9)
        self.stackedWidget.addWidget(self.TeacherTrans_7)
        self.Budgets_8 = QWidget()
        self.Budgets_8.setObjectName(u"Budgets_8")
        self.label_19 = QLabel(self.Budgets_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(320, 210, 111, 31))
        self.label_19.setFont(font9)
        self.stackedWidget.addWidget(self.Budgets_8)
        self.Expenses_9 = QWidget()
        self.Expenses_9.setObjectName(u"Expenses_9")
        self.label_20 = QLabel(self.Expenses_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(320, 210, 121, 31))
        self.label_20.setFont(font9)
        self.stackedWidget.addWidget(self.Expenses_9)
        self.BusinessOver_10 = QWidget()
        self.BusinessOver_10.setObjectName(u"BusinessOver_10")
        self.label_21 = QLabel(self.BusinessOver_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(320, 210, 241, 31))
        self.label_21.setFont(font9)
        self.stackedWidget.addWidget(self.BusinessOver_10)
        self.Fee_11 = QWidget()
        self.Fee_11.setObjectName(u"Fee_11")
        self.label_22 = QLabel(self.Fee_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(320, 210, 71, 31))
        self.label_22.setFont(font9)
        self.stackedWidget.addWidget(self.Fee_11)
        self.Settings_12 = QWidget()
        self.Settings_12.setObjectName(u"Settings_12")
        self.label_23 = QLabel(self.Settings_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(320, 210, 111, 31))
        self.label_23.setFont(font9)
        self.stackedWidget.addWidget(self.Settings_12)
        self.Help_13 = QWidget()
        self.Help_13.setObjectName(u"Help_13")
        self.label_24 = QLabel(self.Help_13)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(410, 80, 61, 31))
        self.label_24.setFont(font9)
        self.label_11 = QLabel(self.Help_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(310, 260, 71, 16))
        self.label_11.setFont(font2)
        self.label_25 = QLabel(self.Help_13)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(400, 230, 61, 61))
        self.label_25.setPixmap(QPixmap(u":/png/icons/laroussigsm.net.png"))
        self.label_25.setScaledContents(True)
        self.stackedWidget.addWidget(self.Help_13)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.body)

        self.widget_7 = QWidget(self.styles)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 20))
        self.widget_7.setStyleSheet(u"background-color: rgb(35, 30, 80);\n"
"color: rgb(85, 75, 197);")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 0, 9, 0)
        self.label_34 = QLabel(self.widget_7)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_16.addWidget(self.label_34)

        self.label_35 = QLabel(self.widget_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_35)


        self.verticalLayout_2.addWidget(self.widget_7)


        self.horizontalLayout_15.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.styles)

        self.retranslateUi(MainWindow)
        self.manage_student2_btn.toggled.connect(self.subMenu1.setHidden)
        self.manage_teacher2_btn.toggled.connect(self.subMenu2.setHidden)
        self.manage_finances2_btn.toggled.connect(self.subMenu3.setHidden)
        self.dashboard2_btn.toggled.connect(self.dashboard_btn.setChecked)
        self.institution2_btn.toggled.connect(self.institution_btn.setChecked)
        self.manage_student2_btn.toggled.connect(self.manage_student_btn.setChecked)
        self.manage_teacher2_btn.toggled.connect(self.manage_teacher_btn.setChecked)
        self.manage_finances2_btn.toggled.connect(self.manage_finances_btn.setChecked)
        self.fee2_btn.toggled.connect(self.fee_btn.setChecked)
        self.settings2_btn.toggled.connect(self.settings_btn.setChecked)
        self.help2_btn.toggled.connect(self.help_btn.setChecked)
        self.toggle_btn.toggled.connect(self.expand_sidBar.setHidden)
        self.toggle_btn.toggled.connect(self.left_sideBar.setVisible)

        self.stackedWidget.setCurrentIndex(13)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Laroussi Pyside6 Coding Tutorial | https://laroussigsm.net/", None))
        self.minimize_btn.setText("")
        self.restore_btn.setText("")
        self.close_btn.setText("")
        self.label_3.setText("")
        self.dashboard_btn.setText("")
        self.institution_btn.setText("")
        self.manage_student_btn.setText("")
        self.manage_teacher_btn.setText("")
        self.manage_finances_btn.setText("")
        self.fee_btn.setText("")
        self.settings_btn.setText("")
        self.help_btn.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"System Manager", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pyside Coding Project", None))
        self.dashboard2_btn.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.institution2_btn.setText(QCoreApplication.translate("MainWindow", u" Institution", None))
        self.manage_student2_btn.setText(QCoreApplication.translate("MainWindow", u" Manage Student's", None))
        self.student_info_btn.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_pay_btn.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.student_trans_btn.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.manage_teacher2_btn.setText(QCoreApplication.translate("MainWindow", u" Manage Teacher's", None))
        self.teacher_info_btn.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teacher_salar_btn.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teacher_trans_btn.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.manage_finances2_btn.setText(QCoreApplication.translate("MainWindow", u" Manage Finances", None))
        self.budgets_btn.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses_btn.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.business_over_btn.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.fee2_btn.setText(QCoreApplication.translate("MainWindow", u" Fee's", None))
        self.settings2_btn.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.help2_btn.setText(QCoreApplication.translate("MainWindow", u"  Help", None))
        self.toggle_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hello, Laroussi !", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"How are you doing today?", None))
#if QT_CONFIG(tooltip)
        self.logout_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.logout_btn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u" LOGOUT", None))
        self.avatar.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.total_student_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Total Student's", None))
        self.show_more_students_btn.setText(QCoreApplication.translate("MainWindow", u"   Show More", None))
        self.total_male_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Total Male's", None))
        self.show_more_male_btn.setText(QCoreApplication.translate("MainWindow", u"   Show More", None))
        self.total_female_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Total Female's", None))
        self.show_more_female_btn.setText(QCoreApplication.translate("MainWindow", u"   Show More", None))
        self.total_marks_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Students Marks", None))
        self.show_more_marks_btn.setText(QCoreApplication.translate("MainWindow", u"   Show More", None))
#if QT_CONFIG(tooltip)
        self.total_eliminate_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.total_eliminate_label.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.total_eliminate_label.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Elimination", None))
        self.show_more_eliminate_btn.setText(QCoreApplication.translate("MainWindow", u"   Show More", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Welcome to Student Information Page", None))
        self.add_student_btn.setText(QCoreApplication.translate("MainWindow", u" Add New Student", None))
        self.to_excel_btn.setText(QCoreApplication.translate("MainWindow", u" Export To Excel", None))
        self.to_pdf_btn.setText(QCoreApplication.translate("MainWindow", u" Export To PDF", None))
        self.id_label.setText("")
        self.first_name_label.setText("")
        self.last_name_label.setText("")
        self.age_label.setText("")
        self.label_33.setText("")
        self.year_label.setText(QCoreApplication.translate("MainWindow", u"age :", None))
        self.year_label_2.setText(QCoreApplication.translate("MainWindow", u"surname :", None))
        self.year_label_3.setText(QCoreApplication.translate("MainWindow", u"name :", None))
        self.filter_gender_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Filter by gender", None))
        self.filter_gender_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.filter_gender_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.filter_class_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Filter by class", None))
        self.filter_class_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 01", None))
        self.filter_class_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 02", None))
        self.filter_class_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 03", None))
        self.filter_class_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 04", None))

        self.searchBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search ...", None))
        ___qtablewidgetitem = self.students_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.students_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u" First Name", None));
        ___qtablewidgetitem2 = self.students_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem3 = self.students_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None));
        ___qtablewidgetitem4 = self.students_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem5 = self.students_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem6 = self.students_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem7 = self.students_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone N\u00b0", None));
        ___qtablewidgetitem8 = self.students_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem9 = self.students_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem10 = self.students_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem11 = self.students_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        ___qtablewidgetitem12 = self.students_table.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.students_table.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.students_table.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.students_table.verticalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.students_table.verticalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.students_table.verticalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.students_table.verticalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.students_table.isSortingEnabled()
        self.students_table.setSortingEnabled(False)
        ___qtablewidgetitem19 = self.students_table.item(0, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"jkhjkhjkhj", None));
        ___qtablewidgetitem20 = self.students_table.item(0, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u",bn,bn,bn,", None));
        ___qtablewidgetitem21 = self.students_table.item(0, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"bn,bn,bn,", None));
        ___qtablewidgetitem22 = self.students_table.item(0, 3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"bn,bn,bn,bn,", None));
        ___qtablewidgetitem23 = self.students_table.item(1, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u":jklmjkmljk", None));
        ___qtablewidgetitem24 = self.students_table.item(1, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"mjkmjkm", None));
        ___qtablewidgetitem25 = self.students_table.item(1, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"jkmjkmjk", None));
        ___qtablewidgetitem26 = self.students_table.item(2, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"kjkmjkm", None));
        ___qtablewidgetitem27 = self.students_table.item(2, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"kkjmjkmjk", None));
        ___qtablewidgetitem28 = self.students_table.item(2, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"jkmjkmj", None));
        ___qtablewidgetitem29 = self.students_table.item(3, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"jkmjkm", None));
        ___qtablewidgetitem30 = self.students_table.item(3, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"jkmjkm", None));
        ___qtablewidgetitem31 = self.students_table.item(3, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"jkmjkm", None));
        self.students_table.setSortingEnabled(__sortingEnabled)

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fee's", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"QR-URL: ", None))
        self.label_25.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"By : Laroussi Boulanouar", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"V1.0.0", None))
    # retranslateUi

