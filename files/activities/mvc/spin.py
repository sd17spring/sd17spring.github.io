"""Spins a line around the center of the screen.

Author : Oliver Steele <oliver.steele@olin.edu>
Course : Olin Software Design Fall 2016
Date   : 2016-10-24
License: MIT LICENSE
"""

import math

import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Spinner(object):
    def __init__(self):
        self.x = 320
        self.y = 240
        self.length = 80.0
        self.angle = 0.0

    def step(self):
        self.angle += 1.0

    def draw(self, surface):
        radians = self.angle * math.pi / 360.0
        dx = self.length / 2 * math.cos(radians)
        dy = self.length / 2 * math.sin(radians)
        start = (self.x - dx, self.y - dy)
        end = (self.x + dx, self.y + dy)
        pygame.draw.line(surface, BLUE, start, end, 2)


pygame.init()
screen = pygame.display.set_mode((640, 480))

spinner = Spinner()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spinner.contains_pt(pygame.mouse.get_pos()):
                pass
        if event.type == pygame.QUIT:
            running = False

    spinner.step()

    screen.fill(BLACK)
    spinner.draw(screen)

    pygame.display.update()

pygame.quit()
