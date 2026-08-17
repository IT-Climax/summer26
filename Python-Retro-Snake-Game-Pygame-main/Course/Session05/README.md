# Session 5

## Goal of today's lesson

Today we will draw a snake made from three squares.

## What students will learn

- Lists
- Repeating with `for`
- Grid positions

## New words

**List:** A row of pieces of information kept in order.

**For loop:** A loop that does a job once for every item.

**Grid:** A neat map made from equal squares.

## Code walkthrough

`cell_size` says one grid square is 30 pixels. `snake_body` is a list of three `(x, y)` grid addresses. The `for body_square` line visits each address. Index `[0]` reads its X and `[1]` reads its Y; multiplying by `cell_size` changes grid addresses into pixel addresses. The rectangle line then draws that body square. The event loop and display lines work exactly as before.

## Challenge

Add two more body squares to the left end of the list.

## What should happen

You see a short, three-square dark-green snake.

## Teacher Tips

Common mistake: forgetting to multiply by `cell_size`. Ask: “How many times does the for loop run?” Mini recap: one list and one loop can draw many squares.
