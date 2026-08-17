# Session 4

## Goal of today's lesson

Today we will move our square with the arrow keys.

## What students will learn

- Keyboard events
- Changing variable values
- Addition and subtraction

## New words

**Keyboard event:** A message that says a key was pressed.

**Condition:** A question with a yes-or-no answer.

**Step size:** How far something moves in one turn.

## Code walkthrough

`step_size = 30` gives every move the same distance. Inside the event loop, `KEYDOWN` asks whether a key was pressed. The four `if event.key` lines recognise arrow keys. Up and left subtract a step; down and right add one. They change the same X and Y variables that the rectangle uses, so the next drawing appears in a new place. The remaining lines are our familiar window loop.

## Challenge

Use the W, A, S, and D keys too.

## What should happen

The dark square moves when you press an arrow key.

## Teacher Tips

Common mistake: using `+` for Up (screen Y grows downward). Ask: “Why does up subtract?” Mini recap: input can change variables, and drawings use the newest values.
