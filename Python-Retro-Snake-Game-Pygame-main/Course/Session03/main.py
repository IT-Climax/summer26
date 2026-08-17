import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake - Session 3")
square_x = 270  # Save the left-to-right position in a named box.
square_y = 270  # Save the up-and-down position in a named box.
square_size = 60
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    screen.fill((173, 204, 96))
    pygame.draw.rect(screen, (43, 51, 24), (square_x, square_y, square_size, square_size))
    pygame.display.update()

pygame.quit()
