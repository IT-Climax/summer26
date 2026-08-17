# Session 11 — Marking Complete & Deleting

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Update and remove specific items using their ID.
- **Topics:** `.filter()`, conditional class names, re-rendering after every change.
- **Features Built:** A checkbox per item toggles `completed`; a "Delete" button removes the item by ID; completed items show with strikethrough styling.
- **Exercises:** Add a "Clear completed" button.
- **Expected Outcome:** Full CRUD (minus saving) works — goals and habits can be added, completed, and deleted.

---

## Teaching Aids & Explanations

### Everyday Analogy
- **Toggling completed**: Like flipping a light switch on or off. If `completed` is currently `false`, clicking turns it to `true`.
- **Deleting with `.filter()`**: Think of passing a basket of apples through a sifter net. If you want to throw away apple #3, your filter rule says: *"Keep every apple whose ID is NOT 3."* All other apples pass through into the new basket, and apple #3 is left behind.

### What the Code Does
`.filter(...)` builds a *new* array containing only the items that pass a test — perfect for deleting, since "delete item with id 3" really means "keep everything except id 3." Each rendered `<li>` gets its own checkbox and delete button, and both are wired with `addEventListener` to functions that know the item's `id`, change the array, then call `renderGoals()` again so the screen updates.

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
        let goals = [];
        let habits = [];
        let nextId = 1;

        const goalList = document.getElementById("goalList");
        const habitList = document.getElementById("habitList");

        function renderGoals() {
            goalList.innerHTML = "";

            for (let i = 0; i < goals.length; i++) {
                const goal = goals[i];
                const li = document.createElement("li");

                // Checkbox to mark this goal complete/incomplete
                const checkbox = document.createElement("input");
                checkbox.type = "checkbox";
                checkbox.checked = goal.completed;
                checkbox.addEventListener("click", function () {
                    toggleGoalComplete(goal.id);
                });

                // Text label for the goal
                const span = document.createElement("span");
                span.textContent = goal.text;
                if (goal.completed) {
                    span.classList.add("completed"); // Add strikethrough style
                }

                // Delete button
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
                if (habit.completed) {
                    span.classList.add("completed");
                }

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

        // Flips a goal's completed status by finding it via its id
        function toggleGoalComplete(id) {
            for (let i = 0; i < goals.length; i++) {
                if (goals[i].id === id) {
                    goals[i].completed = !goals[i].completed; // Flip true/false
                }
            }
            renderGoals();
        }

        // Removes a goal by keeping everything EXCEPT the matching id
        function deleteGoal(id) {
            goals = goals.filter(function (goal) {
                return goal.id !== id;
            });
            renderGoals();
        }

        function toggleHabitComplete(id) {
            for (let i = 0; i < habits.length; i++) {
                if (habits[i].id === id) {
                    habits[i].completed = !habits[i].completed;
                }
            }
            renderHabits();
        }

        function deleteHabit(id) {
            habits = habits.filter(function (habit) {
                return habit.id !== id;
            });
            renderHabits();
        }

        const addGoalBtn = document.getElementById("addGoalBtn");
        const goalInput = document.getElementById("goalInput");

        function handleAddGoal() {
            const typedText = goalInput.value;
            const newGoal = { id: nextId, text: typedText, completed: false };
            nextId = nextId + 1;
            goals.push(newGoal);
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
