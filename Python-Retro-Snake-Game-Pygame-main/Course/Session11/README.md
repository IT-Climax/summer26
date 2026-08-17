# Session 11

## Goal of today's lesson

Today the snake will also stop if it runs into its own tail.

## What students will learn

- Slicing a list
- Checking whether an item is in a list
- Combining collision rules

## New words

**Collision:** When two game things touch the same place.

**Slice:** A smaller part of a list.

**Tail:** Every snake square after the head.

## Code walkthrough

`snake_body[1:]` means “all body squares from item 1 onward,” so it leaves out the head. `new_head in snake_body[1:]` asks whether the head address is already in the tail. Its answer is saved as `touched_tail`. The condition `outside_board or touched_tail` ends the game for either kind of crash. Everything else—food, growth, keyboard direction, and drawing—continues from Session 10.

## Challenge

Can you make a long snake turn into itself on purpose?

## What should happen

The game now stops for both wall crashes and tail crashes.

## Teacher Tips

Common mistake: checking `snake_body[0] in snake_body`, which is always true. Ask: “Why must we leave out the head?” Mini recap: a slice lets us inspect only the tail.
