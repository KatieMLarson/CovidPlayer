import pygame
import time
import MusicSelector

def main():
    pygame.init()
    pygame.mixer.pre_init(devicename='Muzen Button')
    pygame.mixer.init()
    # Window needed to focus button click events
    pygame.display.set_mode((400, 400))
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            key_name = pygame.key.name(event.key)
            key_name = key_name.upper()
            if event.type == pygame.KEYDOWN:
                print ('{} key pressed'.format(key_name))
            elif event.type == pygame.KEYUP:
                song = MusicSelector.main()
                songSound = pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.event.wait()
                print ('{} key released'.format(key_name))
                
    pygame.quit()


if __name__ == '__main__':
    main()



