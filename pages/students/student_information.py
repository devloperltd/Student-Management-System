import pandas as pd
from PySide6.QtWidgets import (QTableWidgetItem, QFileDialog, QWidget,
                               QHBoxLayout, QPushButton)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize
from io import BytesIO
from PIL import Image
from PIL.ImageQt import ImageQt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib import colors
from utils.qdialog_utils import *  # Import global show_message function
from animations.CustomQDialog import *
from pages.students import add_student # Import add_student module
from pages.students import update_student # Import update_student module
from database.database_connection import get_database_connection
from pymysql.err import MySQLError

class StudentInfo:
    def __init__(self, ui, main_window):
        """
        Initialize with a reference to the main window's UI.
        """
        self.ui = ui
        self.main_window = main_window  # Store the main window reference
        self.ui.add_student_btn.clicked.connect(self.open_add_student)
        self.ui.to_excel_btn.clicked.connect(self.export_excel_students_details)
        self.ui.to_pdf_btn.clicked.connect(self.export_pdf_students_details)

        # Load student information to QTableWidget initially (show all)
        self.load_students_info()

        # Connect the search box textChanged signal to the filter function
        self.ui.students_searchBox.textChanged.connect(self.filter_students_by_search)

        # Connect comboboxes to filter method
        self.ui.filter_class_comboBox.currentTextChanged.connect(self.reload_studentstable_data)
        self.ui.filter_gender_comboBox.currentTextChanged.connect(self.reload_studentstable_data)

        # Connect the row selection signal to a function
        self.ui.students_table.itemSelectionChanged.connect(self.display_selected_student_info)

    # Display Selected Row in labels
    def display_selected_student_info(self):
        # Get the selected row index
        selected_row = self.ui.students_table.currentRow()

        if selected_row != -1:  # Make sure a row is selected
            # Get data from the selected row
            id_addstudent = int(self.ui.students_table.item(selected_row, 0).text())
            first_name = self.ui.students_table.item(selected_row, 1).text()
            last_name = self.ui.students_table.item(selected_row, 2).text()
            age = self.ui.students_table.item(selected_row, 4).text()

            # Update the labels with the selected data
            self.ui.first_name_label.setText(first_name)
            self.ui.last_name_label.setText(last_name)
            self.ui.age_label.setText(age)

            # Fetch and display the student's photo using their ID
            self.fetch_and_display_photo(id_addstudent)

    # Fetch and display the student's photo using their ID
    def fetch_and_display_photo(self, student_id):
        db, cursor = get_database_connection()
        if not db or not cursor:
            print("Failed to connect to the database.")
            return
        try:
            # Query to retrieve photo_id (binary data) using student_id
            query = "SELECT photo_id FROM add_students WHERE id_addstudent = %s"
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()

            if result and result[0]:  # Check if a photo is available
                # Convert binary data to QPixmap
                image_data = result[0]
                image = Image.open(BytesIO(image_data))
                qt_image = QPixmap.fromImage(ImageQt(image))
                
                # Display the image in id_label, scaled to fit
                self.ui.id_label.setPixmap(qt_image.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                # Clear the image if no photo is found
                self.ui.id_label.clear()
        finally:
            if db:
                db.close()

    # Opens add student dialog with animations
    def open_add_student(self):
        """
        Opens the AddStudent dialog with animations.
        """
        if hasattr(self, 'add_student') and self.add_student.isVisible():
            self.add_student.raise_()  # Bring the existing dialog to the front
            self.add_student.main_window = self.main_window
        else:
            # Pass the correct QWidget (like the main window) as the parent
            animation_dialog_Window(self.main_window, add_student.AddStudent)  # Pass main_window as parent
            self.reload_studentstable_data()

    # Reload student information In QTableWidget
    def reload_studentstable_data(self):
        self.load_students_info()

    # Search Box by Filter rows in QTableWidget
    def filter_students_by_search(self, text):
        """
        Filter students in the students_table based on the first word typed in the search box.
        """
        # Get the number of rows in the table
        row_count = self.ui.students_table.rowCount()

        for row in range(row_count):
            # Assume no match initially
            match = False

            # Check each column in the row for a match with the start of the cell content
            for column in range(self.ui.students_table.columnCount()):
                item = self.ui.students_table.item(row, column)
                if item and item.text().lower().startswith(text.lower()):
                    match = True
                    break

            # Hide the row if no match, show otherwise
            self.ui.students_table.setRowHidden(row, not match)

    # Load and filter student information to QTableWidget
    def load_students_info(self):
        # Clear existing data in the table
        self.ui.students_table.setRowCount(0)

        # Get selected class and gender from the comboboxes
        selected_class = self.ui.filter_class_comboBox.currentText()
        selected_gender = self.ui.filter_gender_comboBox.currentText()

        # Check if filtering is necessary
        class_filter = selected_class != "Filter by class"
        gender_filter = selected_gender != "Filter by gender"

        # Build the SQL query dynamically
        # based on the selected class and gender
        query = """
            SELECT id_addstudent, first_name, last_name, date_birth, age, gender, class, phone, email, address, city
            FROM add_students
            WHERE 1=1
        """
        params = []

        # Apply class filter only if a valid class is selected
        if class_filter:
            query += " AND class = %s"
            params.append(selected_class)

        # Apply gender filter only if a valid gender is selected
        if gender_filter:
            query += " AND gender = %s"
            params.append(selected_gender)

        # Fetch filtered or unfiltered data from the database
        db, cursor = get_database_connection()  # Use the function to get the connection and cursor
        if db is None or cursor is None:
            print("Failed to connect to the database.")
            return  # Exit if the connection is unsuccessful
        try:
            cursor.execute(query, params)  # Execute the SQL query with parameters
            result = cursor.fetchall()  # Fetch all rows from the query

            # Loop through the result and insert them into the QTableWidget
            for row_number, row_data in enumerate(result):
                self.ui.students_table.insertRow(row_number)  # Add a new row for each student

                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)  # Center-align the text
                    self.ui.students_table.setItem(row_number, column_number, item)

                    # ِCreate a custom widget with tow buttons lineed up horizontally for the actions column
                    double_button_widget = DoubleButtonWidgetStudents(row_number, row_data, self)

                    # ِSet this custom widget with tow buttons as the cell widget for the actions column
                    self.ui.students_table.setCellWidget(row_number, 11, double_button_widget)
                    self.ui.students_table.setRowHeight(row_number, 45)

        except MySQLError as e:
            print(f"Error retrieving data from database: {e}")
        finally:
            if db:
                cursor.close() # Close the cursor
                db.close() # Close the connection when done

    # TO EXCEL EXPORT
    def export_excel_students_details(self):
        # Convert QTableWidget to Pandas DataFrame
        data = []
        self.headers = [self.ui.students_table.horizontalHeaderItem(col).text() for col in range(self.ui.students_table.columnCount())]
        for row in range(self.ui.students_table.rowCount()):
            # Check if the item is not None before accessing it's text
            row_data = [self.ui.students_table.item(row, col).text() if self.ui.students_table.item(row, col) is not None else "" for col in range(self.ui.students_table.columnCount())]
            data.append(row_data)

        # Create a Pandas Data Frame with collected data and the header's
        df = pd.DataFrame(data, columns=self.headers)

        # Save Data Frame to Excel File
        # Exclude the last column before exporting
        df_filtered = df.iloc[ :, :-1 ]

        # Opoen QFileDialog to get the file path
        file_filter = "Files (*.xlsx)"
        filename, _ = QFileDialog.getSaveFileName(None, "Save Excel File", "", file_filter)
        if filename:
            df_filtered.to_excel(filename, index=False)
            print(f"Table exported to {filename}")
            show_message('Excel File exported Successfully !!!', 'success')

    # TO PDF EXPORT
    def export_pdf_students_details(self):
        # Open QFileDialog to get the file path
        file_filter = "PDF Files (*.pdf)"
        filename, _ = QFileDialog.getSaveFileName(None, "Save PDF File", "", file_filter)
        if filename:
            # Define margins (in points)
            margin_left = 20
            margin_right = 20
            margin_top = 20
            margin_bottom = 20

            # Create a PDF Document with A4 page size and specified margins
            pdf_document = SimpleDocTemplate(
                filename, 
                pagesize=A4,
                leftMargin=margin_left,
                rightMargin=margin_right,
                topMargin=margin_top,
                bottomMargin=margin_bottom
            )
            
            # Get total number of columns in QTableWidget
            n = self.ui.students_table.columnCount()
            
            # Extract headers from the QTableWidget, excluding the last column
            headers = [self.ui.students_table.horizontalHeaderItem(col).text() for col in range(n - 1)]
            
            # Extract data from the QTableWidget, excluding the last column
            data = [headers]
            for row in range(self.ui.students_table.rowCount()):
                row_data = [
                    self.ui.students_table.item(row, col).text() if self.ui.students_table.item(row, col) is not None else ""
                    for col in range(n - 1)
                ]
                data.append(row_data)

            # Calculate column widths based on A4 page width minus margins
            page_width, _ = A4
            available_width = page_width - margin_left - margin_right
            column_width = available_width / (n - 1)  # Divide available width by number of columns

            # Create PDF Table with calculated column widths
            pdf_table = Table(data, colWidths=[column_width] * (n - 1))

            # Apply Styles to the Table
            style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])
            pdf_table.setStyle(style)

            # Build the PDF Document
            pdf_document.build([pdf_table])
            print(f"Table exported to {filename}")
            show_message('PDF file exported successfully!', 'success')


