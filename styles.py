"""
Music Theory Academy — Enhanced Styles & Responsive Components
"""
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty, BooleanProperty
from kivy.lang import Builder
from kivy.metrics import dp, sp


Builder.load_string('''

<Btn>:
    font_size: sp(14)
    size_hint_y: None
    height: dp(44)
    background_normal: ''
    background_color: (0,0,0,0)
    color: (0.88, 0.88, 0.88, 1)
    canvas.before:
        Color:
            rgba: (0.25, 0.35, 0.55, 1) if self.state == 'down' else (0.12, 0.12, 0.18, 1)
        RoundedRectangle:
            pos: self.x + dp(1), self.y + dp(1)
            size: self.width - dp(2), self.height - dp(2)
            radius: [8,]

<AccentBtn>:
    font_size: sp(15)
    size_hint_y: None
    height: dp(48)
    background_normal: ''
    background_color: (0,0,0,0)
    color: (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: (0.28, 0.55, 0.92, 1) if self.state == 'down' else (0.20, 0.45, 0.80, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]

<PlayBtn>:
    font_size: sp(16)
    size_hint_y: None
    height: dp(52)
    background_normal: ''
    background_color: (0,0,0,0)
    color: (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: (0.18, 0.62, 0.52, 1) if self.state == 'down' else (0.12, 0.50, 0.42, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]

<BackBtn>:
    font_size: sp(14)
    size_hint: (None, None)
    size: (dp(80), dp(36))
    background_normal: ''
    background_color: (0,0,0,0)
    color: (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: (0.60, 0.20, 0.20, 1) if self.state == 'down' else (0.50, 0.14, 0.14, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [6,]

<MenuBtn>:
    font_size: sp(15)
    size_hint_y: None
    height: dp(52)
    background_normal: ''
    background_color: (0,0,0,0)
    color: (1, 1, 1, 1)
    padding: (dp(16), 0)
    canvas.before:
        Color:
            rgba: self.mcolor
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]

<QBtn>:
    font_size: sp(14)
    size_hint_y: None
    height: dp(46)
    background_normal: ''
    background_color: (0,0,0,0)
    color: (0.88, 0.88, 0.88, 1) if not self.is_correct and not self.is_wrong else (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: (0.15, 0.55, 0.25, 1) if self.is_correct else (0.65, 0.18, 0.18, 1) if self.is_wrong else (0.14, 0.14, 0.20, 1) if self.disabled else (0.18, 0.22, 0.32, 1) if self.state == 'normal' else (0.30, 0.38, 0.55, 1)
        RoundedRectangle:
            pos: self.x + dp(1), self.y + dp(1)
            size: self.width - dp(2), self.height - dp(2)
            radius: [8,]

<SectionHeader>:
    font_size: sp(15)
    bold: True
    color: (1, 0.85, 0.2, 1)
    size_hint_y: None
    height: dp(38)
    halign: 'left'
    valign: 'middle'
    canvas.before:
        Color:
            rgba: (0.13, 0.13, 0.19, 1)
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: (1, 0.85, 0.2, 0.6)
        Rectangle:
            pos: self.x, self.y
            size: dp(4), self.height

<ProgressWidget>:
    size_hint_y: None
    height: dp(14)
    canvas.before:
        Color:
            rgba: (0.15, 0.15, 0.20, 1)
        RoundedRectangle:
            pos: self.x, self.y
            size: self.width, self.height
            radius: [7,]
        Color:
            rgba: (0.2, 0.85, 0.4, 1) if self.ratio > 0.5 else (1, 0.8, 0.2, 1) if self.ratio > 0.25 else (0.9, 0.3, 0.3, 1)
        RoundedRectangle:
            pos: self.x, self.y
            size: max(self.width * self.ratio, dp(4)), self.height
            radius: [7,]

<PianoWhite>:
    background_normal: ''
    background_down: ''
    color: (0, 0, 0, 1)
    canvas.before:
        Color:
            rgba: (0.92, 0.92, 0.95, 1) if self.state == 'normal' else (0.6, 0.8, 1, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    canvas.after:
        Color:
            rgba: (0.7, 0.7, 0.7, 1)
        Line:
            rectangle: (*self.pos, *self.size)

<PianoBlack>:
    background_normal: ''
    background_down: ''
    color: (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: (0.15, 0.15, 0.18, 1) if self.state == 'normal' else (0.4, 0.5, 0.8, 1)
        Rectangle:
            pos: self.pos
            size: self.size
''')


class Btn(Button):
    pass

class AccentBtn(Button):
    pass

class PlayBtn(Button):
    pass

class BackBtn(Button):
    pass

class MenuBtn(Button):
    mcolor = ListProperty((0.15, 0.15, 0.22, 1))

class QBtn(Button):
    is_correct = BooleanProperty(False)
    is_wrong = BooleanProperty(False)

class PianoWhite(ToggleButton):
    pass

class PianoBlack(ToggleButton):
    pass


class SectionHeader(Label):
    """Section header label with left accent bar."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(width=lambda i, v: setattr(i, 'text_size', (v - dp(32), None)))


class ProgressWidget(Widget):
    """Visual progress bar — set .ratio between 0.0 and 1.0."""
    ratio = NumericProperty(0.0)


class ResponsiveGrid(GridLayout):
    """GridLayout that auto-adjusts column count based on its own width."""
    min_col_width = NumericProperty(dp(200))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(width=self._adjust_cols)

    def _adjust_cols(self, inst, width):
        new_cols = max(1, int(width / self.min_col_width))
        new_cols = min(new_cols, 4)
        if new_cols != self.cols:
            self.cols = new_cols