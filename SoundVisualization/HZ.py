import librosa
import numpy as np
import winsound

# 设置 MP3 文件路径
mp3_file = "m.mp3"
slice_duration = 300  # 切片的持续时间，单位为毫秒

try:
    # 读取 MP3 文件并转换为音频信号
    audio, sr = librosa.load(mp3_file)

    # 提取频率信息
    frequencies, magnitudes = librosa.core.piptrack(y=audio, sr=sr)

    # 过滤掉频率为零或负数的值
    frequencies = frequencies[frequencies > 0]

    # 将频率转换为 Hz
    Hz = librosa.core.hz_to_midi(frequencies)

    # 将 Hz 值映射到 Beep 函数支持的频率范围内
    freq_range = np.arange(37, 32768)
    Hz_mapped = np.interp(Hz, (Hz.min(), Hz.max()), (freq_range.min(), freq_range.max()))

    # 将 Hz 值转换为整数
    Hz_int = Hz_mapped.astype(int)

    # 将 Hz 值写入文本文件，并按照每 300 毫秒切片
    with open("freq.txt", "w") as f:
        for i in range(0, len(Hz_int), int(sr * slice_duration / 1000)):
            freq = Hz_int[i]
            duration = slice_duration
            winsound.Beep(freq, duration)
            f.write(str(freq) + "\n")

except Exception as e:
    print("Error:", e)