import pygame
import sys
import random
from pygame import Color
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (51, 255, 51), block_rect)


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 25, 25), fruit_rect)


pygame.init()
cell_size = 40
cell_number = 25
screen = pygame.display.set_mode(
    (cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
