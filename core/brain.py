from agents.research_agent import ResearchAgent
from agents.content_agent import ContentAgent
from agents.voice_agent import VoiceAgent
from agents.video_agent import VideoAgent
from agents.publish_agent import PublishAgent
from agents.analytics_agent import AnalyticsAgent

def run_cycle():
    print("🚀 Brain: Starting cycle")

    # 1️⃣ Research trending topic
    topic_data = ResearchAgent().run()

    # 2️⃣ Script generation
    script = ContentAgent().run(topic_data)

    # 3️⃣ Voice generation (gTTS)
    audio_file = VoiceAgent().run(script)

    # 4️⃣ Video generation
    video_file = VideoAgent().run(audio_file, topic_data)

    # 5️⃣ Publish video
    PublishAgent().run(video_file, topic_data)

    # 6️⃣ Analytics / Improvement
    AnalyticsAgent().run(video_file, topic_data)

    print("✅ Cycle complete. AI ready for next task.")
