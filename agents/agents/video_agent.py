import requests, os
from moviepy.editor import ImageClip, AudioFileClip
from settings import PEXELS_API_KEY, TEMP_DIR, VIDEO_FPS

def generate_video(audio_path):
    headers = {"Authorization": PEXELS_API_KEY}
    res = requests.get("https://api.pexels.com/v1/search?query=business&per_page=1", headers=headers)
    image_url = res.json()["photos"][0]["src"]["landscape"]

    image_path = os.path.join(TEMP_DIR, "bg.jpg")
    with open(image_path, "wb") as f:
        f.write(requests.get(image_url).content)

    audio = AudioFileClip(audio_path)
    clip = ImageClip(image_path).set_duration(audio.duration).set_audio(audio)

    output_video = os.path.join(TEMP_DIR, "final_video.mp4")
    clip.write_videofile(output_video, fps=VIDEO_FPS)

    return output_video
