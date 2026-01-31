import openai
from config import settings

openai.api_key = settings.OPENAI_API_KEY

class ResearchAgent:
    def run(self):
        print("🔍 ResearchAgent: Finding trending topic")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a YouTube content research assistant."},
                {"role": "user", "content": "Suggest one high-earning viral topic for Shorts & Long format"}
            ]
        )
        topic = response['choices'][0]['message']['content']
        print(f"🔹 Selected topic: {topic}")
        return {"topic": topic}
