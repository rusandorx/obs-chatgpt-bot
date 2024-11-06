from playsound import playsound
import os
import uuid
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
print(ELEVENLABS_API_KEY)

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


def text_to_speech_file_eleven_labs(text: str) -> str:
    response = client.text_to_speech.convert(
        voice_id="Dyt77XyVgLv7Zjv60RIk",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.4,
            similarity_boost=0.7,
            style=0.1,
            use_speaker_boost=True
        )
    )

    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path
