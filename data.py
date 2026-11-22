"""
Music Theory Academy — Data Constants (Expanded)
"""

NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
NOTE_FLATS = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']

INTERVALS = {
    0:('Unison','P1'), 1:('Minor 2nd','m2'), 2:('Major 2nd','M2'),
    3:('Minor 3rd','m3'), 4:('Major 3rd','M3'), 5:('Perfect 4th','P4'),
    6:('Tritone','TT'), 7:('Perfect 5th','P5'), 8:('Minor 6th','m6'),
    9:('Major 6th','M6'), 10:('Minor 7th','m7'), 11:('Major 7th','M7'),
    12:('Octave','P8'),
}

WESTERN_SCALES = {
    'Major':[0,2,4,5,7,9,11], 'Natural Minor':[0,2,3,5,7,8,10],
    'Harmonic Minor':[0,2,3,5,7,8,11], 'Melodic Minor':[0,2,3,5,7,9,11],
    'Dorian':[0,2,3,5,7,9,10], 'Phrygian':[0,1,3,5,7,8,10],
    'Lydian':[0,2,4,6,7,9,11], 'Mixolydian':[0,2,4,5,7,9,10],
    'Aeolian':[0,2,3,5,7,8,10], 'Locrian':[0,1,3,5,6,8,10],
    'Pentatonic Major':[0,2,4,7,9], 'Pentatonic Minor':[0,3,5,7,10],
    'Blues':[0,3,5,6,7,10], 'Whole Tone':[0,2,4,6,8,10],
    'Chromatic':[0,1,2,3,4,5,6,7,8,9,10,11],
}

CHORD_TYPES = {
    'Major':[0,4,7], 'Minor':[0,3,7], 'Diminished':[0,3,6],
    'Augmented':[0,4,8], 'Major 7th':[0,4,7,11], 'Minor 7th':[0,3,7,10],
    'Dominant 7th':[0,4,7,10], 'Diminished 7th':[0,3,6,9],
    'Half-Dim 7th':[0,3,6,10], 'Augmented 7th':[0,4,8,10],
    'Minor-Major 7th':[0,3,7,11], 'Sus2':[0,2,7], 'Sus4':[0,5,7],
}

# ─── NEW WESTERN DATA ─────────────────────────────────────────

DIATONIC_CHORDS_MAJOR = {
    'I': {'intervals': [0,4,7], 'type': 'Major'},
    'ii': {'intervals': [2,5,9], 'type': 'Minor'},
    'iii': {'intervals': [4,7,11], 'type': 'Minor'},
    'IV': {'intervals': [5,9,12], 'type': 'Major'},
    'V': {'intervals': [7,11,14], 'type': 'Major'},
    'vi': {'intervals': [9,12,16], 'type': 'Minor'},
    'vii°': {'intervals': [11,14,17], 'type': 'Diminished'},
}

DIATONIC_CHORDS_MINOR = {
    'i': {'intervals': [0,3,7], 'type': 'Minor'},
    'ii°': {'intervals': [2,5,8], 'type': 'Diminished'},
    'III': {'intervals': [3,7,10], 'type': 'Major'},
    'iv': {'intervals': [5,8,12], 'type': 'Minor'},
    'v': {'intervals': [7,10,14], 'type': 'Minor'},
    'V': {'intervals': [7,11,14], 'type': 'Major (Harmonic)'},
    'VI': {'intervals': [8,12,15], 'type': 'Major'},
    'VII': {'intervals': [10,14,17], 'type': 'Major'},
    'vii°': {'intervals': [11,14,17], 'type': 'Diminished'},
}

CADENCES = {
    'Perfect Authentic (V → I)': {
        'chords': [[7,11,14], [0,4,7]], 'desc': 'The strongest resolution. V chord moves to I, both in root position.'
    },
    'Plagal (IV → I)': {
        'chords': [[5,9,12], [0,4,7]], 'desc': 'The "Amen" cadence. Subdominant moves to the tonic.'
    },
    'Deceptive (V → vi)': {
        'chords': [[7,11,14], [9,12,16]], 'desc': 'V resolves to vi instead of I, creating surprise and continuation.'
    },
    'Half (ii → V)': {
        'chords': [[2,5,9], [7,11,14]], 'desc': 'Ends on the dominant (V), creating expectation. Does not resolve.'
    },
    'Phrygian Half (iv⁶ → V)': {
        'chords': [[5,8,12], [7,11,14]], 'desc': 'Minor iv moving to V. Often found in minor keys, very dramatic.'
    },
}

