"""
Music Theory Academy — Unified Quiz Screens (Visual & Ear Training)
"""
import random

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp, sp
from kivy.properties import NumericProperty

from styles import BackBtn, AccentBtn, Btn, PlayBtn, QBtn, ProgressWidget, ResponsiveGrid
from synth import Synth, midi_to_freq
from data import (
    NOTE_NAMES, INTERVALS, CHORD_TYPES, JAZZ_CHORDS,
    EASTERN_RAGAS, ARABIC_MAQAMS, PERSIAN_DASTGAH,
    KEY_SIGNATURES, RHYTHM_METER_DATA, 
    DIATONIC_CHORDS_MAJOR, DIATONIC_CHORDS_MINOR, CADENCES
)
from helpers import scale_notes, chord_notes, all_scales


# ─── Base Quiz Screen ─────────────────────────────────────────

class BaseQuizScreen(Screen):
    score  = NumericProperty(0)
    total  = NumericProperty(0)
    streak = NumericProperty(0)

    title  = ''
    icon   = ''
    is_ear_training = False
    has_audio = True

    def __init__(self, **kw):
        super().__init__(**kw)
        self.correct_display = ''
        self.synth = Synth()
        self._build_ui()

    def _build_ui(self):
        self.ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(8))

        # Header row
        hd = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(10))
        bb = BackBtn(text='← Back')
        bb.bind(on_release=lambda x: setattr(self.manager, 'current', 'main_menu'))
        hd.add_widget(bb)
        title_lbl = Label(
            text=f'{self.icon} {self.title}', font_size=sp(20), bold=True, color=(1, .85, .2, 1),
            halign='left', valign='middle',
        )
        title_lbl.bind(width=lambda i, v: setattr(i, 'text_size', (v, None)))
        hd.add_widget(title_lbl)
        self.ly.add_widget(hd)

        # Score + progress row
        score_row = BoxLayout(size_hint_y=None, height=dp(30), spacing=dp(10))
        self.score_lbl = Label(text='0 / 0', font_size=sp(14), bold=True, color=(.2, .9, .4, 1), size_hint_x=.25)
        self.progress = ProgressWidget(size_hint_x=.55)
        self.streak_lbl = Label(text='🔥 0', font_size=sp(13), bold=True, color=(1, .6, .2, 1), size_hint_x=.20)
        score_row.add_widget(self.score_lbl)
        score_row.add_widget(self.progress)
        score_row.add_widget(self.streak_lbl)
        self.ly.add_widget(score_row)

        # Question + Replay
        q_row = BoxLayout(size_hint_y=None, height=dp(72), spacing=dp(8))
        self.q_lbl = Label(text='', font_size=sp(22), bold=True, color=(1, .85, .2, 1))
        q_row.add_widget(self.q_lbl)
        
        if self.has_audio:
            replay_btn = Btn(text='🔊', size_hint=(None, 1), width=dp(50), font_size=sp(22))
            replay_btn.bind(on_release=lambda x: self._play_audio())
            q_row.add_widget(replay_btn)
        self.ly.add_widget(q_row)

        if self.is_ear_training:
            self.play_btn = PlayBtn(text='🔊 Play Sound', size_hint_y=None, height=dp(54))
            self.play_btn.bind(on_release=lambda x: self._play_audio())
            self.ly.add_widget(self.play_btn)

        # Feedback
        self.fb_lbl = Label(text='', font_size=sp(14), size_hint_y=None, height=dp(32), color=(.88, .88, .88, 1))
        self.ly.add_widget(self.fb_lbl)

        # Answers
        sv = ScrollView()
        self.ans_gl = ResponsiveGrid(min_col_width=dp(170), spacing=dp(6), size_hint_y=None)
        self.ans_gl.bind(minimum_height=self.ans_gl.setter('height'))
        sv.add_widget(self.ans_gl)
        self.ly.add_widget(sv)

        # Next
        nxt = AccentBtn(text='Next Question →', size_hint_y=None, height=dp(48))
        nxt.bind(on_release=lambda x: self.new_q())
        self.ly.add_widget(nxt)

        self.add_widget(self.ly)

    def _update_score(self):
        self.score_lbl.text = f'{self.score} / {self.total}'
        self.progress.ratio = self.score / max(self.total, 1)
        self.streak_lbl.text = f'🔥 {self.streak}'

    def _highlight_and_lock(self, correct_text):
        for child in reversed(list(self.ans_gl.children)):
            if isinstance(child, QBtn):
                if child.text == correct_text: child.is_correct = True
                child.disabled = True

    def _make_choices(self, correct, pool, n=4):
        unique_pool = list(set(pool))
        n = min(n, len(unique_pool) + 1)
        choices = [correct]
        safety = 0
        while len(choices) < n and safety < 50:
            c = random.choice(unique_pool)
            if c not in choices: choices.append(c)
            safety += 1
        random.shuffle(choices)
        return choices

    def _populate_answers(self, choices, fmt=None):
        self.ans_gl.clear_widgets()
        for c in choices:
            display = fmt(c) if fmt else c
            b = QBtn(text=display)
            b.bind(on_release=lambda x, ch=c: self.check(ch))
            self.ans_gl.add_widget(b)

    def _finish(self, ok, custom_fb=None):
        self.total += 1
        if ok:
            self.score += 1; self.streak += 1
            self.fb_lbl.text = custom_fb or '✅  Correct!'
            self.fb_lbl.color = (.2, .9, .4, 1)
        else:
            self.streak = 0
            self.fb_lbl.text = custom_fb or f'❌  Answer: {self.correct_display}'
            self.fb_lbl.color = (.9, .25, .25, 1)
        self._update_score()
        self._highlight_and_lock(self.correct_display)

    def new_q(self): raise NotImplementedError
    def _play_audio(self): pass


