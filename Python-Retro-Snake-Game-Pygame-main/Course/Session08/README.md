# Session 8

## Goal of today's lesson

Today the snake will eat food and earn a point.

## What students will learn

- Comparing positions
- `if` and `else`
- Counting with a score variable

## New words

**Compare:** Check whether two things are the same.

**Else:** What the computer does when an `if` answer is no.

**Score:** A number that counts points.

## Code walkthrough

Session 8 adds `score = 0`. After moving, `if snake_body[0] == food_position` compares the head address with the food address. When they match, `score += 1` adds one point and two random numbers choose a replacement food address. This first version still removes the tail every move, so it does not grow yet—that is tomorrow's idea. All drawing and timed movement lines remain from Session 7.

## Challenge

Make each food worth two points.

## What should happen

When the moving snake reaches the food square, the food jumps to a new random place.

## Teacher Tips

Common mistake: comparing the whole list instead of `snake_body[0]`. Ask: “Which square is the snake’s head?” Mini recap: an `if` lets the game react when two positions match.