NON_CHORD_TONES = {
    'Passing Tone': 'Approaches by step, leaves by step in the same direction.',
    'Neighbor Tone': 'Approaches by step, leaves by step in the opposite direction.',
    'Suspension': 'Held over from previous chord, then resolves down by step.',
    'Retardation': 'Held over from previous chord, then resolves up by step.',
    'Appoggiatura': 'Approached by leap, resolved by step in the opposite direction.',
    'Escape Tone': 'Approached by step, resolved by leap in the opposite direction.',
    'Anticipation': 'Approached by step/leap, held as the harmony catches up.',
    'Pedal Point': 'A sustained note while harmonies change around it.',
}

# ─── EASTERN ADDITIONS ────────────────────────────────────────

EASTERN_RAGAS = {
    'Bhairavi':{'notes':[0,1,3,5,7,8,10],'thaat':'Bhairavi','time':'Morning',
        'mood':'Devotional, melancholic','region':'Hindustani',
        'desc':'Uses all flat notes; morning raga of deep devotion.'},
    'Yaman':{'notes':[0,2,4,6,7,9,11],'thaat':'Kalyan','time':'Evening',
        'mood':'Romantic, peaceful','region':'Hindustani',
        'desc':'Evening raga with Tivra Ma (F#); serene and romantic.'},
    'Darbari':{'notes':[0,2,3,5,7,8,10],'thaat':'Asavari','time':'Night',
        'mood':'Grand, majestic','region':'Hindustani',
        'desc':'Night raga of courtly grandeur; heavy and slow-moving.'},
    'Bageshri':{'notes':[0,2,3,5,7,9,10],'thaat':'Kafi','time':'Night',
        'mood':'Longing, romantic','region':'Hindustani',
        'desc':'Late night raga evoking longing and romantic yearning.'},
    'Malkauns':{'notes':[0,3,5,7,10],'thaat':'Bhairavi','time':'Night',
        'mood':'Mystical, serious','region':'Hindustani',
        'desc':'Pentatonic raga of deep meditation; one of the oldest ragas.'},
    'Kalyani':{'notes':[0,2,4,6,7,9,11],'thaat':'Kalyani','time':'Evening',
        'mood':'Bright, auspicious','region':'Carnatic',
        'desc':'Carnatic equivalent of Yaman; bright and auspicious.'},
    'Shankarabharanam':{'notes':[0,2,4,5,7,9,11],'thaat':'Shankarabharanam',
        'time':'Any','mood':'Majestic, complete','region':'Carnatic',
        'desc':'Carnatic equivalent of the Major scale; fundamental raga.'},
    'Hanumatodi':{'notes':[0,1,3,5,7,8,10],'thaat':'Hanumatodi','time':'Morning',
        'mood':'Deep, contemplative','region':'Carnatic',
        'desc':'Carnatic morning raga; deeply contemplative and profound.'},
}

ARABIC_MAQAMS = {
    'Rast':{'notes':[0,2,4,5,7,9,11],'family':'Rast',
        'mood':'Pride, power','region':'Arabic',
        'desc':'Foundational maqam; quarter tones between E-F and B-C.'},
    'Bayati':{'notes':[0,1,3,5,7,8,10],'family':'Bayati',
        'mood':'Vitality, joy','region':'Arabic',
        'desc':'Most popular maqam; starts on D with lowered 2nd.'},
    'Hijaz':{'notes':[0,1,4,5,7,8,10],'family':'Hijaz',
        'mood':'Desert, mystery','region':'Arabic',
        'desc':'Augmented 2nd between 2nd-3rd degrees; instantly recognizable.'},
    'Kurd':{'notes':[0,2,3,5,7,8,10],'family':'Kurd',
        'mood':'Sadness, nostalgia','region':'Arabic',
        'desc':'Equivalent to natural minor; deep sadness and nostalgia.'},
    'Nahawand':{'notes':[0,2,3,5,7,8,11],'family':'Nahawand',
        'mood':'Beauty, tenderness','region':'Arabic',
        'desc':'Similar to harmonic minor; one of the most melodic maqams.'},
    'Ajam':{'notes':[0,2,4,5,7,9,11],'family':'Ajam',
        'mood':'Joy, celebration','region':'Arabic',
        'desc':'Equivalent to major scale; festive and celebratory.'},
    'Saba':{'notes':[0,1,3,4,6,7,10],'family':'Saba',
        'mood':'Pain, yearning','region':'Arabic',
        'desc':'Deeply emotional; no Western equivalent.'},
}

