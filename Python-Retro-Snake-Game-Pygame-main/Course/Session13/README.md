# Session 13

## Goal of today's lesson

Today we will finish and polish our complete Retro Snake game.

## What students will learn

- Small helper functions
- Friendly names for constants
- Final game testing

## New words

**Constant:** A value we choose once and do not change while the game runs.

**Helper function:** A small recipe that does one useful job.

**Polish:** Small changes that make a project feel finished.

## Code walkthrough

Read `main.py` in order. The imports borrow Pygame and random tools. The next group names the window, grid, and colours so no mysterious numbers are hidden in the game. `screen`, `caption`, and `text_font` prepare drawing tools.

`make_food_position` picks a random grid address and repeats while the address is in `snake_body`; this keeps food off the snake. `start_new_game` creates the first three body squares, calls the food recipe, chooses a rightward direction, resets score, and returns all five starting values. `draw_square` changes one grid address into pixel coordinates before drawing a rounded rectangle. `draw_game` paints the background, food, each body square, score or restart message, and then updates the real window.

The next lines call `start_new_game`, make a `game_over` variable, and make the repeating `MOVE_SNAKE` timer. In the main loop, `QUIT` closes safely. The key conditions either restart with Space or choose a non-opposite direction. On each timer event the code makes and inserts `new_head`, checks wall and tail collisions, grows after food, or removes the tail. The last two lines draw every frame and close Pygame when the loop ends.

## Challenge

Add one obstacle square that ends the game when the head touches it.

## What should happen

You have a complete game: arrow keys steer, food appears safely, the snake grows, score is shown, crashes end the round, and Space restarts.

## Teacher Tips

Common mistakes: changing a function name in one place only, or allowing an opposite turn. Ask: “Which function makes the food safe?” and “Why do we draw every frame?” Mini recap: the final project uses variables, lists, loops, conditions, events, timers, functions, random choices, collisions, text, and restart state.

## Congratulations

You built a whole game from a blank window! You can extend it with obstacles, sound, levels, a high score, a pause menu, different food, or animations.
