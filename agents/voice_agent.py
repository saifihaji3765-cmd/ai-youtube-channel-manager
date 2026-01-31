from gtts import gTTS
from config import settings

class VoiceAgent:
    def run(self, script):
        print("🔊 VoiceAgent: Generating audio using gTTS")
        tts = gTTS(text=script, lang='en')
        audio_file = "output_audio.mp3"
        tts.save(audio_file)
        print(f"🔊 Audio saved: {audio_file}")
        return audio_file
