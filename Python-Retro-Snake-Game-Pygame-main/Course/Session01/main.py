import pygame

pygame.init()  # Start pygame before we ask it to make a window.
screen = pygame.display.set_mode((600, 600))  # Make our 600 by 600 pixel window.
pygame.display.set_caption("Snake - Session 1")
game_running = True  # This labelled box remembers whether the game is open.

while game_running:  # Keep showing the window until the player closes it.
    for event in pygame.event.get():  # Check everything that happened since the last turn.
        if event.type == pygame.QUIT:
            game_running = False
    screen.fill((173, 204, 96))  # Paint a calm green background every frame.
    pygame.display.update()  # Put our drawing on the real window.

pygame.quit()  # Tidy up after the loop ends.