# ─── Core Quizzes (Unchanged from previous except logic refinement) ───

class IntervalQuizScreen(BaseQuizScreen):
    title = 'Interval Quiz'; icon = '🎮'
    def new_q(self):
        self.root_n = random.randint(0, 11); self.interval_n = random.randint(1, 12)
        rn = NOTE_NAMES[self.root_n]; tn = NOTE_NAMES[(self.root_n + self.interval_n) % 12]
        self.q_lbl.text = 'What interval did you hear?' if self.is_ear_training else f'{rn}  →  {tn}\nWhat interval?'
        self.fb_lbl.text = ''; correct = INTERVALS[self.interval_n][0]; self.correct_display = correct
        self._populate_answers(self._make_choices(correct, [INTERVALS[i][0] for i in range(1, 13)]))
        self._play_audio()
    def _play_audio(self): self.synth.play_sequence([midi_to_freq(60+self.root_n), midi_to_freq(60+self.root_n+self.interval_n)], duration=0.6)
    def check(self, ans): self._finish(ans == self.correct_display)

class ScaleQuizScreen(BaseQuizScreen):
    title = 'Scale Quiz'; icon = '🎯'
    def new_q(self):
        self.root_n = random.randint(0, 11); rn = NOTE_NAMES[self.root_n]
        self.correct_name, self.current_formula = random.choice(list(all_scales().items()))
        ns = scale_notes(self.root_n, self.current_formula)
        self.q_lbl.text = 'What scale did you hear?' if self.is_ear_training else f'What scale is this?\n{rn}:  {" - ".join(ns)}'
        self.fb_lbl.text = ''; self.correct_display = self.correct_name
        self._populate_answers(self._make_choices(self.correct_name, list(all_scales().keys())))
        self._play_audio()
    def _play_audio(self): self.synth.play_sequence([midi_to_freq(60+self.root_n+i) for i in self.current_formula], duration=0.35)
    def check(self, ans): self._finish(ans == self.correct_name)

class ChordQuizScreen(BaseQuizScreen):
    title = 'Chord Quiz'; icon = '🎸'
    def new_q(self):
        self.root_n = random.randint(0, 11); rn = NOTE_NAMES[self.root_n]
        self.correct_name, self.current_formula = random.choice(list(CHORD_TYPES.items()))
        ns = chord_notes(self.root_n, self.current_formula)
        self.q_lbl.text = 'What chord did you hear?' if self.is_ear_training else f'What chord?\n{" - ".join(ns)}'
        self.fb_lbl.text = ''; self.correct_display = f'{rn} {self.correct_name}'
        self._populate_answers(self._make_choices(self.correct_name, list(CHORD_TYPES.keys())), fmt=lambda c: f'{rn} {c}')
        self._play_audio()
    def _play_audio(self): self.synth.play_chord([midi_to_freq(60+self.root_n+i) for i in self.current_formula], duration=1.5)
    def check(self, ans): self._finish(ans == self.correct_name)

