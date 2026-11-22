"""
Music Theory Academy — Ear Training (Sound) Quiz Screens
Interval, Chord, and Scale ear training.
"""
import random

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp, sp

from styles import BackBtn, AccentBtn, PlayBtn, QBtn, ProgressWidget, ResponsiveGrid
from synth import Synth, midi_to_freq
from data import NOTE_NAMES, INTERVALS, CHORD_TYPES
from helpers import all_scales


# ─── Base Sound Quiz Screen ──────────────────────────────────

class BaseSoundQuizScreen:
    """
    Mixin/Override for ear training quizzes.
    Injects a prominent 'Play Sound' button into the layout.
    """
    def _build_ui(self):
        self.ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(8))

        # Header
        hd = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(10))
        bb = BackBtn(text='← Back')
        bb.bind(on_release=lambda x: setattr(self.manager, 'current', 'main_menu'))
        hd.add_widget(bb)
        title_lbl = Label(
            text=f'{self.icon} {self.title}',
            font_size=sp(20), bold=True, color=(1, .85, .2, 1),
            halign='left', valign='middle',
        )
        title_lbl.bind(width=lambda i, v: setattr(i, 'text_size', (v, None)))
        hd.add_widget(title_lbl)
        self.ly.add_widget(hd)

        # Score
        score_row = BoxLayout(size_hint_y=None, height=dp(30), spacing=dp(10))
        self.score_lbl = Label(
            text='0 / 0', font_size=sp(14), bold=True,
            color=(.2, .9, .4, 1), size_hint_x=.25,
        )
        self.progress = ProgressWidget(size_hint_x=.55)
        self.streak_lbl = Label(
            text='🔥 0', font_size=sp(13), bold=True,
            color=(1, .6, .2, 1), size_hint_x=.20,
        )
        score_row.add_widget(self.score_lbl)
        score_row.add_widget(self.progress)
        score_row.add_widget(self.streak_lbl)
        self.ly.add_widget(score_row)

        # Question
        self.q_lbl = Label(
            text='', font_size=sp(22), bold=True,
            color=(1, .85, .2, 1), size_hint_y=None, height=dp(56),
        )
        self.ly.add_widget(self.q_lbl)

        # PLAY SOUND BUTTON
        self.play_btn = PlayBtn(text='🔊 Play Sound', size_hint_y=None, height=dp(54))
        self.play_btn.bind(on_release=lambda x: self._play_audio())
        self.ly.add_widget(self.play_btn)

        # Feedback
        self.fb_lbl = Label(
            text='', font_size=sp(14),
            size_hint_y=None, height=dp(32),
            color=(.88, .88, .88, 1),
        )
        self.ly.add_widget(self.fb_lbl)

        # Answers
        sv = ScrollView()
        self.ans_gl = ResponsiveGrid(
            min_col_width=dp(170), spacing=dp(6), size_hint_y=None,
        )
        self.ans_gl.bind(minimum_height=self.ans_gl.setter('height'))
        sv.add_widget(self.ans_gl)
        self.ly.add_widget(sv)

        # Next
        nxt = AccentBtn(text='Next Question →', size_hint_y=None, height=dp(48))
        nxt.bind(on_release=lambda x: self.new_q())
        self.ly.add_widget(nxt)

        self.add_widget(self.ly)


# ─── Ear Interval Quiz ───────────────────────────────────────

class EarIntervalQuizScreen(BaseSoundQuizScreen):
    from quizzes import BaseQuizScreen
    # Inherit from mixin first, then BaseQuizScreen
    pass

# Proper multiple inheritance setup to avoid duplicating quiz logic
from quizzes import BaseQuizScreen

class EarIntervalQuizScreen(BaseSoundQuizScreen, BaseQuizScreen):
    title = 'Ear Interval Quiz'
    icon  = '🔊'

    def new_q(self):
        self.root_n = random.randint(0, 11)
        self.interval_n = random.randint(1, 12)
        self.q_lbl.text = 'What interval did you hear?'
        self.fb_lbl.text = ''

        correct = INTERVALS[self.interval_n][0]
        self.correct_display = correct
        pool = [INTERVALS[i][0] for i in range(1, 13)]
        choices = self._make_choices(correct, pool)
        self._populate_answers(choices)
        self._play_audio()

    def _play_audio(self):
        root_midi = 60 + self.root_n
        target_midi = root_midi + self.interval_n
        self.synth.play_sequence([midi_to_freq(root_midi), midi_to_freq(target_midi)], duration=0.6)

    def check(self, ans):
        ok = ans == self.correct_display
        self._finish(ok)


class EarChordQuizScreen(BaseSoundQuizScreen, BaseQuizScreen):
    title = 'Ear Chord Quiz'
    icon  = '🔊'

    def new_q(self):
        self.root_n = random.randint(0, 11)
        rn = NOTE_NAMES[self.root_n]
        items = list(CHORD_TYPES.items())
        self.correct_name, self.current_formula = random.choice(items)
        self.q_lbl.text = 'What chord did you hear?'
        self.fb_lbl.text = ''
        self.correct_display = f'{rn} {self.correct_name}'

        pool = list(CHORD_TYPES.keys())
        choices = self._make_choices(self.correct_name, pool)
        self._populate_answers(choices, fmt=lambda c: f'{rn} {c}')
        self._play_audio()

    def _play_audio(self):
        root_midi = 60 + self.root_n
        freqs = [midi_to_freq(root_midi + i) for i in self.current_formula]
        self.synth.play_chord(freqs, duration=1.5)

    def check(self, ans):
        ok = ans == self.correct_name
        self._finish(ok)


class EarScaleQuizScreen(BaseSoundQuizScreen, BaseQuizScreen):
    title = 'Ear Scale Quiz'
    icon  = '🔊'

    def new_q(self):
        self.root_n = random.randint(0, 11)
        rn = NOTE_NAMES[self.root_n]
        all_s = list(all_scales().items())
        self.correct_name, self.current_formula = random.choice(all_s)
        self.q_lbl.text = 'What scale did you hear?'
        self.fb_lbl.text = ''
        self.correct_display = self.correct_name

        pool = list(all_scales().keys())
        choices = self._make_choices(self.correct_name, pool)
        self._populate_answers(choices)
        self._play_audio()

    def _play_audio(self):
        root_midi = 60 + self.root_n
        freqs = [midi_to_freq(root_midi + i) for i in self.current_formula]
        self.synth.play_sequence(freqs, duration=0.35)

    def check(self, ans):
        ok = ans == self.correct_name
        self._finish(ok)