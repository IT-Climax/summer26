import pygame, random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake - Session 11")
cell_size, number_of_cells = 30, 20
snake_body, food_position = [(9, 10), (8, 10), (7, 10)], (12, 10)
direction_x, direction_y, score, game_over = 1, 0, 0, False
MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 200)
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction_y != 1: direction_x, direction_y = 0, -1
            if event.key == pygame.K_DOWN and direction_y != -1: direction_x, direction_y = 0, 1
            if event.key == pygame.K_LEFT and direction_x != 1: direction_x, direction_y = -1, 0
            if event.key == pygame.K_RIGHT and direction_x != -1: direction_x, direction_y = 1, 0
        if event.type == MOVE_SNAKE and not game_over:
            head_x, head_y = snake_body[0]; snake_body.insert(0, (head_x + direction_x, head_y + direction_y))
            head_x, head_y = snake_body[0]
            outside_board = head_x < 0 or head_x >= number_of_cells or head_y < 0 or head_y >= number_of_cells
            touched_tail = snake_body[0] in snake_body[1:]  # Compare the head with every other square.
            if outside_board or touched_tail: game_over = True
            elif snake_body[0] == food_position:
                score += 1; food_position = (random.randint(0, 19), random.randint(0, 19))
            else: snake_body.pop()
    screen.fill((120, 50, 50) if game_over else (173, 204, 96))
    if not game_over: pygame.draw.rect(screen, (220, 70, 70), (food_position[0] * cell_size, food_position[1] * cell_size, cell_size, cell_size))
    for body_square in snake_body: pygame.draw.rect(screen, (43, 51, 24), (body_square[0] * cell_size, body_square[1] * cell_size, cell_size, cell_size))
    pygame.display.update()

pygame.quit()
