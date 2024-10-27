from tts import play_audio
from stt import STTManager
from obs import set_text
from gpt import GPTManager
import keyboard

stt = STTManager()
gpt = GPTManager()


def on_listen():
    recognized_text = stt.listen()
    response = gpt.send_message(recognized_text)
    print('response: ', response)
    set_text(response)
    play_audio(response)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('l'):
            on_listen()

# response = send_message("Привет чем занимаешься")
#
# set_text(response)
# play_audio(response)
