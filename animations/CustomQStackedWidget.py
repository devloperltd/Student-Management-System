from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup, QRect, QPoint, QParallelAnimationGroup
from PySide6.QtGui import QTransform  # Import QTransform from PySide6.QtGui
from PySide6.QtWidgets import QGraphicsOpacityEffect, QStackedWidget

# Slide QStackedWidget Transition
# Keep a reference to animations globally to avoid garbage collection
_active_animations = []

def slide_stackedWidget(stacked_widget: QStackedWidget, end_index: int, params: dict):
    """
    Slides the QStackedWidget to the specified page index with animation.

    :param stacked_widget: QStackedWidget instance
    :param end_index: Index of the target page to switch to
    :param params: Dictionary of animation parameters
    """
    if not params.get('active', True):
        stacked_widget.setCurrentIndex(end_index)
        return

    duration = params.get('duration', 500)
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutQuad'))

    current_index = stacked_widget.currentIndex()
    if current_index == end_index:
        return  # No animation needed if the target is the current page

    current_widget = stacked_widget.widget(current_index)
    next_widget = stacked_widget.widget(end_index)

    # Prepare the direction
    direction = params.get('direction', 'right')  # Default to right
    width = stacked_widget.width()
    height = stacked_widget.height()

    # Determine positions based on the direction
    if direction == 'right':
        next_start_pos = QRect(width, 0, width, height)
        current_end_pos = QRect(-width, 0, width, height)
    elif direction == 'left':
        next_start_pos = QRect(-width, 0, width, height)
        current_end_pos = QRect(width, 0, width, height)
    elif direction == 'top':
        next_start_pos = QRect(0, -height, width, height)
        current_end_pos = QRect(0, height, width, height)
    elif direction == 'bottom':
        next_start_pos = QRect(0, height, width, height)
        current_end_pos = QRect(0, -height, width, height)
    else:
        raise ValueError(f"Unsupported direction: {direction}")

    # Set up initial geometry for the next widget
    next_widget.setGeometry(next_start_pos)
    next_widget.show()

    # Create animations
    current_animation = QPropertyAnimation(current_widget, b"geometry")
    current_animation.setDuration(duration)
    current_animation.setEasingCurve(easing_curve)
    current_animation.setEndValue(current_end_pos)

    next_animation = QPropertyAnimation(next_widget, b"geometry")
    next_animation.setDuration(duration)
    next_animation.setEasingCurve(easing_curve)
    next_animation.setEndValue(QRect(0, 0, width, height))

    # Group animations to run in parallel
    animation_group = QParallelAnimationGroup()
    animation_group.addAnimation(current_animation)
    animation_group.addAnimation(next_animation)

    # Update the current index after animation completes
    def on_animation_finished():
        stacked_widget.setCurrentIndex(end_index)
        current_widget.hide()  # Hide the previous widget after animation
        _active_animations.remove(animation_group)  # Clean up reference

    animation_group.finished.connect(on_animation_finished)
    _active_animations.append(animation_group)  # Store reference
    animation_group.start()

# Fade QStackedWidget Transition
def fade_stackedWidget(stacked_widget: QStackedWidget, start_index: int, end_index: int, params: dict):
    if not params.get('active', True):
        # If animation is disabled, switch immediately
        stacked_widget.setCurrentIndex(end_index)
        return

    duration = params.get('duration', 500)
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutQuad'))

    current_widget = stacked_widget.widget(start_index)
    next_widget = stacked_widget.widget(end_index)

    if not current_widget or not next_widget:
        print("Invalid widget references")
        return

    # Apply opacity effects
    current_effect = QGraphicsOpacityEffect(current_widget)
    next_effect = QGraphicsOpacityEffect(next_widget)
    current_widget.setGraphicsEffect(current_effect)
    next_widget.setGraphicsEffect(next_effect)

    # Initialize opacity
    next_effect.setOpacity(0.0)
    next_widget.setVisible(True)

    # Fade-out animation for the current widget
    fade_out = QPropertyAnimation(current_effect, b"opacity")
    fade_out.setDuration(duration)
    fade_out.setStartValue(1.0)
    fade_out.setEndValue(0.0)
    fade_out.setEasingCurve(easing_curve)

    # Fade-in animation for the next widget
    fade_in = QPropertyAnimation(next_effect, b"opacity")
    fade_in.setDuration(duration)
    fade_in.setStartValue(0.0)
    fade_in.setEndValue(1.0)
    fade_in.setEasingCurve(easing_curve)

    # Sequential animation group
    animation_group = QSequentialAnimationGroup()
    animation_group.addAnimation(fade_out)
    animation_group.addAnimation(fade_in)

    def on_finished():
        # Switch page and cleanup
        stacked_widget.setCurrentIndex(end_index)
        current_widget.setGraphicsEffect(None)
        next_widget.setGraphicsEffect(None)
        current_widget.setVisible(False)

        # Debugging
        print(f"Fade animation completed: switched to index {end_index}")

    animation_group.finished.connect(on_finished)

    # Attach animation to the stacked widget to avoid garbage collection
    stacked_widget._current_animation = animation_group
    animation_group.start()

