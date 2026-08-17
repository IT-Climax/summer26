import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake - Session 4")
square_x, square_y, square_size = 270, 270, 60
step_size = 30  # One key press moves the square a small, easy-to-see step.
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:  # Only react when a key is first pressed.
            if event.key == pygame.K_UP:
                square_y -= step_size
            if event.key == pygame.K_DOWN:
                square_y += step_size
            if event.key == pygame.K_LEFT:
                square_x -= step_size
            if event.key == pygame.K_RIGHT:
                square_x += step_size
    screen.fill((173, 204, 96))
    pygame.draw.rect(screen, (43, 51, 24), (square_x, square_y, square_size, square_size))
    pygame.display.update()

pygame.quit()
