from tts import play_audio
from stt import STTManager
from obs import set_text
from gpt import send_message
import keyboard

stt = STTManager()


def onListen():
    recognized_text = stt.listen()
    response = send_message(recognized_text)
    print(response)
    set_text(response)
    play_audio(response)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('l'):
            onListen()

# response = send_message("Привет чем занимаешься")
#
# set_text(response)
# play_audio(response)
