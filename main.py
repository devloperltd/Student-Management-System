import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from ui.ui_main_gui import Ui_MainWindow
from pages.students import student_information
from utils.qdialog_utils import *
from pages import dashboard

class MainProject(QMainWindow):
    def __init__(self):
        super(MainProject, self).__init__()
        self.ui = Ui_MainWindow()  # Use Ui_MainWindow to set up the UI
        self.ui.setupUi(self)

        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Store the default window geometry (size & position)
        self.default_geometry = self.geometry()

        # Maximize window by default
        self.setWindowState(Qt.WindowMaximized)

        # Initialize ManageStudent with reference to the UI
        self.student_info = student_information.StudentInfo(self.ui, self)
        self.dashboard_content = dashboard.dashboard_page(self.ui, self)

        # Set initial For Dropdwon QPushButton
        # Set the initial state as checked
        self.ui.manage_student2_btn.setChecked(True)
        self.ui.manage_teacher2_btn.setChecked(True)
        self.ui.manage_finances2_btn.setChecked(True)

        # Set initial visibility and state of the sidebars
        self.ui.expand_sidBar.setHidden(False)
        self.ui.left_sideBar.setHidden(True)

        # Hide Sub Menu QWidget
        self.ui.subMenu1.setHidden(True)
        self.ui.subMenu2.setHidden(True)
        self.ui.subMenu3.setHidden(True)

        self.ui.stackedWidget.setCurrentIndex(0)

        # Assing Button's
        self.ui.close_btn.clicked.connect(self.confirm_close)
        self.ui.logout_btn.clicked.connect(self.open_login_project)
        self.ui.minimize_btn.clicked.connect(self.showMinimized)

        self.ui.dashboard_btn.clicked.connect(self.switch_to_dashboard_page)
        self.ui.dashboard2_btn.clicked.connect(self.switch_to_dashboard_page)
        self.ui.institution_btn.clicked.connect(self.switch_to_institution_page)
        self.ui.institution2_btn.clicked.connect(self.switch_to_institution_page)
        self.ui.student_info_btn.clicked.connect(self.switch_to_student_info_page)
        self.ui.student_pay_btn.clicked.connect(self.switch_to_student_pay_page)
        self.ui.student_trans_btn.clicked.connect(self.switch_to_student_trans_page)
        self.ui.teacher_info_btn.clicked.connect(self.switch_to_teacher_info_page)
        self.ui.teacher_salar_btn.clicked.connect(self.switch_to_teacher_salar_page)
        self.ui.teacher_trans_btn.clicked.connect(self.switch_to_teacher_trans_page)
        self.ui.budgets_btn.clicked.connect(self.switch_to_budgets_btn_page)
        self.ui.expenses_btn.clicked.connect(self.switch_to_expenses_btn_page)
        self.ui.business_over_btn.clicked.connect(self.switch_to_business_over_page)
        self.ui.fee_btn.clicked.connect(self.switch_to_fee_page)
        self.ui.fee2_btn.clicked.connect(self.switch_to_fee_page)
        self.ui.settings_btn.clicked.connect(self.switch_to_settings_page)
        self.ui.settings2_btn.clicked.connect(self.switch_to_settings_page)
        self.ui.help_btn.clicked.connect(self.switch_to_help_page)
        self.ui.help2_btn.clicked.connect(self.switch_to_help_page)

        # Connect other buttons for context menus
        self.ui.manage_student_btn.clicked.connect(self.student_context_menu)
        self.ui.manage_teacher_btn.clicked.connect(self.teacher_context_menu)
        self.ui.manage_finances_btn.clicked.connect(self.finances_context_menu)

        # Control column widths
        self.ui.students_table.setColumnWidth(0, 70)
        self.ui.students_table.setColumnWidth(1, 130)
        self.ui.students_table.setColumnWidth(2, 120)
        self.ui.students_table.setColumnWidth(3, 100)
        self.ui.students_table.setColumnWidth(4, 30)
        self.ui.students_table.setColumnWidth(5, 70)
        self.ui.students_table.setColumnWidth(6, 80)
        self.ui.students_table.setColumnWidth(7, 120)
        self.ui.students_table.setColumnWidth(8, 150)
        self.ui.students_table.setColumnWidth(9, 150)
        self.ui.students_table.setColumnWidth(10, 130)
        self.ui.students_table.setColumnWidth(11, 120)

    # Switch to a page in the custom QStackedWidget
    def switch_to_dashboard_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.dashboard_content.total_students()
        self.dashboard_content.total_male()
        self.dashboard_content.total_female()
        self.dashboard_content.show_donut_chart()
        self.dashboard_content.show_bar_chart()
        self.ui.students_piechart.update()
        self.ui.students_barchart.update()

    def switch_to_institution_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_student_info_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        # Reload the table with the new filter applied
        self.student_info.reload_studentstable_data()

    def switch_to_student_pay_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def switch_to_student_trans_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def switch_to_teacher_info_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def switch_to_teacher_salar_page(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def switch_to_teacher_trans_page(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def switch_to_budgets_btn_page(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def switch_to_expenses_btn_page(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def switch_to_business_over_page(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def switch_to_fee_page(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    def switch_to_settings_page(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def switch_to_help_page(self):
        self.ui.stackedWidget.setCurrentIndex(13)



    # Methods to show context menus
    def student_context_menu(self):
        self.show_custom_context_menu(self.ui.manage_student_btn,
                                      ["Student Information",
                                       "Student Payments",
                                       "Student Transactions"]
                                      )

    def teacher_context_menu(self):
        self.show_custom_context_menu(self.ui.manage_teacher_btn,
                                      ["Teacher Information",
                                       "Teacher Salaries",
                                       "Teacher Transactions"]
                                      )

    def finances_context_menu(self):
        self.show_custom_context_menu(self.ui.manage_finances_btn,
                                      ["Budgets",
                                       "Expenses",
                                       "Business Overview"]
                                      )

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)

        # Set style forthe menu
        menu.setStyleSheet("""
                           QMenu{
                           background-color: rgb(23, 21, 59);
                           color: rgb(203, 192, 247);
                           padding-top: 10px;
                           padding-bottom: 10px;
                           line-height: 1.5;
                           border-radius:5px;
                           }
                           QMenu:selected{
                           background-color: rgb(56, 49, 130);
                           color: rgb(198, 187, 241);
                           }
                           """)
        # Add action to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        # Show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()

        if text == "Student Information":
            self.switch_to_student_info_page()
        elif text == "Student Payments":
            self.switch_to_student_pay_page()
        elif text == "Student Transactions":
            self.switch_to_student_trans_page()

        if text == "Teacher Information":
            self.switch_to_teacher_info_page()
        elif text == "Teacher Salaries":
            self.switch_to_teacher_salar_page()
        elif text == "Teacher Transactions":
            self.switch_to_teacher_trans_page()

        if text == "Budgets":
            self.switch_to_budgets_btn_page()
        elif text == "Expenses":
            self.switch_to_expenses_btn_page()
        elif text == "Business Overview":
            self.switch_to_business_over_page()

    # Show Confirm Close Message Dialog
    def confirm_close(self):
        # Use the global show_confirm_close_dialog
        if animate_confirm_close_msg(self, self.close):
            print("Confirmed close.")

    # Methods to back to login window
    def open_login_project(self):
        import login # Import login_project module
        self.login_window = login.LoginWindow()
        self.login_window.show()
        self.close()  # Close the main project after showing the login window




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainProject()
    win.show()
    # Run loop the app
    app.exec()