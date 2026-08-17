# Session 5 — Layout with CSS

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Learn to control spacing and arrangement.
- **Topics:** `margin`, `padding`, `border`, `box-sizing`, flexbox (`display: flex`), media queries.
- **Features Built:** Goals and Habits sections side-by-side on larger screens (stacked on mobile); large, tappable buttons.
- **Exercises:** Adjust spacing between elements; experiment with `flex-direction`.
- **Expected Outcome:** A clean, mobile-friendly layout matching the design spec (large buttons, clear spacing).

---

## Teaching Aids & Explanations

### Everyday Analogy
- **Padding vs Margin**: Imagine a framed picture hanging on a wall. **Padding** is the matting space inside the frame around the photo. **Margin** is the distance between that picture frame and other pictures hanging on the wall.
- **Flexbox**: Think of Flexbox like a **flexible rubber band trays**. Items automatically line up side-by-side or stack neatly without breaking or overlapping.
- **Media Queries**: Like an **automatic transformer**: when on a wide laptop monitor, show 2 columns side-by-side; when on a narrow smartphone screen, stack them into 1 column.

### What the Code Does
`padding` adds space *inside* a box; `margin` adds space *outside* a box, between it and its neighbors. `display: flex` turns a container into a flexible row (or column) that arranges its children automatically — much easier than manually positioning things. A **media query** (`@media`) applies different CSS only when the screen is narrow, which is how we stack the two sections vertically on a phone but show them side-by-side on a laptop.

---

## Session Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Goals Tracker</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #F4F7F5;
            color: #223027;
            margin: 0;
            padding: 20px;
        }

        h1 {
            text-align: center;
            color: #2F6E51;
        }

        p {
            text-align: center;
        }

        /* This container arranges the two sections side by side */
        .container {
            display: flex;
            gap: 20px;
            max-width: 800px;
            margin: 0 auto;
        }

        .section {
            flex: 1;
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 20px;
        }

        input {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            margin-top: 10px;
            border: 2px solid #cccccc;
            border-radius: 6px;
        }

        button {
            width: 100%;
            padding: 14px;
            font-size: 16px;
            margin-top: 10px;
            background-color: #2F6E51;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        /* On small screens, stack the sections instead of side-by-side */
        @media (max-width: 600px) {
            .container {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>

    <h1>My Daily Goals Tracker</h1>
    <p>This app will help me set goals and habits, and track my progress every day.</p>

    <div class="container">
        <div class="section">
            <h2>Goals</h2>
            <ul id="goalList">
                <li>Finish my homework</li>
                <li>Read for 20 minutes</li>
            </ul>
            <input type="text" id="goalInput" placeholder="Type a new goal...">
            <button id="addGoalBtn">Add Goal</button>
        </div>

        <div class="section">
            <h2>Habits</h2>
            <ul id="habitList">
                <li>Drink water</li>
                <li>Stretch in the morning</li>
            </ul>
            <input type="text" id="habitInput" placeholder="Type a new habit...">
            <button id="addHabitBtn">Add Habit</button>
        </div>
    </div>

</body>
</html>
```
