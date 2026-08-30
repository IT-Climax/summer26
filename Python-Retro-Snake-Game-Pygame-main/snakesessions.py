import pygame
import sys

# -----------------------------
# SNAKE PYGAME SESSION 1
# DUNAMA, SAMUEL, ELVIS PLEASE FOLLOW THIS. I WILL DROP SESSION TWO BEFORE END OF WORK ON MONDAY
# AM BREAKING THE FULL PROJECT TO 4 SESSIONS. MONDAY 30TH AUGUST, 1ST SEPT, 2ND SEPT AND 7TH SEPT. 
# BY THE END OF CLASS ON THE 7TH SEPT EVERY STUDENT SUPPOSED TO HAVE COMPLETE SOURCE CODE FOR THE PROJECT
# -----------------------------

pygame.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 25
OFFSET = 75

screen_width = 2 * OFFSET + cell_size * number_of_cells
screen_height = 2 * OFFSET + cell_size * number_of_cells

screen = pygame.display.set_mode(
    (screen_width, screen_height)
)

pygame.display.set_caption("Retro Snake")

snake_x = 6
snake_y = 9

direction_x = 1
direction_y = 0

clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                direction_x = 0
                direction_y = -1

            if event.key == pygame.K_DOWN:
                direction_x = 0
                direction_y = 1

            if event.key == pygame.K_LEFT:
                direction_x = -1
                direction_y = 0

            if event.key == pygame.K_RIGHT:
                direction_x = 1
                direction_y = 0

    snake_x += direction_x
    snake_y += direction_y

    screen.fill(GREEN)

    # Game board
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
    snake_rect = pygame.Rect(
        OFFSET + snake_x * cell_size,
        OFFSET + snake_y * cell_size,
        cell_size,
        cell_size
    )

    pygame.draw.rect(
        screen,
        DARK_GREEN,
        snake_rect,
        0,
        7
    )

    pygame.display.update()

    clock.tick(10)