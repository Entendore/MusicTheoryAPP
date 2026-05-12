"""
Music Theory Academy — Tool Screens
Scale Builder & Circle of Fifths
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.metrics import dp, sp

from styles import BackBtn, AccentBtn, Btn
from data import NOTE_NAMES, CIRCLE_FIFTHS, KEY_SIGNATURES
from helpers import all_scales, scale_notes


# ─── Scale Builder ────────────────────────────────────────────

class ScaleBuilderScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.scale_dict = all_scales()
        self.scale_names = sorted(self.scale_dict.keys())
        
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))
        
        # Header
        hd = BoxLayout(size_hint_y=None, height=dp(42), spacing=dp(8))
        bb = BackBtn(text='← Back')
        bb.bind(on_release=lambda x: setattr(self.manager, 'current', 'main_menu'))
        hd.add_widget(bb)
        hd.add_widget(Label(text='🎹 Scale Builder', font_size=sp(22), bold=True,
                            color=(1, .85, .2, 1)))
        ly.add_widget(hd)

        # Controls (Spinners)
        ctrl = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        
        self.root_spinner = Spinner(
            text='C', values=NOTE_NAMES, size_hint_x=0.3,
            background_color=(.15, .15, .22, 1), color=(1, 1, 1, 1),
            font_size=sp(16))
        self.scale_spinner = Spinner(
            text='Major', values=self.scale_names, size_hint_x=0.7,
            background_color=(.15, .15, .22, 1), color=(1, 1, 1, 1),
            font_size=sp(16))
        
        ctrl.add_widget(self.root_spinner)
        ctrl.add_widget(self.scale_spinner)
        ly.add_widget(ctrl)

        # Result Title Label
        self.result_lbl = Label(text='', font_size=sp(24), bold=True,
                                color=(1, .85, .2, 1), size_hint_y=None, height=dp(60))
        ly.add_widget(self.result_lbl)

        # Result Info Label
        self.info_lbl = Label(text='', font_size=sp(16), color=(.88, .88, .88, 1),
                              halign='center', valign='middle')
        self.info_lbl.bind(size=self.info_lbl.setter('text_size'))
        ly.add_widget(self.info_lbl)

        # Build Button
        btn = AccentBtn(text='Build Scale', size_hint_y=None, height=dp(46))
        btn.bind(on_release=self.update_scale)
        ly.add_widget(btn)

        self.add_widget(ly)
        
        # Auto-update when spinners change
        self.root_spinner.bind(text=self.update_scale)
        self.scale_spinner.bind(text=self.update_scale)
        self.update_scale()

    def update_scale(self, *args):
        root_name = self.root_spinner.text
        scale_name = self.scale_spinner.text
        
        if not root_name or not scale_name:
            return
            
        root_idx = NOTE_NAMES.index(root_name)
        formula = self.scale_dict.get(scale_name, [])
        
        if not formula:
            self.result_lbl.text = 'Scale not found'
            self.info_lbl.text = ''
            return
            
        notes = scale_notes(root_idx, formula)
        self.result_lbl.text = f'{root_name} {scale_name}'
        self.info_lbl.text = f'Notes:  {" - ".join(notes)}\n\nFormula:  {", ".join(str(x) for x in formula)}'


# ─── Circle of Fifths ─────────────────────────────────────────

class CircleScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))
        
        # Header
        hd = BoxLayout(size_hint_y=None, height=dp(42), spacing=dp(8))
        bb = BackBtn(text='← Back')
        bb.bind(on_release=lambda x: setattr(self.manager, 'current', 'main_menu'))
        hd.add_widget(bb)
        hd.add_widget(Label(text='⭕ Circle of Fifths', font_size=sp(22), bold=True,
                            color=(1, .85, .2, 1)))
        ly.add_widget(hd)

        sv = ScrollView()
        gl = GridLayout(cols=1, spacing=dp(8), size_hint_y=None, padding=dp(4))
        gl.bind(minimum_height=gl.setter('height'))

        gl.add_widget(Label(text='The Circle of Fifths arranges the 12 chromatic tones\n'
                                 'by perfect fifths. Each step adds a sharp (right)\n'
                                 'or a flat (left).',
                            font_size=sp(14), color=(.88, .88, .88, 1),
                            size_hint_y=None, height=dp(60)))

        # Circle Grid Layout (4x3)
        circle_gl = GridLayout(cols=4, spacing=dp(5), size_hint_y=None)
        circle_gl.bind(minimum_height=circle_gl.setter('height'))
        
        # Arranged to visually loop around
        order_4x3 = [
            'C', 'G', 'D', 'A',
            'E', 'B', 'F#', 'Db',
            'Ab', 'Eb', 'Bb', 'F'
        ]
        
        for note in order_4x3:
            sig = KEY_SIGNATURES.get(note, 0)
            sig_text = f'{sig} #' if sig > 0 else f'{abs(sig)} b' if sig < 0 else '0'
            lbl = Btn(text=f'{note}\n({sig_text})')
            circle_gl.add_widget(lbl)

        gl.add_widget(circle_gl)
        gl.add_widget(Label(text='', size_hint_y=None, height=dp(12))) # Spacer

        # Info Rules
        info_data = [
            '→  Clockwise: adds one sharp per step',
            '←  Counter-clockwise: adds one flat per step',
            'Minor keys: relative minor is a minor 3rd below its major key',
            'V7 Resolution: dominant 7th chords resolve clockwise to the I chord',
        ]
        for info in info_data:
            lbl = Label(text=info, font_size=sp(14), color=(.88, .88, .88, 1),
                        size_hint_y=None, height=dp(28), halign='left', valign='middle')
            lbl.bind(width=lambda i, v: setattr(i, 'text_size', (v, None)))
            gl.add_widget(lbl)

        sv.add_widget(gl)
        ly.add_widget(sv)
        self.add_widget(ly)