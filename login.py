import os
import sys
import json
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from ui.ui_login_gui import Ui_login_gui
from utils.qstackedwidget_utils import *
from utils.qdialog_utils import *
from database.database_connection import get_database_connection
from pymysql.err import MySQLError

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_login_gui()  # Use Ui_login
        self.ui.setupUi(self)

        # Connect button clicks to close dialog
        self.ui.close_btn.clicked.connect(self.close)

        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Set Custom Navigation Bar
        self.ui.widget.mouseMoveEvent = self.MoveWindow

        # Assing Current Index StackedWidget
        self.ui.stackedWidget.setCurrentIndex(0)

        # Store the default window geometry (size and position)
        self.default_geometry = self.geometry()

        # Connect the button's clicked
        self.ui.login_btn.clicked.connect(self.login_page)
        self.ui.register_btn.clicked.connect(self.registration_page)
        self.ui.reset_pass_btn.clicked.connect(self.forget_page)
        self.ui.show_pass_btn.clicked.connect(self.toggle_password)
        self.ui.hide_pass_btn.clicked.connect(self.toggle_password)

        # Connect button clicks to the respective methods with animations
        self.ui.to_register.clicked.connect(lambda: self.switch_to_page(1, "slide"))  # Register page
        self.ui.to_login.clicked.connect(lambda: self.switch_to_page(0, "slide"))  # Login page
        self.ui.to_forget_pass.clicked.connect(lambda: self.switch_to_page(2, "slide"))  # Forget page
        self.ui.back_to_login.clicked.connect(lambda: self.switch_to_page(0, "slide")) # Back to Login page


        # Initially, hide the "Hide" button
        self.ui.show_pass_btn.hide()

        # Load credentials if available
        self.load_credentials()

    def switch_to_page(self, index, animation_type="slide", direction="right"):
        """
        Switches the QStackedWidget to the given page index with animation.

        :param index: Index of the page to switch to
        :param animation_type: Type of animation to use (slide, fade, bounce, zoom, rotate, scale_fade, swipe)
        :param direction: The direction for slide animations (right, left, top, bottom)
        """
        if animation_type == "slide":
            switch_to_slide_page(self.ui.stackedWidget, index, direction)
        elif animation_type == "fade":
            switch_to_fade_page(self.ui.stackedWidget, index)
        elif animation_type == "bounce":
            switch_to_bounce_page(self.ui.stackedWidget, index)
        elif animation_type == "zoom":
            switch_to_zoom_page(self.ui.stackedWidget, index)
        elif animation_type == "scale_fade":
            switch_to_scale_fade_page(self.ui.stackedWidget, index)
        elif animation_type == "swipe":
            switch_to_swipe_page(self.ui.stackedWidget, index)


    # Methods to Move Window
    def MoveWindow(self, event):
        if not self.isMaximized():
            self.move(
                self.pos() + event.globalPosition().toPoint()
                - self.clickPosition
                )
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    # Call the Position of the window To Center
    def showEvent(self, event):
        super().showEvent(event)
        self.centerWindow()

    def centerWindow(self):
        screen = QApplication.primaryScreen()
        if screen is not None:
            # Get available screen geometry (excluding taskbar)
            screen_geometry = screen.availableGeometry()
            # Calculate center position considering taskbar height
            x = (screen_geometry.width() - self.width()) / 2
            y = (screen_geometry.height() - self.height()) / 2
            # Set the position of the window
            self.move(x, y)

    # Initially, Show the password & Hide the password
    def toggle_password(self):
        if self.ui.pass_lineEdit.echoMode() == QLineEdit.Normal:
            # Show the password (set QLineEdit to Normal mode)
            self.ui.pass_lineEdit.setEchoMode(QLineEdit.Password)
            self.ui.show_pass_btn.hide()
            self.ui.hide_pass_btn.show()
        else:
            # Hide the password (set QLineEdit to Password mode)
            self.ui.pass_lineEdit.setEchoMode(QLineEdit.Normal)
            self.ui.show_pass_btn.show()
            self.ui.hide_pass_btn.hide()

    def load_credentials(self):
        try:
            # Construct the path to credentials.json inside the Json/ directory
            json_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'Json')
            credentials_path = os.path.join(json_dir, 'credentials.json')

            with open(credentials_path, "r") as file:
                credentials = json.load(file)
                self.ui.user_lineEdit.setText(credentials.get("username", ""))
                self.ui.pass_lineEdit.setText(credentials.get("password", ""))
                self.ui.remember_me.setChecked(
                    credentials.get("remember_me", False)
                )
        except FileNotFoundError:
            pass

    def save_credentials(self, username, password, remember_me):
        credentials = {
            "username": username if remember_me else "",
            "password": password if remember_me else "",
            "remember_me": remember_me
        }

        # Construct the path to credentials.json inside the Json/ directory
        json_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'Json'
            )
        credentials_path = os.path.join(json_dir, 'credentials.json')

        with open(credentials_path, "w") as file:
            json.dump(credentials, file)

    # Function to Open main Project Window
    def open_main_project(self):
        import main  # Import main_project module
        self.main_window = main.MainProject()
        self.main_window.show()
        self.close()

    # Connect Database MySQL
    def login_page(self):
        user_name = self.ui.user_lineEdit.text().strip()
        pass_word = self.ui.pass_lineEdit.text().strip()
        remember_me = self.ui.remember_me.isChecked()

        if not all([user_name, pass_word]):
            show_message('Fields should not be empty!', 'warning', parent=self)
            return

        # Database connection
        db, cursor = get_database_connection()
        if not db or not cursor:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return

        try:
            cursor.execute(
                "SELECT * FROM registration WHERE username = %s AND password = %s",
                (user_name, pass_word)
            )
            result = cursor.fetchone()

            if result:
                show_message('System login successfully !!', 'success', parent=self)
                self.save_credentials(user_name, pass_word, remember_me)
                QTimer.singleShot(3000, self.open_main_project)
            else:
                show_message('Invalid username or password!', 'error', parent=self)
        except MySQLError as e:
            show_message(f'Database error: {e}', 'error', parent=self)
        finally:
            cursor.close()
            db.close()

    def registration_page(self):
        add_username = self.ui.add_user_lineEdit.text().strip()
        add_password = self.ui.add_pass_lineEdit.text().strip()
        add_confirm_password = self.ui.confirm_pass_lineEdit.text().strip()
        add_email = self.ui.add_mail_lineEdit.text().strip()

        if not all([add_username, add_password, add_confirm_password, add_email]):
            show_message('Fields should not be empty!', 'warning')
            return
        if add_password != add_confirm_password:
            show_message('Passwords do not match!', 'warning')
            return

        # Database connection
        db, cursor = get_database_connection()
        if not db or not cursor:
            show_message('Database connection failed!', 'error')
            return

        try:
            cursor.execute(
                "SELECT * FROM registration WHERE username = %s",
                (add_username,)
            )
            result = cursor.fetchone()
            
            if result:
                show_message('User already registered!', 'warning')
            else:
                cursor.execute(
                    "INSERT INTO registration (username, password, email) VALUES (%s, %s, %s)",
                    (add_username, add_password, add_email)
                )
                db.commit()
                show_message('Registration successful!', 'success')
                QTimer.singleShot(2000, lambda: self.switch_to_page(0, "slide"))
        except MySQLError as e:
            show_message(f'Database error: {e}', 'error')
        finally:
            cursor.close()
            db.close()

    def forget_page(self):
        reset_username = self.ui.reset_user_lineEdit.text().strip()
        reset_email = self.ui.reset_mail_lineEdit.text().strip()
        reset_password = self.ui.reset_pass_lineEdit.text().strip()
        confirm_reset_password = self.ui.comfirm_reset_pass.text().strip()

        if not all([reset_username, reset_email, reset_password, confirm_reset_password]):
            show_message('Fields should not be empty!', 'warning')
            return
        if reset_password != confirm_reset_password:
            show_message('Passwords do not match!', 'warning')
            return

        # Database connection
        db, cursor = get_database_connection()
        if not db or not cursor:
            show_message('Database connection failed!', 'error')
            return

        try:
            cursor.execute("SELECT * FROM registration WHERE email = %s", (reset_email,))
            row = cursor.fetchone()

            if row is None:
                show_message('This email does not exist!', 'error')
            else:
                cursor.execute(
                    "UPDATE registration SET username = %s, password = %s WHERE email = %s",
                    (reset_username, reset_password, reset_email)
                )
                db.commit()
                show_message('Password successfully updated!', 'success')
                QTimer.singleShot(2000, lambda: self.switch_to_page(0, "slide"))
        except MySQLError as e:
            show_message(f'Database error: {e}', 'error')
        finally:
            cursor.close()
            db.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    # Run loop the app
    app.exec()
