import os

import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"


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

    def reset(self):
        self.x = 320
        self.y = 240
        self.dy = 0

    def contains_pt(self, pt):
        return (self.x - pt[0]) ** 2 + (self.y - pt[1]) ** 2 < self.radius ** 2


class BallView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (self.model.x, int(self.model.y)), self.model.radius)


class BallEnergyView(object):
    def __init__(self, model, x):
        self.model = model
        self.x = x

    def draw(self, surface):
        energy = self.get_energy()
        pygame.draw.line(surface, BLUE, (self.x, 480), (self.x, 480 - int(energy * self.scale)), 20)


class BallKEnergyView(BallEnergyView):
    def __init__(self, model):
        super().__init__(model, 20)
        self.scale = 20

    def get_energy(self):
        return self.model.dy ** 2


class BallPEnergyView(BallEnergyView):
    def __init__(self, model):
        super().__init__(model, 40)
        self.scale = 0.1

    def get_energy(self):
        return (480 - self.model.y) ** 2


class BallController(object):
    def __init__(self, model):
        self.model = model

    def handle_mouse_event(self, event):
        self.model.reset()


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    ball = Ball()
    ball_controller = BallController(ball)
    views = [
        BallView(ball),
        BallPEnergyView(ball),
        BallKEnergyView(ball)
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball_controller.handle_mouse_event(event)
            if event.type == pygame.QUIT:
                running = False

        ball.step()

        screen.fill(BLACK)

        for view in views:
            view.draw(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
