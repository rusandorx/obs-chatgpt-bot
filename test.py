import os
from dotenv import load_dotenv
from openai import OpenAI
from tts import play_audio

load_dotenv()


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.proxyapi.ru/openai/v1",
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Скажи что это тест"}]
)

print(chat_completion.choices[0].message.content)
play_audio(chat_completion.choices[0].message.content)
