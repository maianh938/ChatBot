# tts.py
# Placeholder for Coqui TTS/Bark TTS integration
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    audio_file = "output.wav"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    return audio_file
