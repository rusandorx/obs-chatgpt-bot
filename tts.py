# V4
import os
import torch
import playsound

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)

model = torch.package.PackageImporter(
    local_file).load_pickle("tts_models", "model")
model.to(device)

sample_rate = 48000
speaker = 'baya'


def play_audio(text: str) -> None:
    try:
        audio_path = model.save_wav([text])[0]
        print('--------------------------------------------')
        print(f'Playing audio: {text}')
        playsound.playsound(audio_path)
        print('End of audio')
        print('--------------------------------------------')
        os.remove(audio_path)
    except:
        print(f'Failed playing audio: {text}')
