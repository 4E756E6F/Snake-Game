import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
    # **DRAW ALL OUR ELEMENTS
    pygame.display.update()
