import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

print(f"key - {api_key}")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.proxyapi.ru/openai/v1",
)

print('Successfully created openai client.')


def send_message(message: str):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}]
        )
    except Exception as e:
        print(f"Couldn't send message: {message}")
        print(f"Error: {e}")

    return chat_completion.choices[0].message.content
