# Session 7 — Functions and Events

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand functions as reusable actions; connect a button click to code.
- **Topics:** `function`, parameters, `addEventListener`, the `click` event.
- **Features Built:** Clicking "Add Goal" shows the typed text in the console. Same for "Add Habit."
- **Exercises:** Make the "Add Habit" button do the same as "Add Goal."
- **Expected Outcome:** Buttons are "alive" — first real interactivity.

---

## Teaching Aids & Explanations

### Everyday Analogy
- **Functions as recipes**: A function is like writing down a cooking recipe titled `handleAddGoal()`. Just writing down the recipe doesn't cook the food; the recipe only runs when someone follows the instructions.
- **`addEventListener` as a doorbell**: Wiring up a doorbell outside your house. You tell the front door button: *"Whenever someone presses (clicks) you, chime the bell (run the `handleAddGoal` function)."*

### What the Code Does
A **function** is a named, reusable recipe for a set of steps — write it once, run it as many times as needed by calling its name followed by `()`. `document.getElementById("...")` finds an HTML element by its `id`, so JavaScript can read or change it. `addEventListener("click", ...)` tells an element "run this function whenever you get clicked" — like a doorbell wired to a specific action.

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
        // Find the goal button and goal input using their IDs from the HTML
        const addGoalBtn = document.getElementById("addGoalBtn");
        const goalInput = document.getElementById("goalInput");

        // A function is a reusable recipe. This one runs whenever "Add Goal" is clicked.
        function handleAddGoal() {
            const typedText = goalInput.value; // .value reads what's typed in the input
            console.log("Goal typed: " + typedText);
        }

        // This tells the button: "when you are clicked, run handleAddGoal"
        addGoalBtn.addEventListener("click", handleAddGoal);

        // Same pattern for habits
        const addHabitBtn = document.getElementById("addHabitBtn");
        const habitInput = document.getElementById("habitInput");

        function handleAddHabit() {
            const typedText = habitInput.value;
            console.log("Habit typed: " + typedText);
        }

        addHabitBtn.addEventListener("click", handleAddHabit);
    </script>

</body>
</html>
```
