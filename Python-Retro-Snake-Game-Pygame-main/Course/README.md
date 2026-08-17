# Retro Snake: 13-session bootcamp

## Project analysis

The original game is one Python file using **pygame**. Its main loop reads keyboard and close-window events, updates the game every 200 milliseconds, draws the screen 60 times each second, and shows the result. `Snake` stores body squares and direction; `Food` chooses an unused random grid square; `Game` checks food, walls, and the snake's own tail, then holds the score and restart state. The original assets are `Graphics/food.png`, `Sounds/eat.mp3`, and `Sounds/wall.mp3`; pygame is the only dependency.

## Teaching roadmap

1. Open a coloured window.
2. Draw a square.
3. Store a square position.
4. Move a square with arrow keys.
5. Draw a three-square snake.
6. Move the snake automatically.
7. Add random food.
8. Eat food and count points.
9. Grow the snake.
10. Stop at a wall.
11. Stop when the snake meets its tail.
12. Add a score and restart.
13. Polish the finished Retro Snake game.

## Setup

Install Python, then run `pip install pygame`. Open a session folder in a terminal and run `python main.py`. Each folder is independent, so students can revisit any lesson.
