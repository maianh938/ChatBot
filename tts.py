from bark import SAMPLE_RATE, generate_audio
import numpy as np
import scipy.io.wavfile as wavfile
import os

def text_to_speech(text):
    audio_array = generate_audio(text, history_prompt="v2/en_speaker_6")
    os.makedirs("outputs", exist_ok=True)
    output_path = f"outputs/audio_{int(time.time())}.wav"
    wavfile.write(output_path, SAMPLE_RATE, audio_array)
    return output_path
