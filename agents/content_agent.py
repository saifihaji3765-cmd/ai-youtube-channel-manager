import openai
from config import settings

openai.api_key = settings.OPENAI_API_KEY

class ContentAgent:
    def run(self, topic_data):
        print("📝 ContentAgent: Generating script")
        prompt = f"Write a viral YouTube script for the topic: {topic_data['topic']}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative script writer for YouTube."},
                {"role": "user", "content": prompt}
            ]
        )
        script = response['choices'][0]['message']['content']
        print(f"📝 Script generated:\n{script[:100]}...")
        return script