# Bounce QStackedWidget Transition
def bounce_stackedWidget(stacked_widget: QStackedWidget, end_index: int, params: dict):
    if not params.get('active', True):
        stacked_widget.setCurrentIndex(end_index)
        return

    duration = params.get('duration', 2000)
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutBounce'))

    next_widget = stacked_widget.widget(end_index)
    stacked_widget.setCurrentIndex(end_index)  # Switch to the target page

    # Ensure the widget remains in place
    parent_geometry = stacked_widget.geometry()
    target_x = parent_geometry.x()
    target_y = parent_geometry.y()

    # Create bounce geometry
    start_geometry = QRect(
        target_x,
        target_y + 20,  # Bounce down by 20 pixels
        parent_geometry.width(),
        parent_geometry.height()
    )
    end_geometry = QRect(
        target_x,
        target_y,
        parent_geometry.width(),
        parent_geometry.height()
    )

    # Bounce animation
    anim = QPropertyAnimation(stacked_widget, b"geometry")
    anim.setDuration(duration)
    anim.setStartValue(start_geometry)
    anim.setEndValue(end_geometry)
    anim.setEasingCurve(easing_curve)

    # Prevent garbage collection
    global _active_animations
    _active_animations.append(anim)

    # Cleanup after animation
    def on_animation_finished():
        _active_animations.remove(anim)

    anim.finished.connect(on_animation_finished)
    anim.start()

# Zoom QStackedWidget Transition
def zoom_stackedWidget(stacked_widget: QStackedWidget, end_index: int, params: dict):
    if not params.get('active', True):
        stacked_widget.setCurrentIndex(end_index)
        return

    duration = params.get('duration', 600)
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutQuad'))

    next_widget = stacked_widget.widget(end_index)
    stacked_widget.setCurrentIndex(end_index)

    # Set initial size and ensure visibility
    next_widget.setGeometry(0, 0, stacked_widget.width(), stacked_widget.height())
    next_widget.setVisible(True)

    # Zoom animation
    anim = QPropertyAnimation(next_widget, b"geometry")
    anim.setDuration(duration)
    anim.setStartValue(QRect(
        stacked_widget.width() // 2,
        stacked_widget.height() // 2,
        0,
        0
    ))
    anim.setEndValue(QRect(
        0,
        0,
        stacked_widget.width(),
        stacked_widget.height()
    ))
    anim.setEasingCurve(easing_curve)

    # Prevent garbage collection
    global _active_animations
    _active_animations.append(anim)

    # Remove animation from global list when finished
    def on_animation_finished():
        _active_animations.remove(anim)

    anim.finished.connect(on_animation_finished)
    anim.start()

