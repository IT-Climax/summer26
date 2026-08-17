# Session 2 — Structuring the Page

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Learn common structural/content tags; understand nesting.
- **Topics:** `<h1>`–`<h3>`, `<p>`, `<div>`, `<ul>`/`<li>`, comments.
- **Features Built:** Two sections, "Goals" and "Habits," each with a placeholder list.
- **Exercises:** Add 2 fake goals and 2 fake habits as list items by hand.
- **Expected Outcome:** A static two-section layout resembling the final app's skeleton.

---

## Teaching Aids & Explanations

### Everyday Analogy
Think of nesting HTML elements like **boxes inside boxes**:
- A `<div>` is like a cardboard storage container labeled "Goals" or "Habits".
- Inside the container, you place a label (`<h2>`) and a list folder (`<ul>`).
- Inside the list folder, each individual index card (`<li>`) represents one goal or habit.

### What the Code Does
A `<div>` is a box that groups related things together — we use one for Goals and one for Habits. `<h2>` is a smaller heading, used for section titles inside the page (the `<h1>` stays the single main title). `<ul>` means "unordered list" (a bullet list); each `<li>` is one item in that list. Nesting means putting tags inside other tags — the `<ul>` is nested inside the `<div>`, and each `<li>` is nested inside the `<ul>`.

---

## Session Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Goals Tracker</title>
</head>
<body>

    <h1>My Daily Goals Tracker</h1>
    <p>This app will help me set goals and habits, and track my progress every day.</p>

    <!-- A div is a "box" that groups related things together. -->
    <div>
        <h2>Goals</h2>
        <ul>
            <li>Finish my homework</li>
            <li>Read for 20 minutes</li>
        </ul>
    </div>

    <div>
        <h2>Habits</h2>
        <ul>
            <li>Drink water</li>
            <li>Stretch in the morning</li>
        </ul>
    </div>

</body>
</html>
```
