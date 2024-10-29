from tts import make_audio_files, play_audio
from stt import STTManager
from obs import set_text, set_image_enabled
from gpt import GPTManager
import pygame

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


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([100, 100])
    screen.fill((0, 0, 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    on_listen()
                if event.key == pygame.K_x:
                    running = False
    pygame.quit()


# response = send_message("Привет чем занимаешься")
#
# set_text(response)
# play_audio(response)
