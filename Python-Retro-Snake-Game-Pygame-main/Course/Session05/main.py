import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake - Session 5")
cell_size = 30
snake_body = [(9, 10), (8, 10), (7, 10)]  # A list keeps every square that makes the snake.
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    screen.fill((173, 204, 96))
    for body_square in snake_body:  # Draw every square in the snake list.
        square_x = body_square[0] * cell_size
        square_y = body_square[1] * cell_size
        pygame.draw.rect(screen, (43, 51, 24), (square_x, square_y, cell_size, cell_size))
    pygame.display.update()

pygame.quit()