PERSIAN_DASTGAH = {
    'Shur':{'notes':[0,1,3,5,7,8,10],'mood':'Sorrowful, passionate',
        'desc':'The most important dastgah; mother of all Persian modes.'},
    'Mahur':{'notes':[0,2,4,5,7,9,11],'mood':'Joyful, festive',
        'desc':'Similar to major scale; associated with joy.'},
    'Homayun':{'notes':[0,1,3,5,7,8,10],'mood':'Majestic, heroic',
        'desc':'Heroic and grand; shares notes with Shur but different emphasis.'},
    'Segah':{'notes':[0,2,3,5,7,8,10],'mood':'Mystical, meditative',
        'desc':'Meditative; starts on the 3rd degree. Very ancient.'},
    'Chahargah':{'notes':[0,2,3,5,7,9,10],'mood':'Heroic, determined',
        'desc':'Powerful dastgah of heroism and determination.'},
    'Nava':{'notes':[0,2,3,5,7,8,10],'mood':'Intimate, tender',
        'desc':'One of the most popular; intimate and expressive.'},
}

TURKISH_MAKAMS = {
    'Rast':{'notes':[0,2,4,5,7,9,11],'family':'Rast',
        'desc':'Fundamental Turkish makam; bright and majestic. Uses comma flats.'},
    'Hicaz':{'notes':[0,1,4,5,7,8,10],'family':'Hicaz',
        'desc':'Distinctive augmented 2nd; deeply emotional and exotic.'},
    'Hüseyni':{'notes':[0,2,3,5,7,8,10],'family':'Hüseyni',
        'desc':'Sorrowful and profound; A minor equivalent with Turkish microtones.'},
    'Uşşak':{'notes':[0,1,3,5,7,8,10],'family':'Uşşak',
        'desc':'Gentle and melancholic; starts with a lowered 2nd degree.'},
    'Kürdi':{'notes':[0,2,3,5,7,8,10],'family':'Kürdi',
        'desc':'Similar to Phrygian/Dorian; soft and emotive.'},
}

JAPANESE_SCALES = {
    'Yo':[0,2,5,7,9], 'In':[0,1,5,7,8],
    'Hirajoshi':[0,2,3,7,8], 'Kumoi':[0,2,3,7,9],
    'Iwato':[0,1,5,6,10],
}

CHINESE_SCALES = {
    'Gong (Major Pent)': [0,2,4,7,9],
    'Shang': [0,2,5,7,10],
    'Jiao': [0,3,5,7,10],
    'Zhi (Mixo Pent)': [0,2,4,7,10],
    'Yu (Minor Pent)': [0,3,5,7,10],
}

GAMELAN_SCALES = {
    'Pelog (approx)': {'notes':[0,1,3,5,7,8,10], 'desc':'Indonesian heptatonic scale. Uses subsets of 5 notes per piece.'},
    'Slendro (approx)': {'notes':[0,2,4,7,9], 'desc':'Indonesian pentatonic scale. Equidistant intervals (roughly).'},
}

# ─── JAZZ ADDITIONS ───────────────────────────────────────────

JAZZ_CHORDS = {
    'Major 9th':[0,4,7,11,14], 'Minor 9th':[0,3,7,10,14],
    'Dominant 9th':[0,4,7,10,14], 'Major 11th':[0,4,7,11,14,17],
    'Minor 11th':[0,3,7,10,14,17], 'Dominant 13th':[0,4,7,10,14,17,21],
    '7b9':[0,4,7,10,13], '7#9':[0,4,7,10,15], '7b5':[0,4,6,10],
    '7#5':[0,4,8,10], '6/9':[0,4,7,9,14], 'Minor 6/9':[0,3,7,9,14],
}

JAZZ_SCALES = {
    'Bebop Dominant':[0,2,4,5,7,9,10,11], 'Bebop Major':[0,2,4,5,7,8,9,11],
    'Altered':[0,1,3,4,6,8,10], 'Lydian Dominant':[0,2,4,6,7,9,10],
    'Phrygian Dominant':[0,1,4,5,7,8,10], 'Diminished HW':[0,1,3,4,6,7,9,10],
    'Diminished WH':[0,2,3,5,6,8,9,11], 'Lydian Augmented':[0,2,4,6,8,9,11],
    'Super Locrian':[0,1,3,4,6,8,10],
}

