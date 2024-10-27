import vosk
import pyaudio
import json
import keyboard

# Here I have downloaded this model to my PC, extracted the files
# and saved it in local directory
# Set the model path
model_path = "vosk-model-ru-0.42"
# Initialize the model with model-path
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, 16000)


p = pyaudio.PyAudio()


class STTManager:
    def __init__(self):
        self.pressed_stop_key = False

        keyboard.on_press_key('q', self.on_pressed_stop_key)

    def on_pressed_stop_key(self, key):
        self.pressed_stop_key = True

    def listen(self):
        print("Listening to speech")
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=16000,
                        input=True,
                        frames_per_buffer=8192)

        text = ''
        while True:
            data = stream.read(4096)
            if rec.AcceptWaveform(data):  # accept waveform of input voice
                # Parse the JSON result and get the recognized text
                result = json.loads(rec.Result())
                recognized_text = result['text']

                print(recognized_text)
                text += recognized_text

                if self.pressed_stop_key:
                    self.pressed_stop_key = False
                    print("Termination key detected. Stopping...")
                    break
        return text
