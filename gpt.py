import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

INITIAL_MESSAGE = ""

api_key = os.environ.get("OPENAI_API_KEY")

print(f"key - {api_key}")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.proxyapi.ru/openai/v1",
)

print('Successfully created openai client.')


class GPTManager:
    def __init__(self):
        self.history = [{"role": "system", "content": INITIAL_MESSAGE}]

    def send_message(self, message: str):
        try:
            chat_completion = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=[*self.history, {"role": "user", "content": message}]
            )
        except Exception as e:
            print(f"Couldn't send message: {message}")
            print(f"Error: {e}")

        print('chat_completion: ', chat_completion)
        response = chat_completion.choices[0].message.content
        self.history.append({"role": "user", "content": message}, )
        self.history.append({"role": "assistant", "content": response})

        return chat_completion.choices[0].message.content
