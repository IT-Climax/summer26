"""
We Introduce Object-Oriented Programming.
Students learn: [What is a class?, What is an object?, __init__ , self, Methods, Creating objects, Random,numbers]
Session: Project Session 2.
Goal: Our goal is to create some classes, Snake, Food, Game
"""

import pygame
import sys
import random
from pygame.math import Vector2

pygame.init()


GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 25
OFFSET = 75


screen = pygame.display.set_mode(
    (
        2 * OFFSET + cell_size * number_of_cells,
        2 * OFFSET + cell_size * number_of_cells
    )
)

pygame.display.set_caption("Retro Snake - Session 2")

clock = pygame.time.Clock()

class Snake:

    def __init__(self):

        self.body = [
            Vector2(6, 9),
            Vector2(5, 9),
            Vector2(4, 9)
        ]

        self.direction = Vector2(1, 0)


    def draw(self):

        for segment in self.body:

            segment_rect = (
                OFFSET + segment.x * cell_size,
                OFFSET + segment.y * cell_size,
                cell_size,
                cell_size
            )

            pygame.draw.rect(
                screen,
                DARK_GREEN,
                segment_rect,
                0,
                7
            )


    def update(self):

        new_head = self.body[0] + self.direction

        self.body.insert(0, new_head)

        self.body.pop()


class Food:

    def __init__(self):

        self.position = self.generate_random_position()


    def generate_random_position(self):

        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)

        return Vector2(x, y)


    def draw(self):

        food_rect = pygame.Rect(
            OFFSET + self.position.x * cell_size,
            OFFSET + self.position.y * cell_size,
            cell_size,
            cell_size
        )

        pygame.draw.rect(
            screen,
            DARK_GREEN,
            food_rect,
            0,
            7
        )


snake = Snake()
food = Food()


# -----------------------------------
# GAME LOOP
# -----------------------------------

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)

            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)


    snake.update()

    screen.fill(GREEN)

    pygame.draw.rect(
        screen,
        DARK_GREEN,
        (
            OFFSET - 5,
            OFFSET - 5,
            cell_size * number_of_cells + 10,
            cell_size * number_of_cells + 10
        ),
        5
    )

    snake.draw()
    food.draw()


    pygame.display.update()

    clock.tick(10)