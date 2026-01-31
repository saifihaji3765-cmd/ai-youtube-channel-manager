from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from config import settings

class VideoAgent:
    def run(self, audio_file, topic_data):
        print("🎬 VideoAgent: Creating video")
        # Example: Simple static image video with audio
        clip = ImageClip("sample_image.jpg", duration=10)  # Replace with dynamic visuals later
        audio = AudioFileClip(audio_file)
        clip = clip.set_audio(audio)
        output_video = settings.VIDEO_OUTPUT_PATH
        clip.write_videofile(output_video, fps=24)
        print(f"🎬 Video saved: {output_video}")
        return output_video
