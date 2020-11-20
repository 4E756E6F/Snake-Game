import pygame
import sys
import random
from pygame import Color
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame.surface import Surface


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        # ?    ▼▼  DIFERENTE HEAD POSITION  ▼▼
        self.head_up = pygame.image.load(
            'Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Graphics/head_left.png').convert_alpha()
        # ?    ▼▼  DIFERENTE TAIL POSITION  ▼▼
        self.tail_up = pygame.image.load(
            'Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Graphics/tail_left.png').convert_alpha()
        # ?    ▼▼  DIFERENTE BODY POSITION  ▼▼
        self.body_vertical = pygame.image.load(
            'Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Graphics/body_horizontal.png').convert_alpha()
        # ?    ▼▼  DIFERENTE BODY TURNS  ▼▼
        self.body_tr = pygame.image.load(
            'Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'Graphics/body_bl.png').convert_alpha()
        # ?    ▼▼  EATING SOUND  ▼▼
        self.eating_sound = pygame.mixer.Sound(file='Sound/smb_jump-super.wav')
        # ?    ▼▼  GAMEOVER SOUND  ▼▼
        #! WORK IN PROGRESS
        #self.gameover_sound = pygame.mixer.Sound(file='Sound/smb_death.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                # * Check for body position
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                # * Check for change in direction
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    # * This verifies the position of the head and changes the orientation of the head to the correct one
    def update_head_graphics(self):
        head_body_relation = self.body[1] - self.body[0]
        if head_body_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_body_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_body_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_body_relation == Vector2(0, -1):
            self.head = self.head_down

    # * This verifies the position of the tail and changes the orientation of the tail to the correct one
    def update_tail_graphics(self):
        tail_body_relation = self.body[-2] - self.body[-1]
        if tail_body_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_body_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_body_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_body_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def play_eating_sound(self):
        self.eating_sound.play()

    #! WORK IN PROGRESS
    # def play_gameover_sound(self):
    #     self.gameover_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        fruit_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        screen.blit(ramen, fruit_rect)
        #pygame.draw.rect(screen, (255, 25, 25), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_fruit()
        self.check_colision()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_fruit(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_eating_sound()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_colision(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            # self.snake.play_gameover_sound()
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                # self.snake.play_gameover_sound()
                self.game_over()

    # * Draw grass pattern
    def draw_grass(self):
        GRASS_COLOR = (64, 64, 64)
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, GRASS_COLOR, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, GRASS_COLOR, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = GAME_FONT.render(score_text, True, WHITE)
        score_x = int(CELL_SIZE * CELL_NUMBER - 50)
        score_y = int(CELL_SIZE * CELL_NUMBER - 55)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        ramen_rect = ramen.get_rect(
            midright=(score_rect.left, score_rect.centery))
        background_rect = pygame.Rect(
            ramen_rect.left, ramen_rect.top, ramen_rect.width + score_rect.width + 5, ramen_rect.height)
        pygame.draw.rect(screen, BACKGROUND_COLOR, background_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(ramen, ramen_rect)
        pygame.draw.rect(screen, WHITE, background_rect, 2)

    def game_over(self):
        self.snake.reset()


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# ? CONSTANTS
CELL_SIZE = 40
CELL_NUMBER = 25
BACKGROUND_COLOR = (32, 32, 32)
WHITE = (255, 250, 250)
GAME_FONT = pygame.font.Font('Font/Bohemian Typewriter.ttf', 25)

screen = pygame.display.set_mode(
    (CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()
ramen = pygame.image.load('Graphics/ramen.png').convert_alpha()
ramen = pygame.transform.scale(ramen, (35, 35))


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
    screen.fill(BACKGROUND_COLOR)
    main_game.draw_elements()
    pygame.display.update()
    # * Predifine game framerate
    clock.tick(60)
