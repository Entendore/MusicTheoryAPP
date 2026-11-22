"""
Music Theory Academy — Professional Audio Synthesizer
"""
import threading
import numpy as np

try:
    import sounddevice as sd
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False

SAMPLE_RATE = 44100

def midi_to_freq(midi_note):
    return 440.0 * 2.0 ** ((midi_note - 69) / 12.0)

class Synth:
    def __init__(self):
        self.sr = SAMPLE_RATE

    def _generate_tone(self, freq, duration=0.5, volume=0.35):
        if not AUDIO_AVAILABLE or freq <= 0:
            return np.array([])
        t = np.linspace(0, duration, int(self.sr * duration), False)
        wave = np.sin(2 * np.pi * freq * t) * 0.6
        wave += np.sin(2 * np.pi * freq * 2 * t) * 0.25
        wave += np.sin(2 * np.pi * freq * 3 * t) * 0.10
        wave += np.sin(2 * np.pi * freq * 4 * t) * 0.05
        
        attack = int(0.02 * self.sr)
        decay = int(0.1 * self.sr)
        release = int(0.3 * self.sr)
        env = np.ones_like(t)
        if len(t) > attack + decay + release:
            env[:attack] = np.linspace(0, 1, attack)
            env[attack:attack+decay] = np.linspace(1, 0.7, decay)
            env[attack+decay:-release] = 0.7
            env[-release:] = np.linspace(0.7, 0, release)
        else:
            env = np.linspace(0, 1, len(t) // 2)
            env = np.concatenate([env, np.linspace(1, 0, len(t) - len(env))])
        return wave * env * volume

    def play_chord(self, freqs, duration=1.5):
        if not AUDIO_AVAILABLE or not freqs: return
        def target():
            data = self._generate_tone(freqs[0], duration)
            for f in freqs[1:]:
                data += self._generate_tone(f, duration)
            max_val = np.max(np.abs(data))
            if max_val > 0: data = data / max_val * 0.6
            sd.stop()
            sd.play(data, self.sr)
        threading.Thread(target=target, daemon=True).start()

    def play_sequence(self, freqs, duration=0.5, gap=0.15):
        if not AUDIO_AVAILABLE or not freqs: return
        def target():
            data = np.array([])
            gap_silence = np.zeros(int(self.sr * gap))
            for f in freqs:
                data = np.concatenate([data, self._generate_tone(f, duration), gap_silence])
            max_val = np.max(np.abs(data))
            if max_val > 0: data = data / max_val * 0.6
            sd.stop()
            sd.play(data, self.sr)
        threading.Thread(target=target, daemon=True).start()

    def play_progression(self, chords_freqs, beat_duration=0.8, gap=0.1):
        """Plays a list of chords sequentially. chords_freqs = [[freq1, freq2], [freq3, freq4]]"""
        if not AUDIO_AVAILABLE or not chords_freqs: return
        def target():
            data = np.array([])
            gap_silence = np.zeros(int(self.sr * gap))
            for chord in chords_freqs:
                # Mix chord
                chord_data = self._generate_tone(chord[0], beat_duration, volume=0.3)
                for f in chord[1:]:
                    chord_data += self._generate_tone(f, beat_duration, volume=0.3)
                data = np.concatenate([data, chord_data, gap_silence])
            max_val = np.max(np.abs(data))
            if max_val > 0: data = data / max_val * 0.7
            sd.stop()
            sd.play(data, self.sr)
        threading.Thread(target=target, daemon=True).start()