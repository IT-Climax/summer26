import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake - Session 2")
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    screen.fill((173, 204, 96))
    pygame.draw.rect(screen, (43, 51, 24), (270, 270, 60, 60))  # Draw one snake-sized square.
    pygame.display.update()

pygame.quit()
