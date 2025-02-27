# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:19:25 2018
@author: zou
"""
import pygame, random
import numpy as np
# import the time module
import time


class Settings:
    def __init__(self):
        self.width = 28
        self.height = 28
        self.rect_len = 15


class Snake1:
    def __init__(self):

        self.image_up = pygame.image.load('images/head_up.bmp')
        self.image_down = pygame.image.load('images/head_down.bmp')
        self.image_left = pygame.image.load('images/head_left.bmp')
        self.image_right = pygame.image.load('images/head_right.bmp')

        self.tail_up = pygame.image.load('images/tail_up.bmp')
        self.tail_down = pygame.image.load('images/tail_down.bmp')
        self.tail_left = pygame.image.load('images/tail_left.bmp')
        self.tail_right = pygame.image.load('images/tail_right.bmp')

        self.image_body = pygame.image.load('images/body.bmp')

        self.facing = "right"
        self.initialize()

    def initialize(self):
        self.facing = "right"
        self.position = [6, 6]
        self.segments = [[6 - i, 6] for i in range(3)]
        self.score = 0

    def blit_body(self, x, y, screen):
        screen.blit(self.image_body, (x, y))

    def blit_head(self, x, y, screen):
        if self.facing == "up":
            screen.blit(self.image_up, (x, y))
        elif self.facing == "down":
            screen.blit(self.image_down, (x, y))
        elif self.facing == "left":
            screen.blit(self.image_left, (x, y))
        else:
            screen.blit(self.image_right, (x, y))

    def blit_tail(self, x, y, screen):
        tail_direction = [self.segments[-2][i] - self.segments[-1][i] for i in range(2)]

        if tail_direction == [0, -1]:
            screen.blit(self.tail_up, (x, y))
        elif tail_direction == [0, 1]:
            screen.blit(self.tail_down, (x, y))
        elif tail_direction == [-1, 0]:
            screen.blit(self.tail_left, (x, y))
        else:
            screen.blit(self.tail_right, (x, y))

    def blit(self, rect_len, screen):
        self.blit_head(self.segments[0][0] * rect_len, self.segments[0][1] * rect_len, screen)
        for position in self.segments[1:-1]:
            self.blit_body(position[0] * rect_len, position[1] * rect_len, screen)
        self.blit_tail(self.segments[-1][0] * rect_len, self.segments[-1][1] * rect_len, screen)

    def update(self):
        if self.facing == 'right':
            self.position[0] += 1
        if self.facing == 'left':
            self.position[0] -= 1
        if self.facing == 'up':
            self.position[1] -= 1
        if self.facing == 'down':
            self.position[1] += 1
        self.segments.insert(0, list(self.position))

class Snake2:
    def __init__(self):

        self.image_up = pygame.image.load('images/head_up.bmp')
        self.image_down = pygame.image.load('images/head_down.bmp')
        self.image_left = pygame.image.load('images/head_left.bmp')
        self.image_right = pygame.image.load('images/head_right.bmp')

        self.tail_up = pygame.image.load('images/tail_up.bmp')
        self.tail_down = pygame.image.load('images/tail_down.bmp')
        self.tail_left = pygame.image.load('images/tail_left.bmp')
        self.tail_right = pygame.image.load('images/tail_right.bmp')

        self.image_body = pygame.image.load('images/body.bmp')

        self.facing = "right"
        self.initialize()

    def initialize(self):
        self.facing = "right"
        self.position = [22, 22]
        self.segments = [[22 + i, 22] for i in range(3)]
        self.score = 0

    def blit_body(self, x, y, screen):
        screen.blit(self.image_body, (x, y))

    def blit_head(self, x, y, screen):
        if self.facing == "up":
            screen.blit(self.image_up, (x, y))
        elif self.facing == "down":
            screen.blit(self.image_down, (x, y))
        elif self.facing == "left":
            screen.blit(self.image_left, (x, y))
        else:
            screen.blit(self.image_right, (x, y))

    def blit_tail(self, x, y, screen):
        tail_direction = [self.segments[-2][i] - self.segments[-1][i] for i in range(2)]

        if tail_direction == [0, -1]:
            screen.blit(self.tail_up, (x, y))
        elif tail_direction == [0, 1]:
            screen.blit(self.tail_down, (x, y))
        elif tail_direction == [-1, 0]:
            screen.blit(self.tail_left, (x, y))
        else:
            screen.blit(self.tail_right, (x, y))

    def blit(self, rect_len, screen):
        self.blit_head(self.segments[0][0] * rect_len, self.segments[0][1] * rect_len, screen)
        for position in self.segments[1:-1]:
            self.blit_body(position[0] * rect_len, position[1] * rect_len, screen)
        self.blit_tail(self.segments[-1][0] * rect_len, self.segments[-1][1] * rect_len, screen)

    def update(self):
        if self.facing == 'right':
            self.position[0] -= 1
        if self.facing == 'left':
            self.position[0] += 1
        if self.facing == 'up':
            self.position[1] += 1
        if self.facing == 'down':
            self.position[1] -= 1
        self.segments.insert(0, list(self.position))

class Strawberry():
    def __init__(self, settings):
        self.settings = settings

        self.style = str(random.randint(1, 8))
        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')
        self.initialize()

    def random_pos(self, snake1):
        self.style = str(random.randint(1, 8))
        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')
        eat_sound = pygame.mixer.Sound('./sound/eat.wav')
        pygame.mixer.Sound.play(eat_sound)
        self.position[0] = random.randint(0, self.settings.width - 1)
        self.position[1] = random.randint(0, self.settings.height - 1)

        self.position[0] = random.randint(9, 19)
        self.position[1] = random.randint(9, 19)

        if self.position in snake1.segments:
            self.random_pos(snake1)


    def blit(self, screen):
        screen.blit(self.image, [p * self.settings.rect_len for p in self.position])

    def initialize(self):
        self.position = [15, 10]


class Game:
    """
    """

    def countdown(t):
        while t:
            time.sleep(1)
            t -= 1

    def __init__(self):
        self.settings = Settings()
        self.snake1 = Snake1()
        self.snake2 = Snake2()

        self.strawberry = Strawberry(self.settings)
        self.move_dict = {0: 'up',
                          1: 'down',
                          2: 'left',
                          3: 'right'}

    def restart_game(self):
        self.snake1.initialize()
        self.snake2.initialize()
        self.strawberry.initialize()

    def current_state(self):
        state = np.zeros((self.settings.width + 2, self.settings.height + 2, 2))
        expand = [[0, 1], [0, -1], [-1, 0], [1, 0], [0, 2], [0, -2], [-2, 0], [2, 0]]

        for position in self.snake1.segments:
            state[position[1], position[0], 0] = 1
        for position in self.snake2.segments:
            state[position[1], position[0], 0] = 1

        state[:, :, 1] = -0.5

        state[self.strawberry.position[1], self.strawberry.position[0], 1] = 0.5
        for d in expand:
            state[self.strawberry.position[1] + d[0], self.strawberry.position[0] + d[1], 1] = 0.5
        return state

    def direction_to_int(self, direction):
        direction_dict = {value: key for key, value in self.move_dict.items()}
        return direction_dict[direction]

    def do_move(self, move):
        move_dict = self.move_dict

        change_direction = move_dict[move]

        if change_direction == 'right' and not self.snake1.facing == 'left':
            self.snake1.facing = change_direction
            self.snake2.facing = change_direction
        if change_direction == 'left' and not self.snake1.facing == 'right':
            self.snake1.facing = change_direction
            self.snake2.facing = change_direction
        if change_direction == 'up' and not self.snake1.facing == 'down':
            self.snake1.facing = change_direction
            self.snake2.facing = change_direction
        if change_direction == 'down' and not self.snake1.facing == 'up':
            self.snake1.facing = change_direction
            self.snake2.facing = change_direction

        self.snake1.update()
        self.snake2.update()

        if self.snake1.position == self.strawberry.position:
            self.strawberry.random_pos(self.snake1)
            reward = 1
            self.snake1.score += 1
        elif self.snake2.position == self.strawberry.position:
            self.strawberry.random_pos(self.snake2)
            reward = 1
            self.snake2.score += 1
        else:
            self.snake1.segments.pop()
            self.snake2.segments.pop()
            reward = 0

        if self.game_end():
            return -1

        return reward

    def game_end(self):
        end = False
        if self.snake1.position[0] >= self.settings.width or self.snake1.position[0] < 0:
            end = True
        if self.snake1.position[1] >= self.settings.height or self.snake1.position[1] < 0:
            end = True
        if self.snake1.segments[0] in self.snake1.segments[1:]:
            end = True
        if self.snake2.position[0] >= self.settings.width or self.snake2.position[0] < 0:
            end = True
        if self.snake2.position[1] >= self.settings.height or self.snake2.position[1] < 0:
            end = True
        if self.snake2.segments[0] in self.snake2.segments[1:]:
            end = True
        if self.snake1.segments[0] in self.snake2.segments[1:]:
            end = True

        return end

    def blit_score(self, color, screen):
        font = pygame.font.SysFont(None, 25)
        text = font.render('Score: ' + str(self.snake1.score), True, color)
        screen.blit(text, (0, 0))
'''
    def blit_time(self, color, screen):
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont(None, 25)
        counter, text = 10, '10'.rjust(3)
        while True:
            for e in pygame.event.get():
                if e.type == pygame.USEREVENT:
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else 'boom!'
                if e.type == pygame.QUIT:
                    break
'''



class no_endGame:
    """
    """

    def __init__(self):
        self.settings = Settings()
        self.snake = Snake1()
        self.strawberry = Strawberry(self.settings)
        self.move_dict = {0: 'up',
                          1: 'down',
                          2: 'left',
                          3: 'right'}

    def restart_game(self):
        self.snake.initialize()
        self.strawberry.initialize()

    def current_state(self):
        state = np.zeros((self.settings.width + 2, self.settings.height + 2, 2))
        expand = [[0, 1], [0, -1], [-1, 0], [1, 0], [0, 2], [0, -2], [-2, 0], [2, 0]]

        for position in self.snake.segments:
            state[position[1], position[0], 0] = 1

        state[:, :, 1] = -0.5

        state[self.strawberry.position[1], self.strawberry.position[0], 1] = 0.5
        for d in expand:
            state[self.strawberry.position[1] + d[0], self.strawberry.position[0] + d[1], 1] = 0.5
        return state

    def direction_to_int(self, direction):
        direction_dict = {value: key for key, value in self.move_dict.items()}
        return direction_dict[direction]

    def do_move(self, move):
        move_dict = self.move_dict

        change_direction = move_dict[move]

        if change_direction == 'right' and not self.snake.facing == 'left':
            self.snake.facing = change_direction
        if change_direction == 'left' and not self.snake.facing == 'right':
            self.snake.facing = change_direction
        if change_direction == 'up' and not self.snake.facing == 'down':
            self.snake.facing = change_direction
        if change_direction == 'down' and not self.snake.facing == 'up':
            self.snake.facing = change_direction

        self.snake.update()

        if self.snake.position == self.strawberry.position:
            self.strawberry.random_pos(self.snake)
            reward = 1
            self.snake.score += 1
        else:
            self.snake.segments.pop()
            reward = 0

        if self.game_end():
            return -1

        return reward

    def game_end(self):
        end = False
        if self.snake.position[0] >= self.settings.width:
            self.snake.position[0] = 0
        if self.snake.position[0] < 0:
            self.snake.position[0] = self.settings.width
        if self.snake.position[1] >= self.settings.height:
            self.snake.position[0] = 0
        if self.snake.position[1] < 0:
            self.snake.position[1] = self.settings.height

        return end

    def blit_score(self, color, screen):
        font = pygame.font.SysFont(None, 25)
        text = font.render('Score: ' + str(self.snake.score), True, color)
        screen.blit(text, (0, 0))