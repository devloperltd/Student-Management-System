<<<<<<< HEAD
from utils.qdialog_utils import *
from database.database_connection import get_database_connection
from pymysql.err import MySQLError
from PySide6.QtCharts import (QChart, QPieSeries, QBarSet, QBarSeries,
                              QBarCategoryAxis, QValueAxis, QAbstractBarSeries)
from PySide6.QtGui import QPainter, QColor


class dashboard_page:
    def __init__(self, ui, main_window):
        """
        Initialize with a reference to the main window's UI.
        """
        self.ui = ui
        self.main_window = main_window  # Store the main window reference

        # Load student count when the dashboard initializes
        self.total_students()
        self.total_male()
        self.total_female()
        self.show_donut_chart()
        self.show_bar_chart()

        # Connect buttons with a reference to the main window's UI
        self.ui.show_more_students_btn.clicked.connect(self.show_all_gender)
        self.ui.show_more_male_btn.clicked.connect(self.filter_student_by_male)
        self.ui.show_more_female_btn.clicked.connect(self.filter_student_by_female)

    # Method to load the total students in label
    def total_students(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return  # Exit if the connection is unsuccessful

        try:
            cursor.execute('SELECT COUNT(*) FROM add_students')  # Efficient count query
            total_students = cursor.fetchone()[0]  # Fetch the count directly
            self.ui.total_student_label.setText(f"{total_students}")  # Update total students label

        except MySQLError as e:
            show_message(f"Error retrieving data from database: {e}", 'error', parent=self)  # User-friendly error message

        finally:
            if db:
                cursor.close()  # Close the cursor
                db.close()  # Close the connection when done

    # Method to load the total male in label
    def total_male(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return  # Exit if the connection is unsuccessful

        try:
            cursor.execute("SELECT COUNT(*) FROM add_students WHERE gender = 'Male'")  # Efficient "male" count query
            total_male = cursor.fetchone()[0]  # Fetch the male student count
            self.ui.total_male_label.setText(f"{total_male}")  # Update total male label

        except MySQLError as e:
            show_message(f"Error retrieving data from database: {e}", 'error', parent=self)  # User-friendly error message

        finally:
            if db:
                cursor.close()  # Close the cursor
                db.close()  # Close the connection when done

    # Method to load the total female in label
    def total_female(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return  # Exit if the connection is unsuccessful

        try:
            cursor.execute("SELECT COUNT(*) FROM add_students WHERE gender = 'Female'")  # Efficient "female" count query
            total_female = cursor.fetchone()[0]  # Fetch the female student count
            self.ui.total_female_label.setText(f"{total_female}")  # Update total female label

        except MySQLError as e:
            show_message(f"Error retrieving data from database: {e}", 'error', parent=self)  # User-friendly error message

        finally:
            if db:
                cursor.close()  # Close the cursor
                db.close()  # Close the connection when done

    # Set the all gender 'Male & Female'
    def show_all_gender(self):
        # Set the gender filter to 'Filter by gender'
        self.ui.filter_gender_comboBox.setCurrentText("Filter by gender")
        # Switch to the student information page if not already there
        self.main_window.switch_to_student_info_page()

    # Set the gender filter to 'Male'
    def filter_student_by_male(self):
        # Set the gender filter to 'Male'
        self.ui.filter_gender_comboBox.setCurrentText("Male")       
        # Switch to the student information page if not already there
        self.main_window.switch_to_student_info_page()

    # Set the gender filter to 'Female'
    def filter_student_by_female(self):
        # Set the gender filter to 'Female'
        self.ui.filter_gender_comboBox.setCurrentText("Female")
        # Switch to the student information page if not already there
        self.main_window.switch_to_student_info_page()

    # QChartView Students Pie chart in the QGraphicsView
    def show_donut_chart(self):
        # Get data for the donut chart
        total_students = int(self.ui.total_student_label.text())
        total_male = int(self.ui.total_male_label.text())
        total_female = int(self.ui.total_female_label.text())

        # Handle case where there are no students
        if total_students == 0:
            chart = QChart()
            chart.setTitle("No Data Available")
            chart_view = self.ui.students_piechart  # This is the promoted QChartView
            chart_view.setChart(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)
            return

        # Donut chart data
        labels = ['Total Students', 'Male Students', 'Female Students']
        sizes = [total_students, total_male, total_female]
        colors = ['#0d92f4', '#ffb200', '#f05a7e']  # Custom colors for slices
        explode = [0, 0, 0.1]  # Highlight the first slice slightly

        # Create a pie series and add data
        series = QPieSeries()
        for label, size, color, explode_value in zip(labels, sizes, colors, explode):
            slice = series.append(label, size)
            # Convert the color string to QColor
            slice.setBrush(QColor(color))  # Use QColor to set the brush color
            slice.setLabelVisible(True)

            # Add percentage labels
            percentage = (size / total_students) * 100 if total_students > 0 else 0
            slice.setLabel(f"{label}: {percentage:.1f}%")  # Format the label with percentage

            if explode_value > 0:  # Check if the slice should be exploded
                slice.setExploded(True)
                slice.setExplodeDistanceFactor(explode_value)

        # Create a chart and add the series
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Student Distribution")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Set the hole size for the donut effect (the range is 0.0 to 1.0, where 1.0 is a full circle)
        series.setHoleSize(0.3)  # Adjust this value to make the hole smaller or larger

        # Set rendering hints for better visual quality
        chart_view = self.ui.students_piechart  # This is the promoted QChartView
        chart_view.setChart(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Optionally, you can make the chart responsive by setting a layout
        chart_view.setMinimumHeight(300)  # Adjust as needed
        chart_view.setMinimumWidth(300)  # Adjust as needed


    # QChartView Students Bar chart in the QGraphicsView
    def show_bar_chart(self):
        # Create a bar series
        bar_series = QBarSeries()
        bar_series.setName("Student Distribution (Bar Chart)")

        # Set the width of the bars
        bar_series.setBarWidth(0.9)  # Adjust width (default is 0.15)

        # Get data for the bar chart
        categories = ['Total Students', 'Male Students', 'Female Students']
        colors = ['#0d92f4', '#ffb200', '#f05a7e']  # Define custom colors
        total_students = int(self.ui.total_student_label.text())
        total_male = int(self.ui.total_male_label.text())
        total_female = int(self.ui.total_female_label.text())

        # Create bar sets for each data type
        bar_set_total_students = QBarSet("Total Students")
        bar_set_total_students.append([total_students, 0, 0])  # Values for all categories

        bar_set_total_male = QBarSet("Male Students")
        bar_set_total_male.append([0, total_male, 0])          # Values for all categories

        bar_set_total_female = QBarSet("Female Students")
        bar_set_total_female.append([0, 0, total_female])      # Values for all categories

        # Set custom colors for each bar set
        bar_set_total_students.setColor(colors[0])
        bar_set_total_male.setColor(colors[1])
        bar_set_total_female.setColor(colors[2])

        # Add the bar sets to the series
        bar_series.append(bar_set_total_students)
        bar_series.append(bar_set_total_male)
        bar_series.append(bar_set_total_female)

        # Enable labels to show numbers inside the bars
        bar_series.setLabelsVisible(True)
        bar_series.setLabelsPosition(QAbstractBarSeries.LabelsInsideEnd)  # Position labels inside bars
        bar_series.setLabelsFormat("@value")  # Display the value of the bar

        # Create a chart and add the bar series
        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle("Student Distribution (Bar Chart)")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Create a category axis for labels (X-axis)
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        bar_series.attachAxis(axis_x)

        # Create a value axis for the Y-axis
        axis_y = QValueAxis()
        axis_y.setRange(0, max(total_students, total_male, total_female) + 1)  # Automatically scale range
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        bar_series.attachAxis(axis_y)

        # Apply the chart to the view
        self.ui.students_barchart.setChart(chart)
        self.ui.students_barchart.setMinimumSize(300, 300)  # Ensure the chart is visible
=======
from utils.qdialog_utils import *
from database.database_connection import get_database_connection
from pymysql.err import MySQLError
from PySide6.QtCharts import (QChart, QPieSeries, QBarSet, QBarSeries,
                              QBarCategoryAxis, QValueAxis, QAbstractBarSeries)
from PySide6.QtGui import QPainter, QColor


class dashboard_page:
    def __init__(self, ui, main_window):
        """
        Initialize with a reference to the main window's UI.
        """
        self.ui = ui
        self.main_window = main_window  # Store the main window reference

        # Load student count when the dashboard initializes
        self.total_students()
        self.total_male()
        self.total_female()
        self.show_donut_chart()
        self.show_bar_chart()

        # Connect buttons with a reference to the main window's UI
        self.ui.show_more_students_btn.clicked.connect(self.show_all_gender)
        self.ui.show_more_male_btn.clicked.connect(self.filter_student_by_male)
        self.ui.show_more_female_btn.clicked.connect(self.filter_student_by_female)

    # Method to load the total students in label
    def total_students(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return  # Exit if the connection is unsuccessful

        try:
            cursor.execute('SELECT COUNT(*) FROM add_students')  # Efficient count query
            total_students = cursor.fetchone()[0]  # Fetch the count directly
            self.ui.total_student_label.setText(f"{total_students}")  # Update total students label

        except MySQLError as e:
            show_message(f"Error retrieving data from database: {e}", 'error', parent=self)  # User-friendly error message

        finally:
            if db:
                cursor.close()  # Close the cursor
                db.close()  # Close the connection when done

    # Method to load the total male in label
    def total_male(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return  # Exit if the connection is unsuccessful

        try:
            cursor.execute("SELECT COUNT(*) FROM add_students WHERE gender = 'Male'")  # Efficient "male" count query
            total_male = cursor.fetchone()[0]  # Fetch the male student count
            self.ui.total_male_label.setText(f"{total_male}")  # Update total male label

        except MySQLError as e:
            show_message(f"Error retrieving data from database: {e}", 'error', parent=self)  # User-friendly error message

        finally:
            if db:
                cursor.close()  # Close the cursor
                db.close()  # Close the connection when done

    # Method to load the total female in label
    def total_female(self):
        # Get a database connection and cursor
        db, cursor = get_database_connection()
        if db is None or cursor is None:
            show_message('Database connection failed. Please try again later.', 'error', parent=self)
            return  # Exit if the connection is unsuccessful

        try:
            cursor.execute("SELECT COUNT(*) FROM add_students WHERE gender = 'Female'")  # Efficient "female" count query
            total_female = cursor.fetchone()[0]  # Fetch the female student count
            self.ui.total_female_label.setText(f"{total_female}")  # Update total female label

        except MySQLError as e:
            show_message(f"Error retrieving data from database: {e}", 'error', parent=self)  # User-friendly error message

        finally:
            if db:
                cursor.close()  # Close the cursor
                db.close()  # Close the connection when done

    # Set the all gender 'Male & Female'
    def show_all_gender(self):
        # Set the gender filter to 'Filter by gender'
        self.ui.filter_gender_comboBox.setCurrentText("Filter by gender")
        # Switch to the student information page if not already there
        self.main_window.switch_to_student_info_page()

    # Set the gender filter to 'Male'
    def filter_student_by_male(self):
        # Set the gender filter to 'Male'
        self.ui.filter_gender_comboBox.setCurrentText("Male")       
        # Switch to the student information page if not already there
        self.main_window.switch_to_student_info_page()

    # Set the gender filter to 'Female'
    def filter_student_by_female(self):
        # Set the gender filter to 'Female'
        self.ui.filter_gender_comboBox.setCurrentText("Female")
        # Switch to the student information page if not already there
        self.main_window.switch_to_student_info_page()

    # QChartView Students Pie chart in the QGraphicsView
    def show_donut_chart(self):
        # Get data for the donut chart
        total_students = int(self.ui.total_student_label.text())
        total_male = int(self.ui.total_male_label.text())
        total_female = int(self.ui.total_female_label.text())

        # Handle case where there are no students
        if total_students == 0:
            chart = QChart()
            chart.setTitle("No Data Available")
            chart_view = self.ui.students_piechart  # This is the promoted QChartView
            chart_view.setChart(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)
            return

        # Donut chart data
        labels = ['Total Students', 'Male Students', 'Female Students']
        sizes = [total_students, total_male, total_female]
        colors = ['#0d92f4', '#ffb200', '#f05a7e']  # Custom colors for slices
        explode = [0, 0, 0.1]  # Highlight the first slice slightly

        # Create a pie series and add data
        series = QPieSeries()
        for label, size, color, explode_value in zip(labels, sizes, colors, explode):
            slice = series.append(label, size)
            # Convert the color string to QColor
            slice.setBrush(QColor(color))  # Use QColor to set the brush color
            slice.setLabelVisible(True)

            # Add percentage labels
            percentage = (size / total_students) * 100 if total_students > 0 else 0
            slice.setLabel(f"{label}: {percentage:.1f}%")  # Format the label with percentage

            if explode_value > 0:  # Check if the slice should be exploded
                slice.setExploded(True)
                slice.setExplodeDistanceFactor(explode_value)

        # Create a chart and add the series
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Student Distribution")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Set the hole size for the donut effect (the range is 0.0 to 1.0, where 1.0 is a full circle)
        series.setHoleSize(0.3)  # Adjust this value to make the hole smaller or larger

        # Set rendering hints for better visual quality
        chart_view = self.ui.students_piechart  # This is the promoted QChartView
        chart_view.setChart(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Optionally, you can make the chart responsive by setting a layout
        chart_view.setMinimumHeight(300)  # Adjust as needed
        chart_view.setMinimumWidth(300)  # Adjust as needed


    # QChartView Students Bar chart in the QGraphicsView
    def show_bar_chart(self):
        # Create a bar series
        bar_series = QBarSeries()
        bar_series.setName("Student Distribution (Bar Chart)")

        # Set the width of the bars
        bar_series.setBarWidth(0.9)  # Adjust width (default is 0.15)

        # Get data for the bar chart
        categories = ['Total Students', 'Male Students', 'Female Students']
        colors = ['#0d92f4', '#ffb200', '#f05a7e']  # Define custom colors
        total_students = int(self.ui.total_student_label.text())
        total_male = int(self.ui.total_male_label.text())
        total_female = int(self.ui.total_female_label.text())

        # Create bar sets for each data type
        bar_set_total_students = QBarSet("Total Students")
        bar_set_total_students.append([total_students, 0, 0])  # Values for all categories

        bar_set_total_male = QBarSet("Male Students")
        bar_set_total_male.append([0, total_male, 0])          # Values for all categories

        bar_set_total_female = QBarSet("Female Students")
        bar_set_total_female.append([0, 0, total_female])      # Values for all categories

        # Set custom colors for each bar set
        bar_set_total_students.setColor(colors[0])
        bar_set_total_male.setColor(colors[1])
        bar_set_total_female.setColor(colors[2])

        # Add the bar sets to the series
        bar_series.append(bar_set_total_students)
        bar_series.append(bar_set_total_male)
        bar_series.append(bar_set_total_female)

        # Enable labels to show numbers inside the bars
        bar_series.setLabelsVisible(True)
        bar_series.setLabelsPosition(QAbstractBarSeries.LabelsInsideEnd)  # Position labels inside bars
        bar_series.setLabelsFormat("@value")  # Display the value of the bar

        # Create a chart and add the bar series
        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle("Student Distribution (Bar Chart)")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Create a category axis for labels (X-axis)
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        bar_series.attachAxis(axis_x)

        # Create a value axis for the Y-axis
        axis_y = QValueAxis()
        axis_y.setRange(0, max(total_students, total_male, total_female) + 1)  # Automatically scale range
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        bar_series.attachAxis(axis_y)

        # Apply the chart to the view
        self.ui.students_barchart.setChart(chart)
        self.ui.students_barchart.setMinimumSize(300, 300)  # Ensure the chart is visible
>>>>>>> 317bfcbba86aa64c83a359b578861a738cd9b39f