class EasternQuizScreen(BaseQuizScreen):
    title = 'Raga & Maqam Quiz'; icon = '🔮'
    def __init__(self, **kw):
        self.pool = [(f'Raga {k}', v['notes'], v['desc']) for k,v in EASTERN_RAGAS.items()] + \
                    [(f'Maqam {k}', v['notes'], v['desc']) for k,v in ARABIC_MAQAMS.items()] + \
                    [(f'Dastgah {k}', v['notes'], v['desc']) for k,v in PERSIAN_DASTGAH.items()]
        super().__init__(**kw)
    def new_q(self):
        self.root_n = random.randint(0, 11); rn = NOTE_NAMES[self.root_n]
        self.correct_name, self.current_formula, self.correct_desc = random.choice(self.pool)
        ns = scale_notes(self.root_n, self.current_formula)
        self.q_lbl.text = 'Identify the mode you heard:' if self.is_ear_training else f'Identify this mode:\n{rn}:  {" - ".join(ns)}'
        self.fb_lbl.text = ''; self.correct_display = self.correct_name
        self._populate_answers(self._make_choices(self.correct_name, [p[0] for p in self.pool]))
        self._play_audio()
    def _play_audio(self): self.synth.play_sequence([midi_to_freq(60+self.root_n+i) for i in self.current_formula], duration=0.35)
    def check(self, ans):
        cfb = (f'✅  Correct!\n{self.correct_desc}') if ans==self.correct_name else (f'❌  Answer: {self.correct_name}\n{self.correct_desc}')
        self._finish(ans == self.correct_name, custom_fb=cfb)

class JazzQuizScreen(BaseQuizScreen):
    title = 'Jazz Chord Quiz'; icon = '🎺'
    def new_q(self):
        self.root_n = random.randint(0, 11); rn = NOTE_NAMES[self.root_n]
        self.correct_name, self.current_formula = random.choice(list(JAZZ_CHORDS.items()))
        ns = chord_notes(self.root_n, self.current_formula)
        self.q_lbl.text = 'What jazz chord did you hear?' if self.is_ear_training else f'What jazz chord?\n{" - ".join(ns)}'
        self.fb_lbl.text = ''; self.correct_display = f'{rn}{self.correct_name}'
        self._populate_answers(self._make_choices(self.correct_name, list(JAZZ_CHORDS.keys())), fmt=lambda c: f'{rn}{c}')
        self._play_audio()
    def _play_audio(self): self.synth.play_chord([midi_to_freq(60+self.root_n+i) for i in self.current_formula], duration=1.5)
    def check(self, ans): self._finish(ans == self.correct_name)

class KeySigQuizScreen(BaseQuizScreen):
    title = 'Key Signature Quiz'; icon = '📝'; has_audio = False
    def new_q(self):
        self.correct_key, sig = random.choice(list(KEY_SIGNATURES.items()))
        self.q_lbl.text = f'What key has {abs(sig)} flat{"s" if abs(sig)!=1 else ""}?' if sig<0 else f'What key has {sig} sharp{"s" if sig!=1 else ""}?' if sig>0 else 'What key has no accidentals?'
        self.fb_lbl.text = ''; self.correct_display = self.correct_key
        self._populate_answers(self._make_choices(self.correct_key, list(KEY_SIGNATURES.keys())))
    def check(self, ans): self._finish(ans == self.correct_key)

class RhythmQuizScreen(BaseQuizScreen):
    title = 'Rhythm & Meter Quiz'; icon = '🥁'; has_audio = False
    def new_q(self):
        self.correct_name, mdata = random.choice(list(RHYTHM_METER_DATA.items()))
        self.q_lbl.text = f'Which meter fits this?\n{mdata["desc"]}' if random.choice([True, False]) else f'What kind of meter is {mdata["example"]}?'
        self.correct_desc = mdata['desc']; self.fb_lbl.text = ''; self.correct_display = self.correct_name
        self._populate_answers(self._make_choices(self.correct_name, list(RHYTHM_METER_DATA.keys())))
    def check(self, ans):
        cfb = (f'✅  Correct!\n{self.correct_desc}') if ans==self.correct_name else (f'❌  Answer: {self.correct_name}\n{self.correct_desc}')
        self._finish(ans == self.correct_name, custom_fb=cfb)


