# Session 1

## Goal of today's lesson

Today we will open our first game window and give it a green background.

## What students will learn

- How to start Pygame
- A loop that keeps a window open
- How to close a program safely

## New words

**Library:** A box of ready-made computer tools. Pygame gives us game tools.

**Loop:** Instructions the computer repeats again and again.

**Event:** Something that happens, such as clicking the close button.

## Code walkthrough

Open `main.py` and read it from top to bottom. `import pygame` borrows the game tools. `pygame.init()` wakes them up. The next two lines make and name the window. `game_running` is a variable that remembers whether the loop should continue. Inside `while`, `pygame.event.get()` checks for events; the `QUIT` event changes the variable to `False`. `fill` paints the background each turn, and `update` shows it. The final `quit` tidies up.

## Challenge

Change the background to your favourite colour.

## What should happen

A 600 by 600 green window opens and stays open until you close it.

## Teacher Tips

Common mistake: forgetting `pygame.display.update()`. Ask: “Why does the loop need to repeat?” Mini recap: Pygame starts, the loop listens, then it draws.
