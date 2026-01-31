from agents.research_agent import get_trending_topic
from agents.content_agent import generate_script
from agents.voice_agent import generate_voice
from agents.video_agent import generate_video
from agents.publish_agent import upload_video

print("🔥 AI SYSTEM STARTED")

topic = get_trending_topic()
print("Topic:", topic)

script = generate_script(topic)
voice = generate_voice(script)
video = generate_video(voice)

upload_video(video, topic, script)

print("✅ VIDEO UPLOADED SUCCESSFULLY")
