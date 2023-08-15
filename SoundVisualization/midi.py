import os
import numpy as np
import librosa
import pretty_midi

# 读取 MP3 文件并转换为音频信号
audio, sr = librosa.load("m.mp3")

# 提取音高信息
pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)
pitch_indices = np.argmax(magnitudes, axis=0)
pitch_frequencies = pitches[pitch_indices]

# 过滤掉无效的音高信息
valid_indices = np.logical_and(pitch_frequencies > 20, pitch_frequencies < 4186)
valid_pitch_frequencies = pitch_frequencies[valid_indices]

# 创建 PrettyMIDI 对象并指定分辨率为 10
midi = pretty_midi.PrettyMIDI(initial_tempo=120.0, resolution=80)

# 创建一个乐器对象，并将其添加到 midi 对象中
program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
midi_instrument = pretty_midi.Instrument(program=program)
midi.instruments.append(midi_instrument)

# 将音高转换为 MIDI 音符号并添加到 PrettyMIDI 对象中
if len(valid_pitch_frequencies) > 0:
    for pitch_freq in valid_pitch_frequencies:
        midi_note = pretty_midi.hz_to_note_number(pitch_freq)
        print(int(midi_note),end=" ")
        # note_start_time = 0.0
        # note_end_time = 0.5
        # note_velocity = 100
#         note = pretty_midi.Note(
#             velocity=note_velocity,
#             pitch=int(midi_note),
#             start=note_start_time,
#             end=note_end_time
#         )
#         midi_instrument.notes.append(note)
#
# # 将 PrettyMIDI 对象写入 MIDI 文件中
# midi.write("output.mid")