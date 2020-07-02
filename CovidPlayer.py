
#! /usr/bin/env python3

import pygame
import time
import MusicSelector
from evdev import InputDevice, categorize, ecodes

def connectGamepad():
    try:
        return InputDevice('/dev/input/event3')
    except:
        print("I'm sleeping")
        time.sleep(5)
        return connectGamepad()

def player(gamepad):
    pygame.init()
    pygame.mixer.pre_init(devicename='Muzen Button')
    pygame.mixer.init()
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 00:
                if event.code == 115:
                    song = MusicSelector.main()
                    songSound = pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
                    print('Playing {}' .format(song))
                    while pygame.mixer.music.get_busy():
                        pygame.event.wait()
def main():
    gamepad = connectGamepad()
    player(gamepad)

if __name__ == '__main__':
    main()