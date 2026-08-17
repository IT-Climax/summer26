# Session 8 — Arrays: Storing Multiple Goals

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand arrays as lists of data.
- **Topics:** `[]`, `.push()`, indexing, `.length`.
- **Features Built:** Clicking "Add Goal" pushes the typed text into a `goals` array (visible via `console.log`).
- **Exercises:** Do the same for a `habits` array; log the full array after adding 3 items.
- **Expected Outcome:** Data is being collected in memory, even though it isn't shown on screen yet.

---

## Teaching Aids & Explanations

### Everyday Analogy
- **Arrays as a binder/to-do list notebook**: Instead of storing 1 goal in 1 single variable box, an array `goals = []` is like opening a fresh lined notebook binder where you can add as many pages/items as you want.
- **`.push()`**: Dropping a new sheet of paper onto the end of the stack in the binder.
- **Index numbers**: Position numbers on a runner's track starting at `0` (the first runner is `[0]`, the second is `[1]`, etc.).

### What the Code Does
An **array** is a list that can hold many values in order, written with square brackets `[]`. `.push(item)` adds a new item to the end of the array. Each item has an **index** (position number, starting at 0) and `.length` tells us how many items are inside.

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
        // These arrays will hold all of our goals and habits (currently empty)
        let goals = [];
        let habits = [];

        const addGoalBtn = document.getElementById("addGoalBtn");
        const goalInput = document.getElementById("goalInput");

        function handleAddGoal() {
            const typedText = goalInput.value;
            goals.push(typedText); // Add the new goal to the end of the array
            console.log("Current goals:", goals);
            console.log("Number of goals:", goals.length);
            goalInput.value = ""; // Clear the input box after adding
        }

        addGoalBtn.addEventListener("click", handleAddGoal);

        const addHabitBtn = document.getElementById("addHabitBtn");
        const habitInput = document.getElementById("habitInput");

        function handleAddHabit() {
            const typedText = habitInput.value;
            habits.push(typedText);
            console.log("Current habits:", habits);
            habitInput.value = "";
        }

        addHabitBtn.addEventListener("click", handleAddHabit);
    </script>

</body>
</html>
```
