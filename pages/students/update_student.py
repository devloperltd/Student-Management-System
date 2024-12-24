import sys
from database.database_connection import get_database_connection
from pymysql.err import MySQLError
from PySide6.QtCore import Qt, QDate, Signal
from PySide6.QtGui import QPixmap
from datetime import datetime
from utils.qdialog_utils import show_message
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from ui.ui_Updatestudents_Dialog import Ui_Updatestudents_Dialog


# Function to convert an image file to binary data
def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
        return binary_data

class UpdateStudent(QDialog):
    # Defined a custom Signal as a class Variable
    data_updated = Signal()    
    def __init__(self, row_number, row_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_Updatestudents_Dialog()  # Use Ui_MainWindow to set up the UI
        self.ui.setupUi(self)
        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Set Custom Navigation Bar
        self.ui.update_stud_nav.mouseMoveEvent = self.MoveWindow

        # Store the row number and row_data as an instance in variables
        self.row_number = row_number
        self.row_data = row_data

        # Fetch student data
        self.add_student = self.select_student()
        if not self.add_student:
            print("Student data not found.")
            return

        self.id_addstudent, self.first_name, self.last_name, self.birthdate, self.age, \
        self.gender, self.classroom, self.phone, self.email, self.address, \
        self.city, self.photo_id = self.add_student[0]

        # Set UI fields with fetched data
        self.ui.update_first_name_lineEdit.setText(str(self.first_name))
        self.ui.update_last_name_lineEdit.setText(str(self.last_name))

        # Convert birthdate to QDate and set in QDateEdit
        birthdate_qdate = QDate.fromString(str(self.birthdate), "yyyy-MM-dd")
        self.ui.update_birth_dateEdit.setDate(birthdate_qdate)

        self.ui.update_gender_comboBox.setCurrentText(str(self.gender))
        self.ui.update_class_comboBox.setCurrentText(str(self.classroom))
        self.ui.update_phone_lineEdit.setText(str(self.phone))
        self.ui.update_email_lineEdit.setText(str(self.email))
        self.ui.update_address_lineEdit.setText(str(self.address))
        self.ui.update_city_lineEdit.setText(str(self.city))

        # Load the student's photo using their ID
        # Load photo
        self.fetch_and_display_photo(self.id_addstudent)

        # Store the default window geometry (size and position)
        self.default_geometry = self.geometry()

        # Assing Button's
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        self.ui.update_cancel_btn.clicked.connect(self.close)

        self.ui.update_up_std_btn.clicked.connect(self.Add_Photo)
        self.ui.update_delete_std_btn.clicked.connect(self.Delete_Photo)

        self.ui.update_student_btn.clicked.connect(self.update_student)
        self.ui.update_clear_btn.clicked.connect(self.clear_all)

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
            self.ui.update_photo_label.setPixmap(pixmap)

            # Optionally, resize the QLabel to fit the image
            self.ui.update_photo_label.setScaledContents(True)

            # Store the file path for later conversion to binary
            self.selected_image_path = filename
        else:
            self.selected_image_path = None

    # Delete Photo from QLabel
    def Delete_Photo(self):
        self.ui.update_photo_label.clear()
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

    def select_student(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            print("Failed to connect to the database.")
            return  # Exit if the connection is unsuccessful
        try:
            student_id = self.row_data[0]
            student_name = self.row_data[1]
            params = [student_name, student_id]

            # Execute the SELECT query
            select_query = "SELECT * FROM add_students WHERE first_name = %s AND id_addstudent = %s"
            cursor.execute(select_query, params)
            record = cursor.fetchall()  # Fetch the results

            return record  # Return the fetched data

        except MySQLError as e:
            print(f"Error selecting student: {e}")
            return None  # Return None if an error occurs

        finally:
            # Ensure cursor and connection are closed properly
            if cursor:
                cursor.close()
            if db:
                db.close()

    def fetch_and_display_photo(self, student_id):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            print("Failed to connect to the database.")
            return None  # Exit if the connection is unsuccessful
        try:
            # Query to retrieve photo data (binary) for the student_id
            query = "SELECT photo_id FROM add_students WHERE id_addstudent = %s"
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()
            if result and result[0]:  # Check if there is photo data
                # Load image data from binary and create a QPixmap
                image_data = result[0]
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)

                # Set the QPixmap in QLabel and scale it to fit the label
                self.ui.update_photo_label.setPixmap(pixmap.scaled(
                    self.ui.update_photo_label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                ))
            else:
                # If no photo is found, clear the QLabel
                self.ui.update_photo_label.clear()

        except MySQLError as e:
            print(f"Error selecting student: {e}")
        finally:
            # Ensure cursor and connection are closed properly
            if cursor:
                cursor.close()
            if db:
                db.close()

    def update_student(self):
        # Get current values from the form
        firstname = self.ui.update_first_name_lineEdit.text().strip()
        lastname = self.ui.update_last_name_lineEdit.text().strip()
        birthdate = self.ui.update_birth_dateEdit.date().toString("yyyy-MM-dd")
        age = self.calculate_age(self.ui.update_birth_dateEdit.date())
        gender = self.ui.update_gender_comboBox.currentText().strip()
        classroom = self.ui.update_class_comboBox.currentText().strip()
        phone = self.ui.update_phone_lineEdit.text().strip()
        email = self.ui.update_email_lineEdit.text().strip()
        homeaddress = self.ui.update_address_lineEdit.text().strip()
        city = self.ui.update_city_lineEdit.text().strip()

        # Check for empty fields
        if (not firstname or not lastname or not email or not birthdate or 
            not gender or not classroom or not phone or not homeaddress or not city):
            show_message('Fields should not be empty!', 'warning', parent=self)
            return

        # Check if any field has changed or a new photo has been selected
        fields_unchanged = (
            firstname == self.first_name and
            lastname == self.last_name and
            birthdate == str(self.birthdate) and
            gender == self.gender and
            classroom == self.classroom and
            phone == str(self.phone).strip() and
            email == self.email and
            homeaddress == self.address and
            city == self.city and
            self.selected_image_path is None  # Ensure no new image was selected
        )

        if fields_unchanged:
            show_message("No changes were made.", "warning", parent=self)
            return

        # Prepare photo data if a new image was selected
        photo_data = self.photo_id  # Use existing photo if no new one is selected
        if self.selected_image_path:
            photo_data = convertToBinary(self.selected_image_path)

        # Proceed with the update
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            print("Failed to connect to the database.")
            return  # Exit if the connection is unsuccessful

        try:
            cursor.execute(
                """
                UPDATE add_students
                SET first_name = %s, last_name = %s, date_birth = %s, age = %s,
                    gender = %s, class = %s, phone = %s, email = %s,
                    address = %s, city = %s, photo_id = %s
                WHERE id_addstudent = %s
                """,
                (firstname, lastname, birthdate, age, gender, classroom, phone, email, homeaddress, city, photo_data, self.id_addstudent)
            )
            db.commit()  # Commit the changes
            show_message('Student data updated successfully!', 'success', parent=self)
            self.data_updated.emit()  # Emit the signal here

            # Close Update student's Dialog
            self.close()

        except MySQLError as e:
            print(f"Error updating student data: {e}")
            show_message('Failed to update student data.', 'error', parent=self)
        finally:
            # Ensure cursor and connection are closed properly
            if cursor:
                cursor.close()
            if db:
                db.close()


    def clear_all(self):
        self.ui.update_first_name_lineEdit.clear()
        self.ui.update_last_name_lineEdit.clear()
        # Reset date field to current date or a default value
        self.ui.update_birth_dateEdit.setDate(QDate.currentDate())
        # Reset combo boxes to default (usually index 0)
        self.ui.update_gender_comboBox.setCurrentIndex(0)
        self.ui.update_class_comboBox.setCurrentIndex(0)
        self.ui.update_phone_lineEdit.clear()
        self.ui.update_email_lineEdit.clear()
        self.ui.update_address_lineEdit.clear()
        self.ui.update_city_lineEdit.clear()
        # Clear the photo or reset it
        self.ui.update_photo_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UpdateStudent()
    win.show()
    # Run loop the app
    app.exec()