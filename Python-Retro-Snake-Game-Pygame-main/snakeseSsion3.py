"""
Here we design game collision, Eating & Score, the logic that makes it a real game is introduce here.

*Students learn*: 
[if, Boolean values, Comparisons, Lists, Collision detection, Game state, Score]
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

pygame.display.set_caption("Retro Snake - Session 3")

clock = pygame.time.Clock()

score_font = pygame.font.Font(None, 40)


class Snake:

    def __init__(self):

        self.body = [
            Vector2(6, 9),
            Vector2(5, 9),
            Vector2(4, 9)
        ]

        self.direction = Vector2(1, 0)
        self.grow = False


    def draw(self):

        for segment in self.body:

            rect = (
                OFFSET + segment.x * cell_size,
                OFFSET + segment.y * cell_size,
                cell_size,
                cell_size
            )

            pygame.draw.rect(
                screen,
                DARK_GREEN,
                rect,
                0,
                7
            )


    def update(self):

        new_head = self.body[0] + self.direction

        self.body.insert(0, new_head)

        if self.grow:

            self.grow = False

        else:

            self.body.pop()


    def reset(self):

        self.body = [
            Vector2(6, 9),
            Vector2(5, 9),
            Vector2(4, 9)
        ]

        self.direction = Vector2(1, 0)


class Food:

    def __init__(self, snake_body):

        self.position = self.generate_random_position(
            snake_body
        )


    def generate_random_cell(self):

        x = random.randint(
            0,
            number_of_cells - 1
        )

        y = random.randint(
            0,
            number_of_cells - 1
        )

        return Vector2(x, y)


    def generate_random_position(self, snake_body):

        position = self.generate_random_cell()

        while position in snake_body:

            position = self.generate_random_cell()

        return position


    def draw(self):

        rect = pygame.Rect(
            OFFSET + self.position.x * cell_size,
            OFFSET + self.position.y * cell_size,
            cell_size,
            cell_size
        )

        pygame.draw.rect(
            screen,
            DARK_GREEN,
            rect
        )


class Game:

    def __init__(self):

        self.snake = Snake()

        self.food = Food(
            self.snake.body
        )

        self.score = 0

        self.game_over = False


    def update(self):

        if self.game_over:
            return

        self.snake.update()

        self.check_food_collision()

        self.check_wall_collision()

        self.check_tail_collision()


    def check_food_collision(self):

        if self.snake.body[0] == self.food.position:

            self.snake.grow = True

            self.score += 1

            self.food.position = (
                self.food.generate_random_position(
                    self.snake.body
                )
            )


    def check_wall_collision(self):

        head = self.snake.body[0]

        if (
            head.x == number_of_cells
            or head.x == -1
            or head.y == number_of_cells
            or head.y == -1
        ):

            self.game_over = True


    def check_tail_collision(self):

        head = self.snake.body[0]

        tail = self.snake.body[1:]

        if head in tail:

            self.game_over = True


    def reset(self):

        self.snake.reset()

        self.food.position = (
            self.food.generate_random_position(
                self.snake.body
            )
        )

        self.score = 0

        self.game_over = False


    def draw(self):

        self.snake.draw()

        self.food.draw()

# CREATE INSTANCE OF GAME

game = Game()


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if game.game_over:

                    game.reset()


            if event.key == pygame.K_UP:

                if game.snake.direction != Vector2(0, 1):

                    game.snake.direction = Vector2(0, -1)


            if event.key == pygame.K_DOWN:

                if game.snake.direction != Vector2(0, -1):

                    game.snake.direction = Vector2(0, 1)


            if event.key == pygame.K_LEFT:

                if game.snake.direction != Vector2(1, 0):

                    game.snake.direction = Vector2(-1, 0)


            if event.key == pygame.K_RIGHT:

                if game.snake.direction != Vector2(-1, 0):

                    game.snake.direction = Vector2(1, 0)

    game.update()


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

    game.draw()


    score_surface = score_font.render(
        str(game.score),
        True,
        DARK_GREEN
    )

    screen.blit(
        score_surface,
        (
            OFFSET,
            OFFSET + cell_size * number_of_cells + 10
        )
    )


    pygame.display.update()

    clock.tick(10)