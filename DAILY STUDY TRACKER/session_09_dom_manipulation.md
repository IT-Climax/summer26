# Session 9 — DOM Manipulation: Showing Goals on the Page

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Learn to create and insert real HTML elements from JavaScript.
- **Topics:** `document.createElement`, `.textContent`, `.appendChild`, re-rendering.
- **Features Built:** Adding a goal now creates a real `<li>` on the page (same for habits). The old hard-coded `<li>`s are removed from the HTML — everything now comes from JavaScript.
- **Exercises:** Add an "No goals yet" message that disappears once an item exists.
- **Expected Outcome:** The app visibly adds goals/habits to the page — feels like a real app for the first time.

---

## Teaching Aids & Explanations

### Everyday Analogy
- **DOM as a tree / Lego model**: The DOM (Document Object Model) is the browser's live, in-memory build of the webpage.
- **`document.createElement("li")`**: Opening a new unopened Lego brick out of the bag on your desk (not attached to the house yet).
- **`.textContent`**: Sticking a custom printed sticker onto that Lego brick.
- **`.appendChild(...)`**: Snapping that brick onto the main house model so everyone standing in the room sees it.
- **Render Function pattern**: Wipe the table clean (`innerHTML = ""`), then look at your list of instructions (`goals` array) and snap all the Lego bricks together from scratch.

### What the Code Does
The **DOM** (Document Object Model) is the browser's live, in-memory version of the page — JavaScript can create new pieces of it. `document.createElement("li")` makes a brand new, empty `<li>` element (not yet on the page). `.textContent` sets its text. `.appendChild(...)` attaches it inside a parent element, making it actually appear. This project always follows a **render function** pattern: clear the list, then loop through the array and rebuild it from scratch — that way the screen always matches the data exactly.

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

    <!-- The <ul> elements are now empty - JavaScript fills them in -->
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

        const goalList = document.getElementById("goalList");
        const habitList = document.getElementById("habitList");

        // This function clears the goal list and rebuilds it from the goals array
        function renderGoals() {
            goalList.innerHTML = ""; // Clear everything currently shown

            for (let i = 0; i < goals.length; i++) {
                const li = document.createElement("li");   // Create a new <li>
                li.textContent = goals[i];                  // Put the goal text inside it
                goalList.appendChild(li);                    // Add it to the page
            }
        }

        function renderHabits() {
            habitList.innerHTML = "";
            for (let i = 0; i < habits.length; i++) {
                const li = document.createElement("li");
                li.textContent = habits[i];
                habitList.appendChild(li);
            }
        }

        const addGoalBtn = document.getElementById("addGoalBtn");
        const goalInput = document.getElementById("goalInput");

        function handleAddGoal() {
            const typedText = goalInput.value;
            goals.push(typedText);
            renderGoals();          // Rebuild the list on screen
            goalInput.value = "";
        }

        addGoalBtn.addEventListener("click", handleAddGoal);

        const addHabitBtn = document.getElementById("addHabitBtn");
        const habitInput = document.getElementById("habitInput");

        function handleAddHabit() {
            const typedText = habitInput.value;
            habits.push(typedText);
            renderHabits();
            habitInput.value = "";
        }

        addHabitBtn.addEventListener("click", handleAddHabit);
    </script>

</body>
</html>
```
