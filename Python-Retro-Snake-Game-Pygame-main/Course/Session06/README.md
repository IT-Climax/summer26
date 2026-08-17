# Session 6

## Goal of today's lesson

Today we will make the snake crawl by itself.

## What students will learn

- Timers
- A direction
- Adding and removing list items

## New words

**Timer:** A clock that sends an event after a chosen time.

**Head:** The first square of the snake.

**Insert:** Put an item into a list at a chosen place.

## Code walkthrough

`direction_x, direction_y = 1, 0` means one square right and zero squares down. `MOVE_SNAKE` is our own event name. `set_timer` sends it every 200 milliseconds. When it arrives, the code reads the first list item, adds the direction to make `new_head`, and inserts that at position zero. `pop()` removes the last body item, so the snake moves without becoming longer. The drawing loop is unchanged.

## Challenge

Change the starting direction so the snake begins by moving down.

## What should happen

The three-square snake slides smoothly to the right.

## Teacher Tips

Common mistake: removing the head instead of the tail. Ask: “Why do we insert first and pop last?” Mini recap: movement is a new head plus one less tail.
