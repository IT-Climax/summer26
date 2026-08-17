# Session 7

## Goal of today's lesson

Today we will put random red food on the board.

## What students will learn

- Using a second library
- Random numbers
- A food position variable

## New words

**Random:** Chosen by chance.

**Library:** A collection of tools; `random` gives us chance tools.

**Position:** The X and Y address of something.

## Code walkthrough

`import pygame, random` borrows both toolboxes. `number_of_cells` says the board is 20 squares across and down. `food_position` uses `random.randint(0, 19)` twice to choose a legal grid address. The new red rectangle is drawn before the snake, using the same grid-to-pixel multiplication as body squares. The rest of the file is Session 6's timed movement.

## Challenge

Make the food yellow and choose a new starting food address.

## What should happen

A red food square appears somewhere on the board while the snake moves.

## Teacher Tips

Common mistake: using 20 as the final random value (that is outside the board). Ask: “Why is 19 the biggest answer?” Mini recap: random numbers can choose a grid location.
