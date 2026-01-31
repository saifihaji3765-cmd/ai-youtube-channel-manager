from gtts import gTTS
import os
from settings import TEMP_DIR

def generate_voice(script_text):
    output_path = os.path.join(TEMP_DIR, "voice.mp3")
    tts = gTTS(text=script_text, lang="en")
    tts.save(output_path)
    return output_path
