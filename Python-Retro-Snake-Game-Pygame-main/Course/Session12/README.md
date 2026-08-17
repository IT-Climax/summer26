# Session 12

## Goal of today's lesson

Today we will show the score and restart the game with Space.

## What students will learn

- A simple function
- Text on a screen
- Restarting values

## New words

**Font:** A style used to draw letters.

**Return:** Send an answer back from a function.

**Restart:** Put the game back at its beginning.

## Code walkthrough

`pygame.font.Font` makes a text tool. `start_game()` is a recipe that returns fresh snake, food, direction, score, and game-over values; calling it at the start avoids repeating those setup lines. On a key event, the Space condition calls the recipe again only after game over. Near the bottom, `str(score)` changes the number into letters, `render` makes the picture of the words, and `blit` places it below the board.

## Challenge

Change the restart key from Space to R.

## What should happen

The bottom of the window shows your score. After a crash it says to press Space, and Space starts a fresh game.

## Teacher Tips

Common mistake: forgetting parentheses when calling `start_game()`. Ask: “Why is a recipe useful here?” Mini recap: functions keep repeated jobs organised.
