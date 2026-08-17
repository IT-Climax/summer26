# Session 10 — Objects and Unique IDs

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand objects as a way to bundle related data.
- **Topics:** `{}` object literals, dot notation, `{ id, text, completed }`.
- **Features Built:** Goals/habits are now stored as objects with a unique `id` and `completed: false`, instead of plain text. Rendering is updated to read `.text`.
- **Exercises:** Print a full goal object to the console and identify each property.
- **Expected Outcome:** The data structure is upgraded to support completing and deleting specific items.

---

## Teaching Aids & Explanations

### Everyday Analogy
- **Objects as ID Cards / Passport Cards**: Instead of just writing `"Finish homework"` on a blank piece of paper, an **object** is like creating a structured ID card:
  - `id: 1` (Serial Number / Student ID number)
  - `text: "Finish homework"` (Goal description)
  - `completed: false` (Status stamp — checked or unchecked)
- **Unique IDs**: Imagine two students named "Alex" in a school class. If the teacher calls "Alex", both stand up. But if the teacher calls "Student ID #104", only 1 specific student responds! That's why every goal gets a unique ID number.

### What the Code Does
An **object** bundles several related pieces of data together under one value, written with curly braces `{}`. Each piece is a `property: value` pair, read using a dot, like `goal.text`. We give every goal/habit a unique **id** using a simple counter that goes up by 1 each time — this ID is how we'll find and change the *exact right* item later, even if two goals have the same text.

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
            <ul id="goalList"></ul>
            <input type="text" id="goalInput" placeholder="Type a new goal...">
            <button id="addGoalBtn">Add Goal</button>
        </div>

        <div class="section">
            <h2>Habits</h2>
            <ul id="habitList"></ul>
            <input type="text" id="habitInput" placeholder="Type a new habit...">
            <button id="addHabitBtn">Add Habit</button>
        </div>
    </div>

    <script>
        let goals = [];
        let habits = [];
        let nextId = 1; // A counter used to give every goal/habit a unique ID

        const goalList = document.getElementById("goalList");
        const habitList = document.getElementById("habitList");

        function renderGoals() {
            goalList.innerHTML = "";
            for (let i = 0; i < goals.length; i++) {
                const li = document.createElement("li");
                li.textContent = goals[i].text; // Objects use dot notation to read a property
                goalList.appendChild(li);
            }
        }

        function renderHabits() {
            habitList.innerHTML = "";
            for (let i = 0; i < habits.length; i++) {
                const li = document.createElement("li");
                li.textContent = habits[i].text;
                habitList.appendChild(li);
            }
        }

        const addGoalBtn = document.getElementById("addGoalBtn");
        const goalInput = document.getElementById("goalInput");

        function handleAddGoal() {
            const typedText = goalInput.value;

            // Create an object bundling id, text, and completed status together
            const newGoal = {
                id: nextId,
                text: typedText,
                completed: false
            };
            nextId = nextId + 1;

            goals.push(newGoal);
            console.log("New goal object:", newGoal);
            renderGoals();
            goalInput.value = "";
        }

        addGoalBtn.addEventListener("click", handleAddGoal);

        const addHabitBtn = document.getElementById("addHabitBtn");
        const habitInput = document.getElementById("habitInput");

        function handleAddHabit() {
            const typedText = habitInput.value;
            const newHabit = { id: nextId, text: typedText, completed: false };
            nextId = nextId + 1;
            habits.push(newHabit);
            renderHabits();
            habitInput.value = "";
        }

        addHabitBtn.addEventListener("click", handleAddHabit);
    </script>

</body>
</html>
```
