import pygame
import random

pygame.init()

window_width = 600
window_height = 660
cell_size = 30
number_of_cells = 20
background_color = (173, 204, 96)
snake_color = (43, 51, 24)
food_color = (220, 70, 70)
game_over_color = (120, 50, 50)

screen = pygame.display.set_mode((window_width, window_height))  # Make room for the board and score.
pygame.display.set_caption("Retro Snake")
text_font = pygame.font.Font(None, 36)

def make_food_position(snake_body):
    food_position = (random.randint(0, number_of_cells - 1), random.randint(0, number_of_cells - 1))
    while food_position in snake_body:  # Food must appear on an empty square.
        food_position = (random.randint(0, number_of_cells - 1), random.randint(0, number_of_cells - 1))
    return food_position

def start_new_game():
    snake_body = [(9, 10), (8, 10), (7, 10)]
    food_position = make_food_position(snake_body)
    direction_x = 1
    direction_y = 0
    score = 0
    return snake_body, food_position, direction_x, direction_y, score

def draw_square(color, grid_position):
    pixel_x = grid_position[0] * cell_size
    pixel_y = grid_position[1] * cell_size
    pygame.draw.rect(screen, color, (pixel_x, pixel_y, cell_size, cell_size), border_radius=6)

def draw_game(snake_body, food_position, score, game_over):
    screen.fill(game_over_color if game_over else background_color)
    if not game_over:
        draw_square(food_color, food_position)
    for body_square in snake_body:
        draw_square(snake_color, body_square)
    words = "Game over! Press SPACE" if game_over else "Score: " + str(score)
    screen.blit(text_font.render(words, True, snake_color), (15, 615))
    pygame.display.update()

snake_body, food_position, direction_x, direction_y, score = start_new_game()
game_over = False
MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 180)
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                snake_body, food_position, direction_x, direction_y, score = start_new_game()
                game_over = False
            elif event.key == pygame.K_UP and direction_y != 1:
                direction_x, direction_y = 0, -1
            elif event.key == pygame.K_DOWN and direction_y != -1:
                direction_x, direction_y = 0, 1
            elif event.key == pygame.K_LEFT and direction_x != 1:
                direction_x, direction_y = -1, 0
            elif event.key == pygame.K_RIGHT and direction_x != -1:
                direction_x, direction_y = 1, 0
        if event.type == MOVE_SNAKE and not game_over:
            head_x, head_y = snake_body[0]
            new_head = (head_x + direction_x, head_y + direction_y)
            snake_body.insert(0, new_head)
            outside_board = new_head[0] < 0 or new_head[0] >= number_of_cells or new_head[1] < 0 or new_head[1] >= number_of_cells
            touched_tail = new_head in snake_body[1:]
            if outside_board or touched_tail:
                game_over = True
            elif new_head == food_position:
                score += 1
                food_position = make_food_position(snake_body)
            else:
                snake_body.pop()
    draw_game(snake_body, food_position, score, game_over)

pygame.quit()
