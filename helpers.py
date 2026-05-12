"""
Music Theory Academy — Helper Functions
"""
from data import (
    NOTE_NAMES, NOTE_FLATS,
    EASTERN_RAGAS, ARABIC_MAQAMS, PERSIAN_DASTGAH,
    WESTERN_SCALES, JAZZ_SCALES, JAPANESE_SCALES, CHINESE_SCALES,
)


def note_name(semitone, use_flats=False):
    s = semitone % 12
    return NOTE_FLATS[s] if use_flats else NOTE_NAMES[s]


def should_flats(root):
    return root in {1, 3, 5, 8, 10}


def scale_notes(root, formula):
    uf = should_flats(root)
    return [note_name((root + i) % 12, uf) for i in formula]


def chord_notes(root, formula):
    uf = should_flats(root)
    return [note_name((root + i) % 12, uf) for i in formula]


def all_eastern_scales():
    d = {}
    for k, v in EASTERN_RAGAS.items():
        d[f'Raga {k}'] = v['notes']
    for k, v in ARABIC_MAQAMS.items():
        d[f'Maqam {k}'] = v['notes']
    for k, v in PERSIAN_DASTGAH.items():
        d[f'Dastgah {k}'] = v['notes']
    return d


def all_scales():
    d = {}
    d.update(WESTERN_SCALES)
    d.update(JAZZ_SCALES)
    d.update(JAPANESE_SCALES)
    d.update(CHINESE_SCALES)
    d.update(all_eastern_scales())
    return d