"""
Music Theory Academy — Main Menu Screen (Responsive)
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp, sp

from styles import MenuBtn, SectionHeader, ResponsiveGrid


class MainMenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))

        hdr = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(74), spacing=dp(2))
        hdr.add_widget(Label(text='🎵  Music Theory Academy', font_size=sp(28), bold=True, color=(1, .85, .2, 1)))
        hdr.add_widget(Label(text='Western  •  Eastern  •  Jazz  •  Modern', font_size=sp(13), color=(.55, .55, .65, 1)))
        ly.add_widget(hdr)

        sv = ScrollView()
        body = GridLayout(cols=1, spacing=dp(14), size_hint_y=None, padding=dp(2))
        body.bind(minimum_height=body.setter('height'))

        # Reference
        body.add_widget(SectionHeader(text='   📖  Reference'))
        ref_grid = ResponsiveGrid(min_col_width=dp(230), spacing=dp(6), size_hint_y=None)
        ref_grid.bind(minimum_height=ref_grid.setter('height'))
        for txt, scr, clr in [
            ('🎼  Western Theory',  'western_ref', (.12, .30, .55, 1)),
            ('🕌  Eastern Theory',   'eastern_ref', (.50, .28, .10, 1)),
            ('🎷  Jazz Theory',      'jazz_ref',    (.40, .12, .50, 1)),
            ('🎸  Pop & Blues Theory', 'pop_rock_ref', (.55, .20, .25, 1)),
            ('🔮  Modern & Orchestration', 'modern_ref', (.35, .15, .45, 1)),
        ]:
            b = MenuBtn(text=txt, mcolor=clr)
            b.bind(on_release=lambda x, s=scr: setattr(self.manager, 'current', s))
            ref_grid.add_widget(b)
        body.add_widget(ref_grid)

        # Visual Quizzes
        body.add_widget(SectionHeader(text='   🎮  Visual Quizzes'))
        quiz_grid = ResponsiveGrid(min_col_width=dp(210), spacing=dp(6), size_hint_y=None)
        quiz_grid.bind(minimum_height=quiz_grid.setter('height'))
        for txt, scr, clr in [
            ('🎮  Interval Quiz',      'interval_quiz', (.15, .45, .30, 1)),
            ('🎯  Scale Quiz',         'scale_quiz',    (.20, .40, .55, 1)),
            ('🎸  Chord Quiz',         'chord_quiz',    (.55, .25, .15, 1)),
            ('🎵  Diatonic Chord Quiz','diatonic_quiz', (.25, .35, .45, 1)),
            ('🏛️  Cadence Quiz',       'cadence_quiz',  (.40, .40, .25, 1)),
            ('🔮  Raga & Maqam Quiz',  'eastern_quiz',  (.55, .35, .10, 1)),
            ('🎺  Jazz Chord Quiz',    'jazz_quiz',     (.45, .15, .50, 1)),
            ('📝  Key Signature Quiz',  'keysig_quiz',   (.35, .35, .20, 1)),
            ('🥁  Rhythm & Meter Quiz', 'rhythm_quiz',  (.30, .20, .45, 1)),
        ]:
            b = MenuBtn(text=txt, mcolor=clr)
            b.bind(on_release=lambda x, s=scr: setattr(self.manager, 'current', s))
            quiz_grid.add_widget(b)
        body.add_widget(quiz_grid)

        # Ear Training
        body.add_widget(SectionHeader(text='   🎧  Ear Training (Audio)'))
        ear_grid = ResponsiveGrid(min_col_width=dp(220), spacing=dp(6), size_hint_y=None)
        ear_grid.bind(minimum_height=ear_grid.setter('height'))
        for txt, scr, clr in [
            ('🔊  Ear Interval Quiz',  'ear_interval_quiz',  (.12, .50, .42, 1)),
            ('🔊  Ear Chord Quiz',     'ear_chord_quiz',     (.15, .45, .38, 1)),
            ('🔊  Ear Scale Quiz',     'ear_scale_quiz',     (.18, .40, .34, 1)),
            ('🔊  Ear Diatonic Quiz',  'ear_diatonic_quiz',  (.10, .48, .38, 1)),
            ('🔊  Ear Cadence Quiz',   'ear_cadence_quiz',   (.14, .52, .40, 1)),
        ]:
            b = MenuBtn(text=txt, mcolor=clr)
            b.bind(on_release=lambda x, s=scr: setattr(self.manager, 'current', s))
            ear_grid.add_widget(b)
        body.add_widget(ear_grid)

        # Tools
        body.add_widget(SectionHeader(text='   🛠️  Tools'))
        tool_grid = ResponsiveGrid(min_col_width=dp(230), spacing=dp(6), size_hint_y=None)
        tool_grid.bind(minimum_height=tool_grid.setter('height'))
        for txt, scr, clr in [
            ('🎹  Scale Builder',     'scale_builder', (.25, .30, .55, 1)),
            ('⭕  Circle of Fifths', 'circle',        (.15, .40, .40, 1)),
        ]:
            b = MenuBtn(text=txt, mcolor=clr)
            b.bind(on_release=lambda x, s=scr: setattr(self.manager, 'current', s))
            tool_grid.add_widget(b)
        body.add_widget(tool_grid)

        sv.add_widget(body)
        ly.add_widget(sv)
        self.add_widget(ly)