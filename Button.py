import pygame
import CovidPlayer

def main():
    pygame.init()
    pygame.mixer.quit()
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
                CovidPlayer.main()
                print ('{} key released'.format(key_name))

    pygame.quit()


if __name__ == '__main__':
    main()


