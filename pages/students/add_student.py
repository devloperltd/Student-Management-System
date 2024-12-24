import sys
from pymysql.err import MySQLError
from database.database_connection import get_database_connection
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QPixmap
from datetime import datetime
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from ui.ui_Addstudents_Dialog import Ui_Addstudents_Dialog
from utils.qdialog_utils import show_message


# Function to convert an image file to binary data
def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
        return binary_data

class AddStudent(QDialog):
    def __init__(self, parent=None):
        super(AddStudent, self).__init__(parent)
        self.ui = Ui_Addstudents_Dialog()  # Use Ui_MainWindow to set up the UI
        self.ui.setupUi(self)
        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Set Custom Navigation Bar
        self.ui.add_stud_nav.mouseMoveEvent = self.MoveWindow

        # Store the default window geometry (size and position)
        self.default_geometry = self.geometry()

        # Assing Button's
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.cancel_student_btn.clicked.connect(self.close)
        self.ui.minimize_btn.clicked.connect(self.showMinimized)

        self.ui.up_std_btn.clicked.connect(self.Add_Photo)
        self.ui.delete_std_btn.clicked.connect(self.Delete_Photo)

        self.ui.add_student_btn.clicked.connect(self.add_student)
        self.ui.clear_student_btn.clicked.connect(self.clear_all)

        self.selected_image_path = None

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

    # Add Photo with filter parameter in QLabel
    def Add_Photo(self):
        # Set the file filter to allow only png, jpg, jpeg, and bmp files
        file_filter = "Images (*.png *.jpg *.jpeg *.bmp)"

        # Use the filter in QFileDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Select Photo", "", file_filter)

        if filename:  # Check if a file was selected
            # Create a QPixmap from the selected image file
            pixmap = QPixmap(filename)

            # Set the QPixmap as the image for the QLabel
            self.ui.photo_label.setPixmap(pixmap)

            # Optionally, resize the QLabel to fit the image
            self.ui.photo_label.setScaledContents(True)

            # Store the file path for later conversion to binary
            self.selected_image_path = filename
        else:
            self.selected_image_path = None

    # Delete Photo from QLabel
    def Delete_Photo(self):
        self.ui.photo_label.clear()
        self.selected_image_path = None

    # Calculate age by defference in years
    def calculate_age(self, birth_date):
        # Close birthday is a QDate object
        current_date = datetime.now().date()

        # Crete date object for the birthdate
        birth_datetime = datetime(birth_date.year(),
                                  birth_date.month(),
                                  birth_date.day()).date()
        # calculate the defference in years
        age = current_date.year - birth_datetime.year

        # Check if the birthday has occurred this year
        if (current_date.month,
            current_date.day) < (birth_datetime.month,
                                 birth_datetime.day):
            age -= 1
        return age

    # Add new student in Mysql database
    def add_student(self):
        firstname = self.ui.first_name_lineEdit.text()
        lastname = self.ui.last_name_lineEdit.text()
        birthdate = self.ui.birth_dateEdit.date()
        age = self.calculate_age(birthdate)
        gender = self.ui.gender_comboBox.currentText()
        classroom = self.ui.class_comboBox.currentText()              
        phone = self.ui.phone_lineEdit.text()
        email = self.ui.email_lineEdit.text()
        homeaddress = self.ui.address_lineEdit.text()
        city = self.ui.city_lineEdit.text()

        # Convert QDate to string in 'YYYY-MM-DD' format for MySQL
        birthdate_str = birthdate.toString("yyyy-MM-dd")

        # Convert the selected image to binary data if a photo is selected
        photo_id = convertToBinary(self.selected_image_path) if self.selected_image_path else None

        # Get database connection
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return

        try:
            # Check if student already exists
            cursor.execute(
                "SELECT * FROM add_students WHERE first_name = %s AND last_name = %s AND email = %s",
                (firstname, lastname, email)
            )
            result = cursor.fetchone()
            
            if result:
                show_message('User is already registered, try to login', 'warning', parent=self)
            elif not all([firstname, lastname, email, birthdate_str, gender, classroom, phone, homeaddress, city, photo_id]):
                show_message('Field should not be empty !!!', 'warning', parent=self)
            else:
                # Insert new student
                cursor.execute(
                    """INSERT INTO add_students (first_name, last_name, date_birth, age, gender, class, phone, email, address, city, photo_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (firstname, lastname, birthdate_str, age, gender, classroom, phone, email, homeaddress, city, photo_id)
                )
                db.commit()
                show_message('Registration Successfully !!!', 'success', parent=self)
                # Close Add student's Dialog
                self.close()

        except MySQLError as e:
            show_message(f"Database error: {e}", 'error', parent=self)
            print(f"Error: {e}")
        finally:
            # Ensure cursor and connection are closed properly
            if cursor:
                cursor.close()
            if db:
                db.close()

    def clear_all(self):
        self.ui.first_name_lineEdit.clear()
        self.ui.last_name_lineEdit.clear()
        # Reset date field to current date or a default value
        self.ui.birth_dateEdit.setDate(QDate.currentDate())
        # Reset combo boxes to default (usually index 0)
        self.ui.gender_comboBox.setCurrentIndex(0)
        self.ui.class_comboBox.setCurrentIndex(0)
        self.ui.phone_lineEdit.clear()
        self.ui.email_lineEdit.clear()
        self.ui.address_lineEdit.clear()
        self.ui.city_lineEdit.clear()
        # Clear the photo or reset it
        self.ui.photo_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AddStudent()
    win.show()
    # Run loop the app
    app.exec()