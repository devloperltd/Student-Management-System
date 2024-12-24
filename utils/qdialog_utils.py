import os
import json
from PySide6.QtCore import QTimer
from messages.ui_warning_msg import Ui_warning_msg
from messages.ui_success_msg import Ui_success_msg
from messages.ui_error_msg import Ui_error_msg
from messages.ui_confirm_close_msg import Ui_Confirm_close_msg
from messages.ui_confirm_delete_msg import Ui_confirm_delete_msg
from animations.CustomQDialog import *
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import Qt


# Define the path for QDialog.json relative to message_utils.py
qdialog_json_path = os.path.join(os.path.dirname(__file__), '..', 'Json', 'QDialog.json')
with open(qdialog_json_path, 'r') as file:
    qdialog_animation_params = json.load(file)
    # print(f"Loaded animation parameters: {qdialog_animation_params}")

# Function to show success, warning, or error messages
def show_message(message, message_type='success', parent=None):
    # Use active window as parent if none is provided
    if parent is None:
        parent = QApplication.activeWindow()

    if message_type == 'success':
        message_box = Ui_success_msg(parent)
        message_box.show_success(message)
    elif message_type == 'warning':
        message_box = Ui_warning_msg(parent)
        message_box.show_warning(message)
    elif message_type == 'error':
        message_box = Ui_error_msg(parent)
        message_box.show_error(message)
    else:
        raise ValueError("Invalid message type. Use 'success', 'warning', or 'error'.")

    message_box.setModal(True)
    message_box.show()

    # Retain the message box in the parent to prevent premature deletion
    if parent is not None:
        if not hasattr(parent, "_active_message_boxes"):
            parent._active_message_boxes = []
        parent._active_message_boxes.append(message_box)

    # Extract the animation parameters
    slide_params = qdialog_animation_params.get("slide", [{}])[0]
    animation = slide_msg_dialog(message_box, slide_params)
    message_box.animation = animation  # Retain the animation reference
    print("show_message: Message box shown with slide animation")

    # Set a timer to hide the message box with slide-out after 2000ms
    def hide_with_slide_out():
        print("Hiding message box with slide-out animation after 2000ms.")
        slide_out_animation = slide_out_msg_dialog(message_box, slide_params)
        message_box.slide_out_msg_dialog = slide_out_animation  # Retain the animation reference
        slide_out_animation.finished.connect(lambda: parent._active_message_boxes.remove(message_box))

    QTimer.singleShot(2000, hide_with_slide_out)

# Function to show a confirmation close dialog with effect
def animate_confirm_close_msg(parent, on_confirm_callback):
    # Create the confirmation dialog
    confirm_close_dialog = Ui_Confirm_close_msg(parent)
    confirm_close_dialog.setModal(True)
    confirm_close_dialog.confirmed.connect(on_confirm_callback)

    # Load animation parameters from QDialog.json (you still use this data, but control activation here)
    slide_params = next((p for p in qdialog_animation_params["slide"] if p.get("active", True)), {})
    bounce_params = next((p for p in qdialog_animation_params["bounce"] if p.get("active", True)), {})
    zoom_params = next((p for p in qdialog_animation_params["zoom"] if p.get("active", True)), {})
    fade_params = next((p for p in qdialog_animation_params["fade"] if p.get("active", True)), {})
    scale_fade_params = next((p for p in qdialog_animation_params["scale_fade"] if p.get("active", True)), {})

    # Control flags for animation activation (set them to True or False as desired)
    apply_slide = False  # Set to True to enable bounce, False to disable
    apply_bounce = False  # Set to True to enable bounce, False to disable
    apply_zoom = True    # Set to True to enable zoom, False to disable
    apply_fade = False   # Set to True to enable fade, False to disable
    apply_scale_fade = False  # Set to True to enable scale fade, False to disable

    parent_geometry = parent.geometry()

    # Check which animation should be applied
    animation = None

    # Check slide animation (apply if `apply_bounce` is True)
    if apply_slide and slide_params.get("active", False):  # Apply slide if active and flag is True
        animation = slide_msg_dialog(confirm_close_dialog, slide_params)
    # Check bounce animation (apply if `apply_bounce` is True)
    if apply_bounce and bounce_params.get("active", False):  # Apply bounce if active and flag is True
        animation = bounce_dialog(confirm_close_dialog, bounce_params, parent_geometry)
    # Check zoom animation (apply if `apply_zoom` is True)
    elif apply_zoom and zoom_params.get("active", False):  # Apply zoom if active and flag is True
        animation = zoom_dialog(confirm_close_dialog, zoom_params)
    # Check fade animation (apply if `apply_fade` is True)
    elif apply_fade and fade_params.get("active", False):  # Apply fade if active and flag is True
        animation = fade_dialog(confirm_close_dialog, fade_params)
    # Check scale fade animation (apply if `apply_scale_fade` is True)
    elif apply_scale_fade and scale_fade_params.get("active", False):  # Apply scale fade if active and flag is True
        animation = scale_fade_dialog(confirm_close_dialog, scale_fade_params)

    # Start the animation if available
    if animation:
        if isinstance(animation, tuple):  # For zoom_dialog that returns multiple animations
            for anim in animation:
                anim.start()
        else:
            animation.start()

    # Show the dialog (exec blocks until the user closes the dialog)
    return confirm_close_dialog.exec() == QDialog.Accepted


