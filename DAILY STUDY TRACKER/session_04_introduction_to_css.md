# Session 4 — Introduction to CSS

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand what CSS is and how it attaches to HTML.
- **Topics:** `<style>` tag, selectors (tag, class, id), `color`, `font-size`, `font-family`.
- **Features Built:** Basic color scheme (2 colors), readable font, centered heading.
- **Exercises:** Change the color scheme to their own preference; make the heading bigger.
- **Expected Outcome:** The page has a visual identity instead of default browser styling.

---

## Teaching Aids & Explanations

### Everyday Analogy
If HTML is the **skeleton**, then CSS is the **clothing, paint, and interior design**:
- HTML says *what* is on the page (headings, text, buttons).
- CSS says *how it should look* (what colors to use, how big the text should be, where it is placed).
- Selectors are like **addressing an envelope**: target `body` to paint the room walls, target `h1` to paint the main sign.

### What the Code Does
CSS lives inside a `<style>` tag in the `<head>`. A **selector** tells the browser *which* elements to style — `body` selects the whole page background/font, `h1` selects the main heading, and `.btn` (a dot means "class") selects any element given `class="btn"`. This project uses one calm blue-green accent color plus soft neutrals, kept deliberately simple for a beginner-friendly, low-distraction interface.

---

## Session Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Goals Tracker</title>
    <style>
        /* This styles the whole page: background color and default font */
        body {
            font-family: Arial, sans-serif;
            background-color: #F4F7F5;
            color: #223027;
        }

        /* This styles our main heading */
        h1 {
            text-align: center;
            color: #2F6E51;
        }

        h2 {
            color: #2F6E51;
        }
    </style>
</head>
<body>

    <h1>My Daily Goals Tracker</h1>
    <p>This app will help me set goals and habits, and track my progress every day.</p>

    <div>
        <h2>Goals</h2>
        <ul id="goalList">
            <li>Finish my homework</li>
            <li>Read for 20 minutes</li>
        </ul>
        <input type="text" id="goalInput" placeholder="Type a new goal...">
        <button id="addGoalBtn">Add Goal</button>
    </div>

    <div>
        <h2>Habits</h2>
        <ul id="habitList">
            <li>Drink water</li>
            <li>Stretch in the morning</li>
        </ul>
        <input type="text" id="habitInput" placeholder="Type a new habit...">
        <button id="addHabitBtn">Add Habit</button>
    </div>

</body>
</html>
```
