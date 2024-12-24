from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtWidgets import QGraphicsOpacityEffect, QDialog

# Slide Transition for QDialog
def slide_msg_dialog(dialog: QDialog, params: dict, top_margin=30, side_margin=30, bottom_margin=60):
    if not params.get('active', True):
        print("Animation is inactive in the configuration.")
        return None

    # Animation parameters
    speed = params.get('speed', 500)
    direction = params.get('direction', 'right-to-left')  # Default direction
    easing_curve = QEasingCurve.OutBack

    # Get screen geometry for positioning
    screen_geometry = dialog.screen().geometry()
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    # Calculate start and end positions based on direction
    if direction == 'right-to-left':
        start_x = screen_geometry.width()
        end_x = screen_geometry.width() - dialog.width() - side_margin
        start_y = end_y = top_margin
    elif direction == 'left-to-right':
        start_x = -dialog.width()
        end_x = side_margin
        start_y = end_y = top_margin
    elif direction == 'top-to-bottom':
        start_x = end_x = side_margin
        start_y = -dialog.height()
        end_y = top_margin
    elif direction == 'bottom-to-top':
        start_x = end_x = side_margin
        start_y = screen_geometry.height()
        end_y = screen_geometry.height() - dialog.height() - bottom_margin  # Use bottom margin
    else:
        print(f"Unknown direction '{direction}' in animation configuration.")
        return None

    # Set initial geometry for the dialog based on start position
    dialog.setGeometry(start_x, start_y, dialog.width(), dialog.height())

    # Create geometry animation
    animation = QPropertyAnimation(dialog, b"geometry")
    animation.setDuration(speed)
    animation.setStartValue(QRect(start_x, start_y, dialog.width(), dialog.height()))
    animation.setEndValue(QRect(end_x, end_y, dialog.width(), dialog.height()))
    animation.setEasingCurve(easing_curve)

    # Show the dialog and start the animation
    dialog.show()
    animation.start()

    return animation

# Slide out animation for QDialog
def slide_out_msg_dialog(dialog: QDialog, params: dict, top_margin=30, side_margin=30, bottom_margin=60):
    # Animation parameters
    speed = params.get('speed', 500)
    direction = params.get('direction', 'right-to-left')  # Default direction
    easing_curve = QEasingCurve.InBack  # Use an easing curve for sliding out

    # Get screen geometry for positioning
    screen_geometry = dialog.screen().geometry()
    start_x, start_y = dialog.x(), dialog.y()
    end_x, end_y = start_x, start_y

    # Calculate the end position for slide out based on direction and margins
    if direction == 'right-to-left':
        end_x = screen_geometry.width() + side_margin
    elif direction == 'left-to-right':
        end_x = -dialog.width() - side_margin
    elif direction == 'top-to-bottom':
        end_y = screen_geometry.height() + bottom_margin
    elif direction == 'bottom-to-top':
        end_y = -dialog.height() - top_margin
    else:
        print(f"Unknown direction '{direction}' in animation configuration.")
        return None

    # Create geometry animation for sliding out
    animation = QPropertyAnimation(dialog, b"geometry")
    animation.setDuration(speed)
    animation.setStartValue(QRect(start_x, start_y, dialog.width(), dialog.height()))
    animation.setEndValue(QRect(end_x, end_y, dialog.width(), dialog.height()))
    animation.setEasingCurve(easing_curve)

    # Close the dialog after the animation finishes
    animation.finished.connect(dialog.close)
    animation.start()

    return animation  # Return the animation instance

# Fade Transition for QDialog
def fade_dialog(dialog: QDialog, params: dict):
    if not params.get('active', True):
        return None
    
    duration = params.get('duration', 500)
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutQuad'))

    # Apply opacity effect
    opacity_effect = QGraphicsOpacityEffect(dialog)
    dialog.setGraphicsEffect(opacity_effect)

    opacity_animation = QPropertyAnimation(opacity_effect, b"opacity")
    opacity_animation.setDuration(duration)
    opacity_animation.setStartValue(0)  # Start from fully transparent
    opacity_animation.setEndValue(1)  # Fade to fully opaque
    opacity_animation.setEasingCurve(easing_curve)

    return opacity_animation