# Scale Fade QStackedWidget Transition
def scale_fade_stackedWidget(stacked_widget: QStackedWidget, start_index: int, end_index: int, params: dict):
    if not params.get('active', True):
        stacked_widget.setCurrentIndex(end_index)
        return

    duration = params.get('duration', 1000)
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutBack'))

    current_widget = stacked_widget.widget(start_index)
    next_widget = stacked_widget.widget(end_index)

    if start_index == end_index:
        return  # No animation needed if the target is the same page

    # Add opacity effects
    current_opacity_effect = QGraphicsOpacityEffect(current_widget)
    current_widget.setGraphicsEffect(current_opacity_effect)
    next_opacity_effect = QGraphicsOpacityEffect(next_widget)
    next_widget.setGraphicsEffect(next_opacity_effect)

    # Fade animations
    fade_out = QPropertyAnimation(current_opacity_effect, b"opacity")
    fade_out.setDuration(duration)
    fade_out.setStartValue(1)
    fade_out.setEndValue(0)
    fade_out.setEasingCurve(easing_curve)

    fade_in = QPropertyAnimation(next_opacity_effect, b"opacity")
    fade_in.setDuration(duration)
    fade_in.setStartValue(0)
    fade_in.setEndValue(1)
    fade_in.setEasingCurve(easing_curve)

    # Scale animation
    start_geometry = QRect(
        stacked_widget.width() // 4,
        stacked_widget.height() // 4,
        stacked_widget.width() // 2,
        stacked_widget.height() // 2
    )
    end_geometry = QRect(0, 0, stacked_widget.width(), stacked_widget.height())
    print(f"Start geometry: {start_geometry}, End geometry: {end_geometry}")  # Debug

    scale_animation = QPropertyAnimation(next_widget, b"geometry")
    scale_animation.setDuration(duration)
    scale_animation.setStartValue(start_geometry)
    scale_animation.setEndValue(end_geometry)
    scale_animation.setEasingCurve(QEasingCurve.InOutBounce)

    # Group animations
    animation_group = QParallelAnimationGroup()
    animation_group.addAnimation(fade_out)
    animation_group.addAnimation(fade_in)
    animation_group.addAnimation(scale_animation)

    # Switch page after animation
    animation_group.finished.connect(lambda: stacked_widget.setCurrentIndex(end_index))
    
    # Prevent garbage collection
    _active_animations.append(animation_group)

    print("Starting enhanced scale_fade animation")  # Debugging line
    animation_group.start()

# Swipe QStackedWidget Transition
def swipe_stackedWidget(stacked_widget: QStackedWidget, start_index: int, end_index: int, params: dict):
    if not params.get('active', True):
        stacked_widget.setCurrentIndex(end_index)
        return

    duration = params.get('duration', 700)
    direction = params.get('direction', 'horizontal')
    easing_curve = getattr(QEasingCurve, params.get('easingCurve', 'OutBack'))

    # Get widgets
    current_widget = stacked_widget.widget(start_index)
    next_widget = stacked_widget.widget(end_index)

    if start_index == end_index:
        return

    # Calculate distances
    distance = stacked_widget.width() if direction == "horizontal" else stacked_widget.height()
    offset = -distance if end_index < start_index else distance

    if direction == "horizontal":
        current_end_pos = QPoint(-offset, 0)
        next_start_pos = QPoint(offset, 0)
    else:  # vertical
        current_end_pos = QPoint(0, -offset)
        next_start_pos = QPoint(0, offset)

    next_widget.move(next_start_pos)
    current_widget.setVisible(True)
    next_widget.setVisible(True)

    # Create animations
    current_animation = QPropertyAnimation(current_widget, b"pos")
    current_animation.setDuration(duration)
    current_animation.setEasingCurve(easing_curve)
    current_animation.setEndValue(current_end_pos)

    next_animation = QPropertyAnimation(next_widget, b"pos")
    next_animation.setDuration(duration)
    next_animation.setEasingCurve(easing_curve)
    next_animation.setEndValue(QPoint(0, 0))

    # Group animations
    animation_group = QParallelAnimationGroup()
    animation_group.addAnimation(current_animation)
    animation_group.addAnimation(next_animation)

    # Update index after animation
    animation_group.finished.connect(lambda: stacked_widget.setCurrentIndex(end_index))
    animation_group.finished.connect(lambda: _active_animations.remove(animation_group))
    
    global _active_animations
    _active_animations.append(animation_group)
    animation_group.start()