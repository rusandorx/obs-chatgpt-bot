import vosk
import pyaudio
import json


# Here I have downloaded this model to my PC, extracted the files
# and saved it in local directory
# Set the model path
model_path = "vosk-model-ru-0.42"
# Initialize the model with model-path
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, 16000)


p = pyaudio.PyAudio()


def listen():
    print("Listening to speech")
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8192)
    while True:
        data = stream.read(4096)
        if rec.AcceptWaveform(data):  # accept waveform of input voice
            # Parse the JSON result and get the recognized text
            result = json.loads(rec.Result())
            recognized_text = result['text']

            # Write recognized text to the file
            print(recognized_text)

            # Check for the termination keyword
            if "стоп" in recognized_text.lower():
                print("Termination keyword detected. Stopping...")
                break


listen()
