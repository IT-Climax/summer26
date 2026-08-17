# Session 6 — JavaScript Basics: Variables and the Console

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand JS as the "brain" of the page; introduce DevTools console.
- **Topics:** `<script>` tag, `let`/`const`, strings/numbers, `console.log`.
- **Features Built:** No visible change yet — a practice script that logs messages.
- **Exercises:** Store their name and age in variables and log a sentence using them.
- **Expected Outcome:** Students see their first output in the console and understand variables as "boxes."

---

## Teaching Aids & Explanations

### Everyday Analogy
- **Variables as labeled boxes**: Imagine a clear plastic storage box. You stick a label on the front that says `appName`, and put the piece of paper `"Daily Goals Tracker"` inside.
- **`let` vs `const`**: `let` is a standard cardboard box with a removable lid — you can swap what's inside whenever you want. `const` is a glass display case with a padlocked lid — once you put something inside, you can never replace it.
- **`console.log()`**: Like sending a text message or secret memo to your internal developer walkie-talkie — visitors to the website can't see it on the page, but developers can see it in DevTools (F12).

### What the Code Does
A **variable** is a labeled box that stores a value. `let` creates a box whose contents can change later; `const` creates a box that can never be reassigned. `console.log(...)` prints something to the browser's DevTools console (opened with F12 or right-click → Inspect) — it's invisible to normal visitors, but it's the single most useful tool for seeing what our code is actually doing.

---

## Session Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Goals Tracker</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background-color: #F4F7F5; color: #223027; margin: 0; padding: 20px; }
        h1 { text-align: center; color: #2F6E51; }
        p { text-align: center; }
        .container { display: flex; gap: 20px; max-width: 800px; margin: 0 auto; }
        .section { flex: 1; background-color: #FFFFFF; border-radius: 10px; padding: 20px; }
        input { width: 100%; padding: 12px; font-size: 16px; margin-top: 10px; border: 2px solid #cccccc; border-radius: 6px; }
        button { width: 100%; padding: 14px; font-size: 16px; margin-top: 10px; background-color: #2F6E51; color: white; border: none; border-radius: 6px; cursor: pointer; }
        @media (max-width: 600px) { .container { flex-direction: column; } }
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

    <script>
        // A variable is a labeled box that stores a value.
        // "let" means the value inside the box can change later.
        let appName = "Daily Goals Tracker";

        // "const" means this box's value can never be reassigned.
        const creator = "Bootcamp Student";

        // console.log prints a message to the DevTools console (press F12 to see it).
        console.log("Welcome to " + appName + ", built by " + creator + "!");
    </script>

</body>
</html>
```