# Bounce Transition for QDialog
def bounce_dialog(dialog: QDialog, params: dict, parent_geometry: QRect):
    if not params.get('active', True):
        return None

    # Set animation duration and easing curve
    duration = params.get('duration', 500)
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutBounce'), QEasingCurve.OutBounce)

    # Dynamically calculate the start and end positions for centering
    dialog_width = dialog.width()
    dialog_height = dialog.height()
    parent_center_x = parent_geometry.x() + parent_geometry.width() // 2
    parent_center_y = parent_geometry.y() + parent_geometry.height() // 2

    start_y = parent_center_y - (dialog_height // 2) - dialog_height  # Start position is above center
    end_y = parent_center_y - (dialog_height // 2)  # End position is vertically centered

    start_x = parent_center_x - (dialog_width // 2)  # Horizontally centered
    end_x = start_x

    # Set start and end rectangles for the animation
    start_rect = QRect(start_x, start_y, dialog_width, dialog_height)
    end_rect = QRect(end_x, end_y, dialog_width, dialog_height)

    # Set dialog to the starting geometry
    dialog.setGeometry(start_rect)

    # Configure and start the bounce animation
    animation = QPropertyAnimation(dialog, b"geometry")
    animation.setDuration(duration)
    animation.setEasingCurve(easing_curve)
    animation.setStartValue(start_rect)
    animation.setEndValue(end_rect)

    return animation

# Zoom Transition for QDialog
def zoom_dialog(dialog: QDialog, params: dict):
    if not params.get("active", True):
        return None

    # Extract animation parameters
    duration = params.get("duration", 600)
    easing_curve = getattr(QEasingCurve, params.get("easingCurve", "OutQuad"))

    # Get the final size of the dialog
    final_width = dialog.width()
    final_height = dialog.height()

    # Calculate the center position of the dialog on the parent or screen
    parent = dialog.parent()
    if parent:
        # Use parent geometry and adjust for the dialog size
        parent_geometry = parent.geometry()  # Use client area geometry
        center_x = parent_geometry.x() + parent_geometry.width() // 2
        center_y = parent_geometry.y() + parent_geometry.height() // 2
    else:
        # Default to screen center
        screen_geometry = dialog.screen().availableGeometry()
        center_x = screen_geometry.center().x()
        center_y = screen_geometry.center().y()

    # Define start and end geometries for the animation
    start_geometry = QRect(center_x, center_y, 0, 0)  # Start as a point at the center
    end_geometry = QRect(
        center_x - final_width // 2,
        center_y - final_height // 2,
        final_width,
        final_height,
    )  # Expand to the final size from the center

    # Set the initial geometry and visibility
    dialog.setGeometry(end_geometry)  # Ensure final position is correct
    dialog.show()

    # Create the geometry animation (for expansion)
    geometry_animation = QPropertyAnimation(dialog, b"geometry")
    geometry_animation.setDuration(duration)
    geometry_animation.setStartValue(start_geometry)
    geometry_animation.setEndValue(end_geometry)
    geometry_animation.setEasingCurve(easing_curve)

    # Start the animation
    geometry_animation.start()

    return geometry_animation


# Scale Fade Transition for QDialog
def scale_fade_dialog(dialog: QDialog, params: dict):
    if not params.get("active", True):
        return None

    # Extract animation parameters
    duration = params.get("duration", 1000)
    easing_curve = getattr(QEasingCurve, params.get("easingCurve", "OutBack"))

    # Calculate the final geometry of the dialog
    final_geometry = dialog.geometry()
    parent = dialog.parent()

    if parent:
        parent_geometry = parent.geometry()
        center_x = parent_geometry.x() + parent_geometry.width() // 2
        center_y = parent_geometry.y() + parent_geometry.height() // 2
    else:
        screen_geometry = dialog.screen().availableGeometry()
        center_x = screen_geometry.x() + screen_geometry.width() // 2
        center_y = screen_geometry.y() + screen_geometry.height() // 2

    final_x = center_x - final_geometry.width() // 2
    final_y = center_y - final_geometry.height() // 2
    final_geometry.moveTo(final_x, final_y)

    # Set the starting geometry to the right off-screen
    start_x = parent_geometry.right() if parent else screen_geometry.right()
    start_y = center_y - final_geometry.height() // 2
    start_geometry = QRect(start_x, start_y, final_geometry.width(), final_geometry.height())

    # Set the initial geometry and show the dialog
    dialog.setGeometry(start_geometry)
    dialog.show()

    # Scaling animation
    move_animation = QPropertyAnimation(dialog, b"geometry")
    move_animation.setDuration(duration)
    move_animation.setStartValue(start_geometry)
    move_animation.setEndValue(final_geometry)
    move_animation.setEasingCurve(easing_curve)

    # Apply opacity effect
    opacity_effect = QGraphicsOpacityEffect(dialog)
    dialog.setGraphicsEffect(opacity_effect)
    opacity_animation = QPropertyAnimation(opacity_effect, b"opacity")
    opacity_animation.setDuration(duration)
    opacity_animation.setStartValue(0)
    opacity_animation.setEndValue(1)
    opacity_animation.setEasingCurve(easing_curve)

    return move_animation, opacity_animation


# Swipe Transition (not applicable for QDialog since it doesn't use stacked widgets)
# You may skip it or modify it based on how you want to implement swipe behavior.


# Slide Transition for QDialog Window
def slide_dialog_Window(dialog: QDialog, params: dict):
    if not params.get('active', True):
        print("Animation is inactive in the configuration.")
        return None

    # Animation parameters
    speed = params.get('speed', 500)
    direction = params.get('direction', 'right-to-left')  # Default direction: right-to-left
    easing_curve = QEasingCurve.OutBack

    # Get parent geometry for centering
    parent = dialog.parent()
    if parent:
        parent_geometry = parent.geometry()
    else:
        parent_geometry = dialog.screen().geometry()

    dialog_width = dialog.width()
    dialog_height = dialog.height()

    # Calculate center positions
    center_x = parent_geometry.x() + (parent_geometry.width() - dialog_width) // 2
    center_y = parent_geometry.y() + (parent_geometry.height() - dialog_height) // 2

    # Determine the starting position based on direction
    if direction == 'right-to-left':
        start_x = parent_geometry.width()  # Start from the right outside
        start_y = center_y  # Slide horizontally
    elif direction == 'left-to-right':
        start_x = -dialog_width  # Start from the left outside
        start_y = center_y
    elif direction == 'top-to-bottom':
        start_x = center_x  # Slide vertically from the top
        start_y = -dialog_height
    elif direction == 'bottom-to-top':
        start_x = center_x  # Slide vertically from the bottom
        start_y = parent_geometry.height() + dialog_height
    else:
        print(f"Unknown direction '{direction}' in animation configuration.")
        return None

    # Set the initial position of the dialog
    dialog.setGeometry(start_x, start_y, dialog_width, dialog_height)

    # Create geometry animation
    animation = QPropertyAnimation(dialog, b"geometry")
    animation.setDuration(speed)
    animation.setStartValue(QRect(start_x, start_y, dialog_width, dialog_height))
    animation.setEndValue(QRect(center_x, center_y, dialog_width, dialog_height))
    animation.setEasingCurve(easing_curve)

    # Show and start the animation
    dialog.show()
    animation.start()

    return animation

# Slide out animation for QDialog Window
def slide_out_dialog_Window(dialog: QDialog, params: dict, top_margin=30, side_margin=30, bottom_margin=60):
    # Animation parameters
    speed = params.get('speed', 500)
    direction = params.get('direction', 'right-to-left')  # Default direction
    easing_curve = QEasingCurve.InBack  # Use an easing curve for sliding out

    # Get screen geometry for positioning
    screen_geometry = dialog.screen().geometry()
    start_x, start_y = dialog.x(), dialog.y()
    end_x, end_y = start_x, start_y

    # Calculate the end position for slide out based on direction and margins
    if direction == 'right-to-left':
        end_x = screen_geometry.width() + side_margin
    elif direction == 'left-to-right':
        end_x = -dialog.width() - side_margin
    elif direction == 'top-to-bottom':
        end_y = screen_geometry.height() + bottom_margin
    elif direction == 'bottom-to-top':
        end_y = -dialog.height() - top_margin
    else:
        print(f"Unknown direction '{direction}' in animation configuration.")
        return None

    # Create geometry animation for sliding out
    animation = QPropertyAnimation(dialog, b"geometry")
    animation.setDuration(speed)
    animation.setStartValue(QRect(start_x, start_y, dialog.width(), dialog.height()))
    animation.setEndValue(QRect(end_x, end_y, dialog.width(), dialog.height()))
    animation.setEasingCurve(easing_curve)

    # Close the dialog after the animation finishes
    animation.finished.connect(dialog.close)
    animation.start()

    return animation  # Return the animation instance
