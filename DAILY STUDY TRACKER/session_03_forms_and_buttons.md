# Session 3 — Forms and Buttons

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand how users will input data.
- **Topics:** `<input>`, `<button>`, `placeholder`, the `id` attribute.
- **Features Built:** An input box + "Add Goal" button under Goals; the same for Habits.
- **Exercises:** Get the form elements on the page with correct `id`s — no functionality yet.
- **Expected Outcome:** A page with visible (non-functional) input forms.

---

## Teaching Aids & Explanations

### Everyday Analogy
- An `<input>` is like an **empty blank text box** on a paper form where you write your answer.
- The `placeholder` is like **faint gray sample text** printed inside the box to show you what to write (e.g., "Type a new goal...").
- An `id` is like a **unique name tag or serial number** attached to that specific box so code can identify it later without getting confused.

### What the Code Does
An `<input>` is a box the user can type into. `placeholder` shows faint hint text that disappears when typing starts. The `id` attribute gives an element a unique name — this is how JavaScript will find and use it later, so IDs must be spelled exactly and never reused on two elements.

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

    <div>
        <h2>Goals</h2>
        <ul id="goalList">
            <li>Finish my homework</li>
            <li>Read for 20 minutes</li>
        </ul>

        <!-- The id gives this input a name so JavaScript can find it later -->
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
