# Session 10

## Goal of today's lesson

Today the game will stop when the snake hits a wall.

## What students will learn

- Logical `or`
- A game-over state
- Checking board boundaries

## New words

**Boundary:** The edge that something must not cross.

**State:** A word or value that remembers what condition a game is in.

**Or:** True when at least one question is true.

## Code walkthrough

`game_over = False` starts as “not over.” After a new head is added, the four comparisons check left, right, top, and bottom edges. If any is outside `0` through `19`, the code changes `game_over` to `True`. `and not game_over` stops future timer moves. The screen fill uses one colour while playing and a reddish colour after a crash, giving clear visual feedback. Food and snake drawing stay familiar.

## Challenge

Change the game-over background to purple.

## What should happen

The snake moves and grows, but hitting any edge freezes the game and turns the background reddish.

## Teacher Tips

Common mistake: checking `> 20` instead of `>= 20`. Ask: “What is the last valid grid address?” Mini recap: boundaries protect the board.
