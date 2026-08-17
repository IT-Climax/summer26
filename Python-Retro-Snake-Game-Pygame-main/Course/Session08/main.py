import pygame, random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake - Session 8")
cell_size, number_of_cells = 30, 20
snake_body, food_position = [(9, 10), (8, 10), (7, 10)], (12, 10)
direction_x, direction_y, score = 1, 0, 0
MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 200)
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: game_running = False
        if event.type == MOVE_SNAKE:
            head_x, head_y = snake_body[0]
            snake_body.insert(0, (head_x + direction_x, head_y + direction_y)); snake_body.pop()
            if snake_body[0] == food_position:  # The head and food share one grid position.
                score += 1
                food_position = (random.randint(0, 19), random.randint(0, 19))
    screen.fill((173, 204, 96))
    pygame.draw.rect(screen, (220, 70, 70), (food_position[0] * cell_size, food_position[1] * cell_size, cell_size, cell_size))
    for body_square in snake_body: pygame.draw.rect(screen, (43, 51, 24), (body_square[0] * cell_size, body_square[1] * cell_size, cell_size, cell_size))
    pygame.display.update()

pygame.quit()
