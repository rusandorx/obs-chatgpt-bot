from tts import make_audio_files, play_audio
from stt import STTManager
from obs import set_text, set_image_enabled
from gpt import GPTManager
from eleven_labs_tts import text_to_speech_file_eleven_labs, voices
from pick import pick
import pygame

DEFAULT_VOICE = 'saul_dub'
stt = STTManager()
gpt = GPTManager()


def on_listen():
    recognized_text = stt.listen()
    response = gpt.send_message(recognized_text)
    if response is None:
        print("No response returned")
        return

    print('response: ', response)

    print('--------------------------------------------')
    print('Playing audio.')
    paths = make_audio_files(response)

    set_text(response)
    set_image_enabled(True)

    play_audio(paths)
    print('End of audio')
    print('--------------------------------------------')
    set_image_enabled(False)
    set_text('')


def on_listen_eleven_labs(voice: str):
    recognized_text = stt.listen()
    response = gpt.send_message(recognized_text)
    if response is None:
        print("No response returned")
        return

    print('response: ', response)

    print('--------------------------------------------')
    print('Playing audio.')
    paths = [text_to_speech_file_eleven_labs(response, voice)]

    set_text(response)
    set_image_enabled(True)

    play_audio(paths)
    print('End of audio')
    print('--------------------------------------------')
    set_image_enabled(False)
    set_text('')


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([100, 100])
    screen.fill((0, 0, 0))
    running = True
    voice = DEFAULT_VOICE
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    on_listen()
                if event.key == pygame.K_e:
                    on_listen_eleven_labs(voice)
                if event.key == pygame.K_x:
                    running = False
                if event.key == pygame.K_v:
                    voice, index = pick(
                        list(voices.keys()), 'Choose tts voice: ',
                        default_index=list(voices.keys()).index(voice))
    pygame.quit()
