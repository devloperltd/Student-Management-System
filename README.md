# Laroussi Student Management system Project 2024
Laroussi Student Management System is a desktop application developed on Piside6 & Qt Designer.
is designed to record, analyze, and manage information in a school. These systems are updated by teachers and school administrators on a rolling basis to better serve the needs of the greater student body. Without them, schools would become disorganized, staff would lack clarity into scheduling and student activity, and it would become increasingly difficult for school districts to leverage data in the decision-making process.

![2024-12-23_115235](https://github.com/user-attachments/assets/8abe16a4-ab65-4561-88c3-ad00d689a785)

## Credits :
- !/usr/bin/env python3.13.1
- Laroussi Boulanour (GUI, design & coding)
- 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 : [HERE](https://www.facebook.com/Laroussi.Br)
- 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 : [HERE](https://t.me/UncleAnonymous)
- 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 : [HERE](https://laroussigsm.net/)

# Features :

- Animating Pyside6 widgets with QPropertyAnimation.
- Use a Reference to the Main UI.
- Separation of Concerns.
- Ease of Access.
- Flexibility for Refactoring.
- Project Scaling.
- Code Reusability
- Testing and Maintenance.

## Modern UI - Python Graphical User Interface | Login/Register Form | PySide, PyQt, Qt :
- Qt, QPropertyAnimation, QRect, QTimer
- connect a signal to a slot
- JSON files allow you to define all animation properties (duration, easing curves, target objects, etc.) in a centralized location.
- and more advanced project ....

![2024-12-23_115221](https://github.com/user-attachments/assets/90d2b49d-100d-43ce-8e6f-8e453e04d6b1)


## Installation :
- Install Python >= 3.13.1 from the official website [HERE](https://www.python.org/)

## Create python 3.13.1 venv and Activated :

```sh
python -m venv Your_env_name
Your_env_name\Scripts\activate
pip3 install -r requirements.txt
```
## Command Line Tool For Converting .qrc Files Into .py Files :

```sh
pyside6-rcc ico.qrc -o ico_rc.py
```
## Command Line Tool For Converting .uic Files Into .py Files :

```sh
pyside6-uic mainwindow.ui -o ui_mainwindow.py
```
![2024-12-24_230539](https://github.com/user-attachments/assets/f8636393-b022-44d7-812e-e7b656e0e7e2)


## Import/Export Database Using MySQL Workbench :

- Download the latest version of MySQL Workbench from official website : [HERE](https://dev.mysql.com/downloads/workbench/)
- Under Server Administration on the Home window select the server instance you want to restore database to (Create New Server Instance if doing it first time).
- Click on Manage Import/Export.
- Click on Data Import/Restore on the left side of the screen.
- Select Import from Self-Contained File radio button (right side of screen).
- Select the path of .sql.
- Click Start Import button at the right bottom corner of window.

![2024-12-24_193958](https://github.com/user-attachments/assets/c14e1916-92a3-4e4f-89a9-0383f3a9f30b)

## Database instruction :

### Table: add_students :
```sh
Columns:
id_addstudent int AI PK 
first_name varchar(45) 
last_name varchar(45) 
date_birth date 
age int 
gender varchar(45) 
class varchar(45) 
phone int 
email varchar(45) 
address varchar(45) 
city varchar(45) 
photo_id longblob
```
### Table: registration :
```sh
registration_id int AI PK 
username varchar(45) 
password varchar(45) 
email varchar(45)
```

## Control flags for animation activation :
from qdialog_utils.py Set to True to enable effect, False to disable.

```sh
    apply_slide = False
    apply_bounce = False
    apply_zoom = True
    apply_fade = False
    apply_scale_fade = False
```
![2024-12-23_115300](https://github.com/user-attachments/assets/2173924a-9187-4000-b44e-2a9f0bc9f5d3)

## Example To switch between Animation Effects From CustomQDialog.py :

```sh
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
```
Replace [animation_dialog_Window] with [slide_dialog_Window] or [slide_out_dialog_Window]

## Parameters To Custom Json File :
Adjust settings as needed. [ active ], [ duration ], [ easingCurve ]

```sh
{
    "fade": [
        {
            "active": true,
            "duration": 2000,
            "easingCurve": "OutBack"
        }
    ],
    "slide": [
        {
            "active": true,
            "speed": 500,
            "direction": "right-to-left"
        }
    ],
    "bounce": [
        {
            "active": true,
            "direction": "horizontal",
            "duration": 800,
            "easingCurve": "OutBounce"
        }
    ],
    "zoom": [
        {
            "active": true,
            "duration": 800,
            "easingCurve": "OutBounce"
        }
    ],
    "scale_fade": [
        {
            "active": true,
            "duration": 1000,
            "easingCurve": "OutBack"
        }
    ]
}
```
![2024-12-23_115310](https://github.com/user-attachments/assets/92103506-899e-447c-b991-a16349f80192)


## MIT License :

Copyright (c) [2024] [LAROUSSI BOULANOUAR]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