JAZZ_PROGRESSIONS = {
    'ii-V-I (Major)':{
        'chords':['m7','7','maj7'],'degrees':[2,5,1],
        'desc':'Dm7 → G7 → Cmaj7. The most fundamental jazz progression.'},
    'ii-V-I (Minor)':{
        'chords':['m7b5','7','m7'],'degrees':[2,5,1],
        'desc':'Dm7b5 → G7 → Cm7. Minor key variant.'},
    'Rhythm Changes (A section)':{
        'chords':['maj7','m7','m7','7'],'degrees':[1,6,2,5],
        'desc':'Cmaj7 → Am7 → Dm7 → G7. Based on "I Got Rhythm".'},
    'Blues (Basic)':{
        'chords':['7','7','7'],'degrees':[1,4,5],
        'desc':'C7 → F7 → G7. Foundation of blues and jazz.'},
    'Turnaround (iii-VI-ii-V)':{
        'chords':['m7','7','m7','7'],'degrees':[3,6,2,5],
        'desc':'Em7 → A7 → Dm7 → G7. Classic end-of-phrase turnaround.'},
    'Coltrane Changes':{
        'chords':['maj7','7','7','maj7'],'degrees':[1,'b3','b5',1],
        'desc':'Cmaj7 → Eb7 → Gb7 → Cmaj7. Key centers a major 3rd apart.'},
}

MODAL_JAZZ = {
    'So What Chord': 'Stacked fourths (e.g., Dm11: D-G-C-F-A). Used in Miles Davis\' "So What".',
    'So What Scale': 'Dorian mode played over a sustained pedal.',
    'Mixolydian Over Dominant': 'Standard approach for unaltered V7 chords.',
    'Sus4 Chords': 'V7sus4 resolves to V7 or I. Creates open, floating sound.',
    'Quartal Harmony': 'Chords built in 4ths instead of 3rds. Core of the modal jazz sound.',
    'Pedal Point': 'Sustained bass note while chords change above it.',
}

REHARM_TECHNIQUES = {
    'Tritone Substitution': 'Replace V7 with a dominant 7th a tritone away (Db7 instead of G7).',
    'Diatonic Substitution': 'Replace I with iii or vi. Replace V with vii°.',
    'Chord Quality Change': 'Change a Major chord to Minor, or vice versa.',
    'Adding Extensions': 'Turn a triad into a 7th, 9th, or 13th chord.',
    'Diminished Passing Chords': 'Insert a dim7 chord a half-step above your target chord.',
    'Approach Chords': 'Approach a chord from a half-step above or below.',
}

# ─── POP / ROCK / BLUES THEORY ───────────────────────────────

POP_ROCK_PROGRESSIONS = {
    'Pop Punk (I-V-vi-IV)': {
        'desc': 'C - G - Am - F. The most ubiquitous pop/rock progression since 2000.',
    },
    '50s Doo-Wop (I-vi-IV-V)': {
        'desc': 'C - Am - F - G. Classic 1950s sound, "Stand By Me" progression.',
    },
    'Sad Pop (vi-IV-I-V)': {
        'desc': 'Am - F - C - G. Minor start, uplifting resolution. "Someone Like You".',
    },
    'Epic Rock (I-bVII-IV)': {
        'desc': 'C - Bb - F. Mixolydian flavor. Massive stadium rock sound.',
    },
    'Classic Rock (I-bVII-IV-I)': {
        'desc': 'C - Bb - F - C. The backbone of 70s and 80s rock.',
    },
}

BLUES_FORMS = {
    '12-Bar Blues (Quick Change)': {
        'form': 'I | IV | I | I | IV | IV | I | I | V | IV | I | V',
        'desc': 'Standard 12-bar with a IV chord in bar 2.',
    },
    '12-Bar Blues (Slow Change)': {
        'form': 'I | I | I | I | IV | IV | I | I | V | IV | I | V',
        'desc': 'Traditional 12-bar blues form.',
    },
    '8-Bar Blues': {
        'form': 'I | V | IV | I | V | IV | I | V',
        'desc': 'Shorter form, common in ragtime and early blues.',
    },
}

