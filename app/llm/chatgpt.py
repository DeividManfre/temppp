from openai import OpenAI
from app.core.config import settings

client = OpenAI()

class ChatGPT:
    def chat(self, messages: list[dict]) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3
        )
        return response.choices[0].message.content
