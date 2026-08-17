# Session 9

## Goal of today's lesson

Today we will steer the snake and make it grow after eating.

## What students will learn

- Direction rules
- Growing a list
- Preventing an instant turn-around

## New words

**Direction:** The way the snake is travelling.

**Opposite:** Facing completely the other way.

**Grow:** Add one more body square.

## Code walkthrough

The four arrow-key conditions set `direction_x` and `direction_y`. The extra checks, such as `direction_y != 1`, stop the snake turning directly back into itself. The move code always inserts a new head. If food was eaten, it changes the food and does **not** call `pop`; leaving the tail in the list makes the snake longer. Otherwise `pop` keeps its usual length. The score variable counts eaten food for the next lesson's display.

## Challenge

Make the snake start travelling down instead of right.

## What should happen

Arrow keys steer the snake. Each food it eats adds one dark-green square.

## Teacher Tips

Common mistake: allowing the opposite direction. Ask: “What happens if a right-moving snake turns left?” Mini recap: keeping a tail grows the snake.
