import sys, pygame
import time
import random as rand
pygame.init()


class Ball:
    def __init__(self, screen, pos=(500,500), speed=(1,3), color=(255, 0, 0), radius=10):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.screen = screen
        self.speed = speed

    def update(self, balls=None):
        self.move(self.speed, balls)

    def move(self, speed, balls):
        newpos = (self.pos[0] + speed[0], self.pos[1] + speed[1])
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

        if newpos[0] > width or newpos[0] < 0:
            newpos = self.pos
            self.speed = (-1 * self.speed[0], self.speed[1])

        if newpos[1] > height or newpos[1] < 0:
            newpos = self.pos
            self.speed = (self.speed[0], -1 * self.speed[1])

        if balls is not None:
            for other in [b for b in balls if b != self]:
                if (other.pos[0] + other.radius) > newpos[0] > (other.pos[0] - other.radius) and \
                        (other.pos[1] + other.radius) > newpos[1] > (other.pos[1] - other.radius):
                    newpos = self.pos
                    self.color = other.color
                    self.speed = (-1 * self.speed[0], -1 * self.speed[1])
                    other.speed = (-1 * other.speed[0], -1 * other.speed[1])

            print("---")


        self.pos = newpos

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)


size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
balls = [Ball(screen)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            balls.append(Ball(screen,
                              pos=pygame.mouse.get_pos(),
                              speed=(rand.randint(-10, 10), rand.randint(-10, 10)),
                              color=(rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)),
                              radius=rand.randint(10, 35)))

    screen.fill((255,255,255))
    for b in balls:
        b.update(balls)
        b.draw_ball()
    pygame.display.update()
    # time.sleep(0.01)






