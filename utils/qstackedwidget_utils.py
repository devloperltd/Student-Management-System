import os
import json
from animations.CustomQStackedWidget import *


# Define the path for QStackedWidget.json relative to CustomQStackedWidget.py
qstackedwidget_json_path = os.path.join(os.path.dirname(__file__), '..', 'Json', 'QStackedWidget.json')
with open(qstackedwidget_json_path, 'r') as file:
    qstackedwidget_animation_params = json.load(file)
# Debugging: Print the loaded animation parameters
# print(f"Loaded animation parameters: {qstackedwidget_animation_params}")

def switch_to_slide_page(stacked_widget, index, direction="right"):
    """
    Switches the QStackedWidget to the given page index with animation.

    :param stacked_widget: QStackedWidget instance
    :param index: Index of the page to switch to
    :param direction: The direction for the animation (right, left, top, bottom)
    """
    animation_params = qstackedwidget_animation_params.get('slide', [{}])[0]
    animation_params['direction'] = direction  # Override direction dynamically
    slide_stackedWidget(stacked_widget, index, animation_params)

def switch_to_fade_page(stacked_widget, index):
    animation_params = qstackedwidget_animation_params.get('fade', [{}])[0]
    fade_stackedWidget(stacked_widget, stacked_widget.currentIndex(), index, animation_params)

def switch_to_bounce_page(stacked_widget, index):
    animation_params = qstackedwidget_animation_params.get('bounce', [{}])[0]
    bounce_stackedWidget(stacked_widget, index, animation_params)

def switch_to_zoom_page(stacked_widget, index):
    animation_params = qstackedwidget_animation_params.get('zoom', [{}])[0]
    zoom_stackedWidget(stacked_widget, index, animation_params)

def switch_to_scale_fade_page(stacked_widget, index):
    animation_params = qstackedwidget_animation_params.get('scale_fade', [{}])[0]
    print(f"Animation params: {animation_params}")  # Debugging line
    scale_fade_stackedWidget(stacked_widget, stacked_widget.currentIndex(), index, animation_params)

def switch_to_swipe_page(stacked_widget, index):
    animation_params = qstackedwidget_animation_params.get('swipe', [{}])[0]
    swipe_stackedWidget(stacked_widget, stacked_widget.currentIndex(), index, animation_params)
