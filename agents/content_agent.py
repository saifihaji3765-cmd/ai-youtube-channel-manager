from openai import OpenAI
from settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_script(topic):
    prompt = f"""
    Create a powerful YouTube video script on:
    {topic}

    Make it engaging, emotional, and viral.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
