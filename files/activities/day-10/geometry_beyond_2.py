"""
SoftDes Spring 2017 day 11 in-class exercise: Going Beyond #2
"""

import pygame
from geometry import Rect
# from geometry import Circle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
display = pygame.display.set_mode((350, 350))
display.fill(BLACK)


def draw_shapes(shapes):
    pygame.draw.rect(display, WHITE, (10, 10, 10, 10))
    pygame.display.update()

shapes = []
shapes.append((Rect(10, 10, 20, 100), WHITE))
shapes.append((Rect(50, 50, 60, 60), BLACK))
# shapes.append((Circle(50, 150, 30), BLUE))
draw_shapes(shapes)

# Wait for the user to press the Escape key.
while not any(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
              for event in pygame.event.get()):
    pass