# Bouble Buttons Class
class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_number, row_data, MainProject):
        super().__init__()
        # Store a reference to MainProject as the parent
        self.Mainproject = MainProject
        # Ensure access to the main window
        self.main_window = MainProject.main_window

        # Store the row number and row_data as an instance in variables
        self.row_number = row_number
        self.row_data = row_data

        # Get student variables from the tuple
        self.id_addstudent  = self.row_data[0]

        layout = QHBoxLayout(self)

        # Create blue Edit button
        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("""
                                       QPushButton{
                                       background-color:rgb(33, 156, 144);
                                       border-radius:3px;
                                       }
                                        """)
        self.edit_button.setFixedSize(35, 25)

        # Create red Delete button
        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("""
                                        QPushButton{
                                        background-color:rgb(195, 64, 115);
                                        border-radius:3px;
                                        }
                                        """)
        self.delete_button.setFixedSize(35, 25)

        # Set icons for the button's
        icon = QIcon("icons/edit.png")
        self.edit_button.setIcon(icon)

        icon2 = QIcon("icons/trash-bin.png")
        self.delete_button.setIcon(icon2)

        # Set icon sizes
        self.edit_button.setIconSize(QSize(15, 15))  # Set size for edit button icon
        self.delete_button.setIconSize(QSize(15, 15))  # Set size for delete button icon

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        self.edit_button.clicked.connect(self.open_update_student)
        self.delete_button.clicked.connect(self.show_confirm_delete_dialog)

    # Show Confirm Message Dialog
    def show_confirm_delete_dialog(self):
        # Pass MainProject instead of self.Mainproject
        parent_widget = self.Mainproject if isinstance(self.Mainproject, QWidget) else QApplication.activeWindow()
        # Title and content for the confirmation dialog
        title_message = f" You will delete '{self.row_data[1]} {self.row_data[2]}' permanently!!"
        content_message = "Are you sure you want to delete this student from database?"
        if animate_confirm_delete_msg(parent_widget, self.delete_student, title_message=title_message, content_message=content_message):
            print("Confirmed deletion.")
   
    # Methods to open Update student window
    def open_update_student(self):
        if hasattr(self, 'update_student') and self.update_student.isVisible():
            self.update_student.raise_()  # Bring the existing dialog to the front
        else:
            # Pass the dialog class directly; no need for `partial`
            animation_dialog_Window(
                self.Mainproject.main_window,
                lambda parent: update_student.UpdateStudent(self.row_number, self.row_data, parent)
            )

            # Notify MainProject to reload data after deletion
            self.Mainproject.reload_studentstable_data()

    # Method to delete the student from the database
    def delete_student(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            print("Failed to connect to the database.")
            return  # Exit if the connection is unsuccessful
        try:
            # Delete the student record
            query = "DELETE FROM add_students WHERE id_addstudent = %s"
            cursor.execute(query, (self.id_addstudent,))
            db.commit()
            show_message('Student has been deleted successfully')

            # Notify MainProject to reload data after deletion
            self.Mainproject.reload_studentstable_data()
            #self.main_window.dashboard_content.total_students()

        except MySQLError as e:
            print(f"Error deleting student: {e}")
        finally:
            if cursor:
                cursor.close()  # Close the cursor
            if db:
                db.close()  # Close the connection when done