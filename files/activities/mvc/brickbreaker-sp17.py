"""
Created on Mon February 27, 2017

author: Amon Millner, building upon examples built by previous
SoftDes instructors, such as Paul Ruvolo and Ben Hill.
"""
import time

import pygame


class BrickBreakerModel:
    """Encodes the game state."""

    def __init__(self):
        self.bricks = []
        for x in range(20, 620, 150):
            brick = Brick((0, 255, 0), 20, 100, x, 120)
            self.bricks.append(brick)
        self.paddle = Paddle((255, 255, 255), 20, 100, 200, 450)


class Brick:
    """Encodes the state of a brick in the game."""

    def __init__(self, color, height, width, x, y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y


class Paddle:
    """Encode the state of the paddle in the game."""

    def __init__(self, color, height, width, x, y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y


class PyGameWindowView:
    """A view of brick breaker rendered in a Pygame window."""

    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen, pygame.Color(brick.color[0],
                             brick.color[1], brick.color[2]),
                             pygame.Rect(
                             brick.x, brick.y, brick.width,
                             brick.height))
        pygame.draw.rect(self.screen, pygame.Color(
                         self.model.paddle.color[0],
                         self.model.paddle.color[1],
                         self.model.paddle.color[2]), pygame.Rect(
                         self.model.paddle.x, self.model.paddle.y,
                         self.model.paddle.width, self.model.paddle.height))
        pygame.display.update()


class PyGameMouseController:
    def __init__(self, model):
        self.model = model

    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.model.paddle.x = event.pos[0] - self.model.paddle.width/2.0


if __name__ == '__main__':
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)

    model = BrickBreakerModel()
    view = PyGameWindowView(model, screen)
    controller = PyGameMouseController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                controller.handle_mouse_event(event)
        view.draw()
        time.sleep(.001)

    pygame.quit()
