import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake - Session 6")
cell_size = 30
snake_body = [(9, 10), (8, 10), (7, 10)]
direction_x, direction_y = 1, 0  # The snake begins by travelling right.
MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 200)  # Ask pygame for one movement event every fifth of a second.
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == MOVE_SNAKE:
            head_x, head_y = snake_body[0]
            new_head = (head_x + direction_x, head_y + direction_y)
            snake_body.insert(0, new_head)  # Put the new head at the front.
            snake_body.pop()  # Remove the last square so its length stays the same.
    screen.fill((173, 204, 96))
    for body_square in snake_body:
        pygame.draw.rect(screen, (43, 51, 24), (body_square[0] * cell_size, body_square[1] * cell_size, cell_size, cell_size))
    pygame.display.update()

pygame.quit()
