import openai
import json
import os

# 🔑 OpenAI API Key (GitHub secrets ya direct)
openai.api_key = os.getenv("OPENAI_API_KEY") or "PASTE_OPENAI_API_KEY"

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

system_prompt = load_file("brain/system_prompt.txt")
memory = load_file("brain/memory.json")

def run_agent(task):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": f"CHANNEL_MEMORY:\n{memory}"},
            {"role": "user", "content": task}
        ],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"]
