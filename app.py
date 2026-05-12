"""
Music Theory Academy — Main Application Entry Point
"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

Window.clearcolor = (0.08, 0.08, 0.12, 1)

import data; import helpers; import styles; import synth

from main_menu import MainMenuScreen
from ref import WesternRefScreen, EasternRefScreen, JazzRefScreen, PopRockRefScreen, ModernRefScreen
from quizzes import (
    IntervalQuizScreen, ScaleQuizScreen, ChordQuizScreen, EasternQuizScreen, JazzQuizScreen,
    KeySigQuizScreen, RhythmQuizScreen, DiatonicChordQuizScreen, CadenceQuizScreen,
    EarIntervalQuizScreen, EarChordQuizScreen, EarScaleQuizScreen, EarDiatonicChordQuizScreen, EarCadenceQuizScreen,
)
from tools import ScaleBuilderScreen, CircleScreen


class MusicTheoryApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainMenuScreen(name='main_menu'))
        
        # Reference
        sm.add_widget(WesternRefScreen(name='western_ref'))
        sm.add_widget(EasternRefScreen(name='eastern_ref'))
        sm.add_widget(JazzRefScreen(name='jazz_ref'))
        sm.add_widget(PopRockRefScreen(name='pop_rock_ref'))
        sm.add_widget(ModernRefScreen(name='modern_ref'))
        
        # Visual Quizzes
        sm.add_widget(IntervalQuizScreen(name='interval_quiz'))
        sm.add_widget(ScaleQuizScreen(name='scale_quiz'))
        sm.add_widget(ChordQuizScreen(name='chord_quiz'))
        sm.add_widget(DiatonicChordQuizScreen(name='diatonic_quiz'))
        sm.add_widget(CadenceQuizScreen(name='cadence_quiz'))
        sm.add_widget(EasternQuizScreen(name='eastern_quiz'))
        sm.add_widget(JazzQuizScreen(name='jazz_quiz'))
        sm.add_widget(KeySigQuizScreen(name='keysig_quiz'))
        sm.add_widget(RhythmQuizScreen(name='rhythm_quiz'))
        
        # Ear Training Quizzes
        sm.add_widget(EarIntervalQuizScreen(name='ear_interval_quiz'))
        sm.add_widget(EarChordQuizScreen(name='ear_chord_quiz'))
        sm.add_widget(EarScaleQuizScreen(name='ear_scale_quiz'))
        sm.add_widget(EarDiatonicChordQuizScreen(name='ear_diatonic_quiz'))
        sm.add_widget(EarCadenceQuizScreen(name='ear_cadence_quiz'))
        
        # Tools
        sm.add_widget(ScaleBuilderScreen(name='scale_builder'))
        sm.add_widget(CircleScreen(name='circle'))

        return sm


if __name__ == '__main__':
    MusicTheoryApp().run()