# ─── NEW QUIZZES ──────────────────────────────────────────────

class DiatonicChordQuizScreen(BaseQuizScreen):
    title = 'Diatonic Chord Quiz'; icon = '🎵'
    def new_q(self):
        self.root_n = random.randint(0, 11)
        rn = NOTE_NAMES[self.root_n]
        self.is_major = random.choice([True, False])
        
        if self.is_major:
            data = DIATONIC_CHORDS_MAJOR
            key_text = f'{rn} Major'
        else:
            data = DIATONIC_CHORDS_MINOR
            key_text = f'{rn} Minor (Natural)'
            
        self.correct_name, cdata = random.choice(list(data.items()))
        self.current_formula = cdata['intervals']
        ns = [NOTE_NAMES[(self.root_n + i)%12] for i in self.current_formula]
        
        self.q_lbl.text = 'What Roman numeral did you hear?' if self.is_ear_training else f'In {key_text}, what is this chord?\n{" - ".join(ns)}'
        self.fb_lbl.text = ''
        self.correct_display = self.correct_name
        
        self._populate_answers(self._make_choices(self.correct_name, list(data.keys())))
        self._play_audio()

    def _play_audio(self):
        freqs = [midi_to_freq(60 + self.root_n + i) for i in self.current_formula]
        self.synth.play_chord(freqs, duration=1.2)

    def check(self, ans):
        ok = ans == self.correct_name
        self._finish(ok)


class CadenceQuizScreen(BaseQuizScreen):
    title = 'Cadence Quiz'; icon = '🏛️'
    def new_q(self):
        self.root_n = random.randint(0, 11)
        rn = NOTE_NAMES[self.root_n]
        self.correct_name, cdata = random.choice(list(CADENCES.items()))
        self.chord_intervals = cdata['chords']
        self.correct_desc = cdata['desc']
        
        if self.is_ear_training:
            self.q_lbl.text = 'What cadence did you hear?'
        else:
            # Display chords for visual quiz
            names = []
            for chord_ints in self.chord_intervals:
                names.append(" - ".join([NOTE_NAMES[(self.root_n+i)%12] for i in chord_ints]))
            self.q_lbl.text = 'What cadence is this?\n' + "  →  ".join(names)
            
        self.fb_lbl.text = ''
        self.correct_display = self.correct_name
        
        self._populate_answers(self._make_choices(self.correct_name, list(CADENCES.keys())))
        self._play_audio()

    def _play_audio(self):
        chords_freqs = []
        for chord_ints in self.chord_intervals:
            chords_freqs.append([midi_to_freq(48 + self.root_n + i) for i in chord_ints]) # 48 = Low C
        self.synth.play_progression(chords_freqs, beat_duration=0.9)

    def check(self, ans):
        ok = ans == self.correct_name
        cfb = (f'✅  Correct!\n{self.correct_desc}') if ok else (f'❌  Answer: {self.correct_name}\n{self.correct_desc}')
        self._finish(ok, custom_fb=cfb)


# ─── EAR TRAINING SCREENS ────────────────────────────────────

class EarIntervalQuizScreen(IntervalQuizScreen):
    title = 'Ear Interval Quiz'; icon = '🔊'; is_ear_training = True

class EarScaleQuizScreen(ScaleQuizScreen):
    title = 'Ear Scale Quiz'; icon = '🔊'; is_ear_training = True

class EarChordQuizScreen(ChordQuizScreen):
    title = 'Ear Chord Quiz'; icon = '🔊'; is_ear_training = True

class EarDiatonicChordQuizScreen(DiatonicChordQuizScreen):
    title = 'Ear Diatonic Quiz'; icon = '🔊'; is_ear_training = True

class EarCadenceQuizScreen(CadenceQuizScreen):
    title = 'Ear Cadence Quiz'; icon = '🔊'; is_ear_training = True