ROCK_CONCEPTS = {
    'Power Chords': 'Root + Fifth (0,7). Open, heavy sound. Neither major nor minor.',
    'Drop D Tuning': 'Low E string tuned to D. Allows one-finger power chords.',
    'Barre Chords': 'Movable chord shapes based on E and A strings.',
    'Pentatonic Box Positions': '5 overlapping shapes for soloing across the neck.',
    'Modal Interchange': 'Borrowing chords from parallel keys (e.g., bVII, bVI in major).',
}

# ─── MODERN / ORCHESTRATION THEORY ────────────────────────────

SET_THEORY = {
    'Prime Form': 'The most compact, left-packed arrangement of a pitch class set.',
    'Interval Vector': 'A 6-digit number showing the count of interval classes 1-6 in a set.',
    'Inversion': 'Flipping a set vertically (subtracting pitch classes from 12).',
    'Transposition': 'Shifting a set horizontally (adding a constant to all pitch classes).',
    'Complement': 'The pitches NOT in the set. Hexachordal complements are common.',
    'Z-Relation': 'Sets with the same interval vector but different prime forms.',
}

TWELVE_TONE = {
    'Tone Row': 'An ordering of the 12 pitch classes with no repetition.',
    'Prime (P)': 'The original form of the row.',
    'Retrograde (R)': 'The row played backward.',
    'Inversion (I)': 'The row with intervals flipped.',
    'Retrograde Inversion (RI)': 'The inversion played backward.',
}

ORCHESTRATION_TRANSPOSITION = {
    'Clarinet (Bb)': 'Sounds a major 2nd lower than written.',
    'Clarinet (A)': 'Sounds a minor 3rd lower than written.',
    'Trumpet (Bb)': 'Sounds a major 2nd lower than written.',
    'French Horn (F)': 'Sounds a perfect 5th lower than written.',
    'Alto Sax (Eb)': 'Sounds a major 6th higher than written.',
    'Tenor Sax (Bb)': 'Sounds a major 9th higher than written.',
    'Double Bass': 'Sounds an octave higher than written.',
    'Piccolo': 'Sounds an octave lower than written.',
    'Glockenspiel': 'Sounds 2 octaves lower than written.',
    'Xylophone': 'Sounds an octave lower than written.',
}


CIRCLE_FIFTHS = ['C','G','D','A','E','B','F#','Db','Ab','Eb','Bb','F']

KEY_SIGNATURES = {
    'C':0,'G':1,'D':2,'A':3,'E':4,'B':5,'F#':6,
    'F':-1,'Bb':-2,'Eb':-3,'Ab':-4,'Db':-5,'Gb':-6,
    'Am':0,'Em':1,'Bm':2,'F#m':3,'C#m':4,'G#m':5,
    'Dm':-1,'Gm':-2,'Cm':-3,'Fm':-4,'Bbm':-5,'Ebm':-6,
}

RHYTHM_METER_DATA = {
    'Simple Duple':    {'example':'2/4', 'beats':2, 'division':2, 'desc':'March, polka — 2 beats per measure, each divided in 2'},
    'Simple Triple':   {'example':'3/4', 'beats':3, 'division':2, 'desc':'Waltz, minuet — 3 beats per measure, each divided in 2'},
    'Simple Quadruple':{'example':'4/4', 'beats':4, 'division':2, 'desc':'Common time — 4 beats per measure, each divided in 2'},
    'Compound Duple':  {'example':'6/8', 'beats':2, 'division':3, 'desc':'Jig, tarantella — 2 beats, each divided in 3'},
    'Compound Triple': {'example':'9/8', 'beats':3, 'division':3, 'desc':'Siciliana — 3 beats, each divided in 3'},
    'Compound Quadruple':{'example':'12/8','beats':4,'division':3,'desc':'Slow blues, shuffle — 4 beats, each divided in 3'},
    'Odd Meter (5/4)': {'example':'5/4', 'beats':5, 'division':2, 'desc':'Take Five — grouped 3+2 or 2+3'},
    'Odd Meter (7/8)': {'example':'7/8', 'beats':3, 'division':2, 'desc':'Balkan folk — grouped 2+2+3 or 3+2+2'},
    'Mixed Meter':     {'example':'varies','beats':'varies','division':'varies','desc':'Changing time signatures within a piece'},
    'Additive Meter':  {'example':'varies','beats':'varies','division':'varies','desc':'Built by adding irregular groups (e.g. 2+3+2+3=10/8)'},
}