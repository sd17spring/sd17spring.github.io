"""
Created on Thu Feb 27 19:34:24 2014

@author: pruvolo
"""

import math
import random
import time

import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.001)

    pygame.quit()
