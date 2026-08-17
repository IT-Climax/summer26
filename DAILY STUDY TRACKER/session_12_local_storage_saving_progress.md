# Session 12 — Local Storage: Saving Progress

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand that browser memory is temporary, and how localStorage solves that.
- **Topics:** `localStorage.setItem`, `localStorage.getItem`, `JSON.stringify`, `JSON.parse`.
- **Features Built:** Goals and habits now persist after closing and reopening the browser.
- **Exercises:** Save data, close the tab, reopen it, confirm goals are still there; clear localStorage and watch the app reset.
- **Expected Outcome:** The core "save progress" requirement is complete.

---

## Teaching Aids & Explanations

### Everyday Analogy
- **RAM vs Storage**: Normal variables live in temporary memory (RAM) — like writing on a classroom whiteboard. When school closes at night (browser tab closes), the janitor erases the whiteboard!
- **`localStorage` as a mini notebook**: `localStorage` is like keeping a small hard-cover pocket notebook inside the browser's desk drawer.
- **`JSON.stringify` & `JSON.parse`**:
  - `JSON.stringify`: Folding up a complex paper origami crane (our JS array of objects) flat so it fits into an envelope (plain text string) to store in the notebook drawer.
  - `JSON.parse`: Unfolding the letter from the envelope back into a 3D origami crane (a live JS array of objects).

### What the Code Does
`localStorage` is a small notebook the browser keeps for each website, even after the tab is closed. It can only store **text**, not arrays or objects directly — so `JSON.stringify(goals)` turns our array into a text version to save, and `JSON.parse(savedText)` turns that text back into a real array when we load the page. We save after every single change (add, complete, delete), and load once when the page first opens.

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
        ul { list-style: none; padding: 0; }

        .completed {
            text-decoration: line-through;
            color: #888888;
        }
        li {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 8px 0;
        }
        li span { flex: 1; font-size: 16px; }
        li button {
            width: auto;
            padding: 6px 10px;
            font-size: 14px;
            background-color: #C0392B;
        }

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
        let nextId = 1;

        // Try to load saved goals/habits; if nothing is saved yet, start with empty arrays
        let goals = JSON.parse(localStorage.getItem("goals")) || [];
        let habits = JSON.parse(localStorage.getItem("habits")) || [];

        // Saves the current goals and habits arrays into localStorage as text
        function saveData() {
            localStorage.setItem("goals", JSON.stringify(goals));
            localStorage.setItem("habits", JSON.stringify(habits));
        }

        const goalList = document.getElementById("goalList");
        const habitList = document.getElementById("habitList");

        function renderGoals() {
            goalList.innerHTML = "";
            for (let i = 0; i < goals.length; i++) {
                const goal = goals[i];
                const li = document.createElement("li");

                const checkbox = document.createElement("input");
                checkbox.type = "checkbox";
                checkbox.checked = goal.completed;
                checkbox.addEventListener("click", function () {
                    toggleGoalComplete(goal.id);
                });

                const span = document.createElement("span");
                span.textContent = goal.text;
                if (goal.completed) span.classList.add("completed");

                const deleteBtn = document.createElement("button");
                deleteBtn.textContent = "Delete";
                deleteBtn.addEventListener("click", function () {
                    deleteGoal(goal.id);
                });

                li.appendChild(checkbox);
                li.appendChild(span);
                li.appendChild(deleteBtn);
                goalList.appendChild(li);
            }
        }

        function renderHabits() {
            habitList.innerHTML = "";
            for (let i = 0; i < habits.length; i++) {
                const habit = habits[i];
                const li = document.createElement("li");

                const checkbox = document.createElement("input");
                checkbox.type = "checkbox";
                checkbox.checked = habit.completed;
                checkbox.addEventListener("click", function () {
                    toggleHabitComplete(habit.id);
                });

                const span = document.createElement("span");
                span.textContent = habit.text;
                if (habit.completed) span.classList.add("completed");

                const deleteBtn = document.createElement("button");
                deleteBtn.textContent = "Delete";
                deleteBtn.addEventListener("click", function () {
                    deleteHabit(habit.id);
                });

                li.appendChild(checkbox);
                li.appendChild(span);
                li.appendChild(deleteBtn);
                habitList.appendChild(li);
            }
        }

        function toggleGoalComplete(id) {
            for (let i = 0; i < goals.length; i++) {
                if (goals[i].id === id) goals[i].completed = !goals[i].completed;
            }
            renderGoals();
            saveData(); // Save every time the data changes
        }

        function deleteGoal(id) {
            goals = goals.filter(function (goal) { return goal.id !== id; });
            renderGoals();
            saveData();
        }

        function toggleHabitComplete(id) {
            for (let i = 0; i < habits.length; i++) {
                if (habits[i].id === id) habits[i].completed = !habits[i].completed;
            }
            renderHabits();
            saveData();
        }

        function deleteHabit(id) {
            habits = habits.filter(function (habit) { return habit.id !== id; });
            renderHabits();
            saveData();
        }

        const addGoalBtn = document.getElementById("addGoalBtn");
        const goalInput = document.getElementById("goalInput");

        function handleAddGoal() {
            const typedText = goalInput.value;
            const newGoal = { id: nextId, text: typedText, completed: false };
            nextId = nextId + 1;
            goals.push(newGoal);
            renderGoals();
            saveData();
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
            saveData();
            habitInput.value = "";
        }

        addHabitBtn.addEventListener("click", handleAddHabit);

        // Show anything already saved from a previous visit
        renderGoals();
        renderHabits();
    </script>

</body>
</html>
```
