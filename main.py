import pygame
import sys
import random
from pygame import Color
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 25, 25), fruit_rect)


pygame.init()
cell_size = 40
cell_number = 25
screen = pygame.display.set_mode(
    (cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
