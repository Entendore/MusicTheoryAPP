"""
Music Theory Academy — Reference Screens
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp, sp

from styles import BackBtn, SectionHeader, ResponsiveGrid
from data import (
    WESTERN_SCALES, INTERVALS, CHORD_TYPES, KEY_SIGNATURES, NON_CHORD_TONES,
    DIATONIC_CHORDS_MAJOR, DIATONIC_CHORDS_MINOR, CADENCES,
    JAZZ_CHORDS, JAZZ_SCALES, JAZZ_PROGRESSIONS, MODAL_JAZZ, REHARM_TECHNIQUES,
    EASTERN_RAGAS, ARABIC_MAQAMS, PERSIAN_DASTGAH, TURKISH_MAKAMS,
    JAPANESE_SCALES, CHINESE_SCALES, GAMELAN_SCALES,
    POP_ROCK_PROGRESSIONS, BLUES_FORMS, ROCK_CONCEPTS,
    SET_THEORY, TWELVE_TONE, ORCHESTRATION_TRANSPOSITION,
)
from helpers import scale_notes, chord_notes


class BaseRefScreen(Screen):
    screen_title = ''; screen_icon = ''

    def _build_header(self):
        hd = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(10))
        bb = BackBtn(text='← Back')
        bb.bind(on_release=lambda x: setattr(self.manager, 'current', 'main_menu'))
        hd.add_widget(bb)
        title = Label(text=f'{self.screen_icon} {self.screen_title}', font_size=sp(20), bold=True, color=(1, .85, .2, 1), halign='left', valign='middle')
        title.bind(width=lambda i, v: setattr(i, 'text_size', (v, None)))
        hd.add_widget(title)
        return hd

    @staticmethod
    def _subtitle(t): return SectionHeader(text=f'   {t}')

    @staticmethod
    def _info(t):
        lbl = Label(text=t, font_size=sp(13), color=(.85, .85, .85, 1), size_hint_y=None, halign='left', valign='middle')
        lbl.bind(width=lambda i, v: setattr(i, 'text_size', (v - dp(16), None)), texture_size=lambda i, v: setattr(i, 'height', max(v[1], dp(22))))
        return lbl

    @staticmethod
    def _spacer(h=6): return Label(text='', size_hint_y=None, height=dp(h))

    def _build_scroll(self, sections):
        sv = ScrollView()
        gl = GridLayout(cols=1, spacing=dp(4), size_hint_y=None, padding=dp(4))
        gl.bind(minimum_height=gl.setter('height'))
        for title, items in sections:
            gl.add_widget(self._subtitle(title))
            for item in items: gl.add_widget(item)
            gl.add_widget(self._spacer(8))
        sv.add_widget(gl)
        return sv


class WesternRefScreen(BaseRefScreen):
    screen_title = 'Western Theory'; screen_icon = '🎼'

    def __init__(self, **kw):
        super().__init__(**kw)
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))
        ly.add_widget(self._build_header())
        sections = []

        # Scales & Modes
        items = [self._info(f'{sn}:  {" - ".join(scale_notes(0, sf))}') for sn, sf in WESTERN_SCALES.items()]
        sections.append(('Major & Minor Scales', items))

        # Intervals
        items = [self._info(f'{ab}  {nm}  ({st} semitone{"s" if st != 1 else ""})') for st, (nm, ab) in sorted(INTERVALS.items())]
        sections.append(('Intervals', items))

        # Diatonic Chords
        items = [self._info(f'{rn}:  {cd["type"]} ( {" - ".join([NOTE_NAMES[i%12] for i in cd["intervals"]])} )') for rn, cd in DIATONIC_CHORDS_MAJOR.items()]
        sections.append(('Diatonic Chords (Major)', items))
        items = [self._info(f'{rn}:  {cd["type"]} ( {" - ".join([NOTE_NAMES[i%12] for i in cd["intervals"]])} )') for rn, cd in DIATONIC_CHORDS_MINOR.items()]
        sections.append(('Diatonic Chords (Minor)', items))

        # Chords
        items = [self._info(f'{cn}:  {" - ".join(chord_notes(0, cf))}') for cn, cf in CHORD_TYPES.items()]
        sections.append(('Triads & Seventh Chords', items))

        # Cadences
        items = [self._info(f'{cn.split("(")[0]}') for cn, cd in CADENCES.items()]
        for cn, cd in CADENCES.items(): items.append(self._info(f'   {cd["desc"]}'))
        sections.append(('Cadences', items))

        # Non-Chord Tones
        items = [self._info(f'{n}: {d}') for n, d in NON_CHORD_TONES.items()]
        sections.append(('Non-Chord Tones', items))

        # Key Signatures
        items = []
        for k, v in sorted(KEY_SIGNATURES.items(), key=lambda x: x[1]):
            s = f'{v} sharp{"s" if v > 1 else ""}' if v > 0 else f'{abs(v)} flat{"s" if abs(v) > 1 else ""}' if v < 0 else 'No accidentals'
            items.append(self._info(f'{k}:  {s}'))
        sections.append(('Key Signatures', items))

        ly.add_widget(self._build_scroll(sections))
        self.add_widget(ly)


class EasternRefScreen(BaseRefScreen):
    screen_title = 'Eastern Theory'; screen_icon = '🕌'

    def __init__(self, **kw):
        super().__init__(**kw)
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))
        ly.add_widget(self._build_header())
        sections = []

        # Ragas
        items = []
        for rn, rd in EASTERN_RAGAS.items():
            ns = scale_notes(0, rd['notes'])
            items.extend([self._info(f'♩ {rn} ({rd["region"]})'), self._info(f'   Notes: {" - ".join(ns)} | Mood: {rd["mood"]}'), self._info(f'   {rd["desc"]}')])
        sections.append(('🇮🇳 Indian Ragas', items))

        # Arabic
        items = []
        for mn, md in ARABIC_MAQAMS.items():
            ns = scale_notes(0, md['notes'])
            items.extend([self._info(f'♩ {mn} ({md["family"]})'), self._info(f'   Notes: {" - ".join(ns)} | Mood: {md["mood"]}'), self._info(f'   {md["desc"]}')])
        sections.append(('🇸🇦 Arabic Maqamat', items))

        # Turkish
        items = []
        for mn, md in TURKISH_MAKAMS.items():
            ns = scale_notes(0, md['notes'])
            items.extend([self._info(f'♩ {mn} ({md["family"]})'), self._info(f'   Notes: {" - ".join(ns)}'), self._info(f'   {md["desc"]}')])
        sections.append(('🇹🇷 Turkish Makams', items))

        # Persian
        items = []
        for dn, dd in PERSIAN_DASTGAH.items():
            ns = scale_notes(0, dd['notes'])
            items.extend([self._info(f'♩ Dastgah-e {dn}'), self._info(f'   Notes: {" - ".join(ns)} | Mood: {dd["mood"]}')])
        sections.append(('🇮🇷 Persian Dastgah', items))

        # Gamelan
        items = []
        for sn, sd in GAMELAN_SCALES.items():
            ns = scale_notes(0, sd['notes'])
            items.extend([self._info(f'♩ {sn}: {" - ".join(ns)}'), self._info(f'   {sd["desc"]}')])
        sections.append(('🇮🇩 Gamelan (Indonesia)', items))

        # Japan/China
        items = [self._info(f'♩ {sn}:  {" - ".join(scale_notes(0, sf))}') for sn, sf in JAPANESE_SCALES.items()]
        sections.append(('🇯🇵 Japanese Scales', items))
        items = [self._info(f'♩ {sn}:  {" - ".join(scale_notes(0, sf))}') for sn, sf in CHINESE_SCALES.items()]
        sections.append(('🇨🇳 Chinese Scales', items))

        sections.append(('Note on Quarter Tones', [self._info('Many Eastern scales use microtones approximated here by 12-TET.')]))
        ly.add_widget(self._build_scroll(sections))
        self.add_widget(ly)


class JazzRefScreen(BaseRefScreen):
    screen_title = 'Jazz Theory'; screen_icon = '🎷'

    def __init__(self, **kw):
        super().__init__(**kw)
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))
        ly.add_widget(self._build_header())
        sections = []

        items = [self._info(f'C{cn}:  {" - ".join(chord_notes(0, cf))}') for cn, cf in JAZZ_CHORDS.items()]
        sections.append(('Extended & Altered Chords', items))
        items = [self._info(f'{sn}:  {" - ".join(scale_notes(0, sf))}') for sn, sf in JAZZ_SCALES.items()]
        sections.append(('Jazz Scales', items))
        items = []
        for pn, pd in JAZZ_PROGRESSIONS.items(): items.extend([self._info(f'🎵 {pn}'), self._info(f'   {pd["desc"]}')])
        sections.append(('Common Jazz Progressions', items))
        
        items = [self._info(f'{k}: {v}') for k, v in MODAL_JAZZ.items()]
        sections.append(('Modal Jazz Concepts', items))
        items = [self._info(f'{k}: {v}') for k, v in REHARM_TECHNIQUES.items()]
        sections.append(('Reharmonization Techniques', items))

        ly.add_widget(self._build_scroll(sections))
        self.add_widget(ly)


class PopRockRefScreen(BaseRefScreen):
    screen_title = 'Pop & Blues Theory'; screen_icon = '🎸'

    def __init__(self, **kw):
        super().__init__(**kw)
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))
        ly.add_widget(self._build_header())
        sections = []

        items = [self._info(f'🎵 {pn}'), self._info(f'   {pd["desc"]}') for pn, pd in POP_ROCK_PROGRESSIONS.items() for _ in range(1)]
        # Flattening logic for display
        flat_items = []
        for pn, pd in POP_ROCK_PROGRESSIONS.items():
            flat_items.extend([self._info(f'🎵 {pn}'), self._info(f'   {pd["desc"]}')])
        sections.append(('Pop & Rock Progressions', flat_items))

        items = []
        for bn, bd in BLUES_FORMS.items():
            items.extend([self._info(f'🎵 {bn}'), self._info(f'   Form: {bd["form"]}'), self._info(f'   {bd["desc"]}')])
        sections.append(('Blues Forms', items))

        items = [self._info(f'• {k}: {v}') for k, v in ROCK_CONCEPTS.items()]
        sections.append(('Rock Guitar Concepts', items))

        ly.add_widget(self._build_scroll(sections))
        self.add_widget(ly)


class ModernRefScreen(BaseRefScreen):
    screen_title = 'Modern & Orchestration'; screen_icon = '🔮'

    def __init__(self, **kw):
        super().__init__(**kw)
        ly = BoxLayout(orientation='vertical', padding=dp(12), spacing=dp(6))
        ly.add_widget(self._build_header())
        sections = []

        items = [self._info(f'{k}: {v}') for k, v in SET_THEORY.items()]
        sections.append(('Musical Set Theory', items))
        items = [self._info(f'{k}: {v}') for k, v in TWELVE_TONE.items()]
        sections.append(('Twelve-Tone Technique', items))
        items = [self._info(f'{k}: {v}') for k, v in ORCHESTRATION_TRANSPOSITION.items()]
        sections.append(('Orchestration Transposition', items))

        ly.add_widget(self._build_scroll(sections))
        self.add_widget(ly)