# Function to show a confirmation delete dialog with animation
def animate_confirm_delete_msg(parent, on_confirm_callback, title_message=None, content_message=None):
    """
    Show a confirmation delete dialog with optional animations and customizable messages.

    :param parent: The parent widget (e.g., QMainWindow or QDialog).
    :param on_confirm_callback: The callback function to execute upon confirmation.
    :param title_message: Custom title message for the dialog (optional).
    :param content_message: Custom content message for the dialog (optional).
    """
    # Ensure parent is valid
    if parent is None:
        print("Warning: Parent is None. Falling back to active window.")
        parent = QApplication.activeWindow()

    # Initialize the confirmation dialog
    confirm_delete_dialog = Ui_confirm_delete_msg(parent)
    confirm_delete_dialog.setModal(True)  # Set modal to prevent interactions with MainProject
    confirm_delete_dialog.confirmed.connect(on_confirm_callback)  # Connect the callback

    # Update dialog messages
    if title_message:
        confirm_delete_dialog.title_msg_label.setText(title_message)
    if content_message:
        confirm_delete_dialog.content_msg_label.setText(content_message)

    # Handle cases where the parent has no geometry (optional fallback geometry)
    parent_geometry = parent.geometry() if parent else None

    # Load animation parameters from QDialog.json
    slide_params = next((p for p in qdialog_animation_params["slide"] if p.get("active", True)), {})
    bounce_params = next((p for p in qdialog_animation_params["bounce"] if p.get("active", True)), {})
    zoom_params = next((p for p in qdialog_animation_params["zoom"] if p.get("active", True)), {})
    fade_params = next((p for p in qdialog_animation_params["fade"] if p.get("active", True)), {})
    scale_fade_params = next((p for p in qdialog_animation_params["scale_fade"] if p.get("active", True)), {})

    # Control flags for animation activation
    apply_slide = False   # Enable/disable slide animation
    apply_bounce = False   # Enable/disable bounce animation
    apply_zoom = True    # Enable/disable zoom animation
    apply_fade = False    # Enable/disable fade animation
    apply_scale_fade = False  # Enable/disable scale fade animation

    # Check which animation should be applied
    animation = None
    if apply_slide and slide_params.get("active", False) and parent_geometry:
        animation = slide_msg_dialog(confirm_delete_dialog, slide_params)
    elif apply_bounce and bounce_params.get("active", False) and parent_geometry:
        animation = bounce_dialog(confirm_delete_dialog, bounce_params, parent_geometry)
    elif apply_zoom and zoom_params.get("active", False):
        animation = zoom_dialog(confirm_delete_dialog, zoom_params)
    elif apply_fade and fade_params.get("active", False):
        animation = fade_dialog(confirm_delete_dialog, fade_params)
    elif apply_scale_fade and scale_fade_params.get("active", False):
        animation = scale_fade_dialog(confirm_delete_dialog, scale_fade_params)

    # Start the animation if available
    if animation:
        if isinstance(animation, tuple):  # For animations returning multiple animations
            for anim in animation:
                anim.start()
        else:
            animation.start()

    # Show the dialog (exec blocks until the user closes the dialog)
    return confirm_delete_dialog.exec() == QDialog.Accepted

# Function to show a QDialog with animation
def animation_dialog_Window(parent, dialog_class):
    """
    Apply animation to the dialog and display it.
    :param parent: The parent widget for the dialog.
    :param dialog_class: The dialog class to be instantiated and animated.
    """
    # Instantiate the dialog
    dialog = dialog_class(parent)
    dialog.setWindowModality(Qt.ApplicationModal) # Block input to other windows
    dialog.setModal(True)  # Make the dialog modal
    
    # Load animation parameters from QDialog.json
    slide_params = next((p for p in qdialog_animation_params["slide"] if p.get("active", True)), {})
    bounce_params = next((p for p in qdialog_animation_params["bounce"] if p.get("active", True)), {})
    zoom_params = next((p for p in qdialog_animation_params["zoom"] if p.get("active", True)), {})
    fade_params = next((p for p in qdialog_animation_params["fade"] if p.get("active", True)), {})
    scale_fade_params = next((p for p in qdialog_animation_params["scale_fade"] if p.get("active", True)), {})

    # Control flags for animation activation
    apply_slide = False # Adjust as needed
    apply_bounce = False
    apply_zoom = False # Example: Enable zoom animation
    apply_fade = False
    apply_scale_fade = True

    # Determine the animation to apply
    animation = None
    parent_geometry = parent.geometry()  # For reference in some animations

    if apply_slide and slide_params.get("active", False):
        animation = slide_dialog_Window(dialog, slide_params)
    elif apply_bounce and bounce_params.get("active", False):
        animation = bounce_dialog(dialog, bounce_params, parent_geometry)
    elif apply_zoom and zoom_params.get("active", False):
        animation = zoom_dialog(dialog, zoom_params)
    elif apply_fade and fade_params.get("active", False):
        animation = fade_dialog(dialog, fade_params)
    elif apply_scale_fade and scale_fade_params.get("active", False):
        animation = scale_fade_dialog(dialog, scale_fade_params)

    # Start the animation if available
    if animation:
        if isinstance(animation, tuple):  # Handle multiple animations (e.g., zoom)
            for anim in animation:
                anim.start()
        else:
            animation.start()

    # Show the dialog and block until it’s closed
    dialog.exec()
