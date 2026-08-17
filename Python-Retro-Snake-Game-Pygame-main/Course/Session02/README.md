# Session 2

## Goal of today's lesson

Today we will draw one dark-green square for our future snake.

## What students will learn

- RGB colours
- Pixels
- Calling a drawing function

## New words

**Pixel:** One tiny dot on a screen.

**Function:** A named recipe the computer can follow.

**RGB:** Three numbers that mix red, green, and blue light.

## Code walkthrough

`main.py` keeps every line from Session 1, so the window still opens and closes. The new `pygame.draw.rect` line is inside the loop because drawings are refreshed every frame. `screen` says where to draw, `(43, 51, 24)` is the dark-green colour, and `(270, 270, 60, 60)` means left position, top position, width, and height. It is drawn after `fill`, so the background does not cover it.

## Challenge

Make the square blue or make it twice as wide.

## What should happen

You see one dark-green square in the middle of the green window.

## Teacher Tips

Common mistake: putting `fill` after the square. Ask: “Which instruction gets drawn last?” Mini recap: rectangles need a colour and four position-and-size numbers.
