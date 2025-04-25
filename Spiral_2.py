import pygame
from math import sin, cos, radians

pygame.init()

width, height = 700, 600
screen = pygame.display.set_mode((width, height))

class Box:
    def __init__(self, x, y, screen, colour, angle, radius):
        self.startX = x
        self.startY = y
        self.box = pygame.Rect(x, y, 4, 4)
        self.screen = screen
        self.colour = colour
        self.angle = angle
        self.radius = radius
    
    def rotateBox(self):
        self.box.x = cos(radians(self.angle)) * self.radius + self.startX
        self.box.y = sin(radians(self.angle)) * self.radius + self.startY
        pygame.draw.rect(self.screen, self.colour, self.box)


box = Box(width//2 - 2, height//2 - 2, screen, (0, 200, 10), 0, 0)
box2 = Box(width//2 - 2, height//2 - 2, screen, (200, 200, 10), 0, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    box.angle += 23
    box.radius += 0.08

    box2.angle -= 23
    box2.radius += 0.08

    box.rotateBox()
    box2.rotateBox()

    pygame.display.update()
pygame.quit()
