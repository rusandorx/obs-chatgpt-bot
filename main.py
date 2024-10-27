from tts import play_audio
# from stt import listen
from obs import set_text
from gpt import send_message

response = send_message("Привет чем занимаешься")

set_text(response)
play_audio(response)
