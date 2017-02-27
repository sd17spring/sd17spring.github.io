"""Animates a bouncing ball.

Author : Oliver Steele <oliver.steele@olin.edu>
Course : Olin Software Design Fall 2016
Date   : 2016-10-24
License: MIT LICENSE
"""

import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Ball(object):
    def __init__(self):
        self.radius = 20
        self.reset()

    def step(self):
        self.y += self.dy
        self.dy += .08
        if self.y > 480 - self.radius and self.dy > 0:
            self.dy *= -1
        self.dy *= 0.99

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, int(self.y)), self.radius)

    def draw_gauges(self, surface):
        ke = self.dy ** 2
        pe = (480 - self.y) ** 2
        pygame.draw.line(surface, BLUE, (10, 480), (10, 480 - int(ke * 20)), 20)
        pygame.draw.line(surface, BLUE, (40, 480), (40, 480 - int(pe / 10)), 20)

    def reset(self):
        self.x = 320
        self.y = 240
        self.dy = 0

    def contains_pt(self, pt):
        return (self.x - pt[0]) ** 2 + (self.y - pt[1]) ** 2 < self.radius ** 2


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    ball = Ball()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball.contains_pt(pygame.mouse.get_pos()):
                    print 'hit'
                    ball.reset()
            if event.type == pygame.QUIT:
                running = False

        ball.step()

        screen.fill(BLACK)
        ball.draw(screen)
        ball.draw_gauges(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
