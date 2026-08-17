# Daily Goals Tracker — Full Bootcamp Curriculum & Code

**A 13-session HTML/CSS/JavaScript project for beginner students, ages 13–16**

---

## Table of Contents

1. [Project Review](#project-review)
2. [Application Architecture](#application-architecture)
3. [Session 1 — What Is a Website? (HTML Basics)](#session-1)
4. [Session 2 — Structuring the Page](#session-2)
5. [Session 3 — Forms and Buttons](#session-3)
6. [Session 4 — Introduction to CSS](#session-4)
7. [Session 5 — Layout with CSS](#session-5)
8. [Session 6 — JavaScript Basics: Variables and the Console](#session-6)
9. [Session 7 — Functions and Events](#session-7)
10. [Session 8 — Arrays: Storing Multiple Goals](#session-8)
11. [Session 9 — DOM Manipulation: Showing Goals on the Page](#session-9)
12. [Session 10 — Objects and Unique IDs](#session-10)
13. [Session 11 — Marking Complete & Deleting](#session-11)
14. [Session 12 — Local Storage: Saving Progress](#session-12)
15. [Session 13 — Progress Tracking, Polish & "Start New Day"](#session-13)

---

<a id="project-review"></a>
## Project Review

### Strengths

- **Genuinely useful, not a toy**: a goals/habits tracker is something students will actually want to keep using after the bootcamp.
- **Natural CRUD progression**: create → display → complete → delete → persist maps cleanly onto increasing JS complexity.
- **Two parallel entities (goals & habits)**: habits become a repetition exercise once goals are built, reinforcing the pattern.
- **Single-file HTML/CSS/JS**: removes file-navigation and build-tool friction entirely — right for school computers and zero prior experience.
- **Visible daily progress** gives students a satisfying, demo-able feature that's simple to build but feels "real."

### Potential Challenges for Complete Beginners

1. **localStorage + JSON** is the hardest concept in the project and gets its own dedicated session, after arrays and objects are solid.
2. **"Daily" reset logic** is a subtle problem — simplified in this curriculum (see below).
3. **Editing** items is more advanced than early sessions can support — handled as a stretch feature.
4. **DOM manipulation from scratch** (`createElement` vs. `innerHTML`) — this curriculum uses `createElement` throughout.
5. **Unique IDs** for goals/habits — introduced early enough to prevent later bugs.

### Improvements Applied in This Curriculum

- **Editing simplified**: delete-and-re-add in the core path through Session 12; a lightweight Edit feature (using the browser's built-in `prompt()` box) is added in Session 13, giving full create/read/update/delete without the added complexity of inline-editable list items.
- **Daily reset simplified**: a manual "Start New Day" button resets habit completion, instead of real date-comparison logic.
- **`document.createElement` + `appendChild`** used instead of `innerHTML` string-building, to teach the DOM as a tree of real objects.
- **Unique IDs** (a simple incrementing counter) introduced as soon as arrays of objects appear (Session 10).
- **Empty state message** ("No goals yet — add one below!") added as a small conditional-rendering exercise.

### Teaching Approach for Ages 13–16

- Live-code, then students recreate by typing (not copy-pasting).
- Every session ends with something that runs.
- Frequent small wins over big leaps.
- Everyday analogies: variables as "labeled boxes," functions as "recipes," arrays as "to-do lists," objects as "ID cards," events as "a doorbell that runs code when pressed," localStorage as "a notebook the browser keeps even after you close it."
- `console.log` and DevTools introduced early (Session 6) so errors feel visible and normal, not scary.

---

<a id="application-architecture"></a>
## Application Architecture

**Single `index.html` file, three layers stacked top to bottom:**

1. **HTML (structure)** — two sections (Goals, Habits), each with an input + button for adding, and an empty `<ul>` that JavaScript fills in at runtime. A progress summary and a "Start New Day" button sit at the top.
2. **CSS (`<style>` in `<head>`)** — a small set of reusable classes (`.goal-item`, `.completed`, `.btn`, `.container`), flexbox layout, one accent color plus neutrals, mobile-first.
3. **JavaScript (`<script>` before `</body>`)** — organized in the same order every session: (a) data — the `goals`/`habits` arrays, loaded from localStorage at startup; (b) render functions — clear and rebuild the list from the array whenever data changes; (c) event listeners — respond to clicks and call the right data-changing function, which always ends by re-rendering and re-saving.

**Why this fits beginners:** one consistent pattern — "change the data → re-render → save" — repeats through the whole app. Once students learn it for "add," "complete" and "delete" feel like variations, not new topics. Nothing is taught before the feature list actually needs it.

---

<a id="session-1"></a>
## Session 1 — What Is a Website? (HTML Basics)

**Objectives:** Understand HTML as the "skeleton" of a webpage; open and edit a file; view it in a browser.
**Topics:** `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, `<title>`, tags vs. elements.
**Features Built:** A page with a title, a heading, and a short paragraph.
**Exercises:** Change the heading text; add a second paragraph about themselves; try adding an `<h2>` and see what happens.
**Expected Outcome:** A working, personalized HTML page opened in a browser.

### What the code does
Every HTML file has the same skeleton — like the skeleton of a house before walls and paint. `<!DOCTYPE html>` tells the browser "this is a modern page." `<html>` wraps everything. `<head>` holds information *about* the page (like the browser-tab title) that visitors don't see directly. `<body>` holds everything visitors actually see. `<h1>` is the biggest heading — only one per page. `<p>` is a paragraph of normal text. Tags almost always come in pairs: an opening tag and a closing tag with a `/`, wrapping content in between.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Goals Tracker</title>
</head>
<body>

    <!-- 
        This is our main heading. It tells visitors what this page is about.
        <h1> means "Heading, level 1" - the biggest, most important heading on the page.
    -->
    <h1>My Daily Goals Tracker</h1>

    <!-- 
        A paragraph tag holds normal text, just like a paragraph in a book.
    -->
    <p>This app will help me set goals and habits, and track my progress every day.</p>

</body>
</html>
```

---

<a id="session-2"></a>
## Session 2 — Structuring the Page

**Objectives:** Learn common structural/content tags; understand nesting.
**Topics:** `<h1>`–`<h3>`, `<p>`, `<div>`, `<ul>`/`<li>`, comments.
**Features Built:** Two sections, "Goals" and "Habits," each with a placeholder list.
**Exercises:** Add 2 fake goals and 2 fake habits as list items by hand.
**Expected Outcome:** A static two-section layout resembling the final app's skeleton.

### What the code does
A `<div>` is a box that groups related things together — we use one for Goals and one for Habits. `<h2>` is a smaller heading, used for section titles inside the page (the `<h1>` stays the single main title). `<ul>` means "unordered list" (a bullet list); each `<li>` is one item in that list. Nesting means putting tags inside other tags — the `<ul>` is nested inside the `<div>`, and each `<li>` is nested inside the `<ul>`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Goals Tracker</title>
</head>
<body>

    <h1>My Daily Goals Tracker</h1>
    <p>This app will help me set goals and habits, and track my progress every day.</p>

    <!-- A div is a "box" that groups related things together. -->
    <div>
        <h2>Goals</h2>
        <ul>
            <li>Finish my homework</li>
            <li>Read for 20 minutes</li>
        </ul>
    </div>

    <div>
        <h2>Habits</h2>
        <ul>
            <li>Drink water</li>
            <li>Stretch in the morning</li>
        </ul>
    </div>

</body>
</html>
```

---

<a id="session-3"></a>
## Session 3 — Forms and Buttons

**Objectives:** Understand how users will input data.
**Topics:** `<input>`, `<button>`, `placeholder`, the `id` attribute.
**Features Built:** An input box + "Add Goal" button under Goals; the same for Habits.
**Exercises:** Get the form elements on the page with correct `id`s — no functionality yet.
**Expected Outcome:** A page with visible (non-functional) input forms.

### What the code does
An `<input>` is a box the user can type into. `placeholder` shows faint hint text that disappears when typing starts. The `id` attribute gives an element a unique name — this is how JavaScript will find and use it later, so IDs must be spelled exactly and never reused on two elements.

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

---

<a id="session-4"></a>
## Session 4 — Introduction to CSS

**Objectives:** Understand what CSS is and how it attaches to HTML.
**Topics:** `<style>` tag, selectors (tag, class, id), `color`, `font-size`, `font-family`.
**Features Built:** Basic color scheme (2 colors), readable font, centered heading.
**Exercises:** Change the color scheme to their own preference; make the heading bigger.
**Expected Outcome:** The page has a visual identity instead of default browser styling.

### What the code does
CSS lives inside a `<style>` tag in the `<head>`. A **selector** tells the browser *which* elements to style — `body` selects the whole page background/font, `h1` selects the main heading, and `.btn` (a dot means "class") selects any element given `class="btn"`. This project uses one calm blue-green accent color plus soft neutrals, kept deliberately simple for a beginner-friendly, low-distraction interface.

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

---

<a id="session-5"></a>
## Session 5 — Layout with CSS

**Objectives:** Learn to control spacing and arrangement.
**Topics:** `margin`, `padding`, `border`, `box-sizing`, flexbox (`display: flex`), media queries.
**Features Built:** Goals and Habits sections side-by-side on larger screens (stacked on mobile); large, tappable buttons.
**Exercises:** Adjust spacing between elements; experiment with `flex-direction`.
**Expected Outcome:** A clean, mobile-friendly layout matching the design spec (large buttons, clear spacing).

### What the code does
`padding` adds space *inside* a box; `margin` adds space *outside* a box, between it and its neighbors. `display: flex` turns a container into a flexible row (or column) that arranges its children automatically — much easier than manually positioning things. A **media query** (`@media`) applies different CSS only when the screen is narrow, which is how we stack the two sections vertically on a phone but show them side-by-side on a laptop.

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

---

<a id="session-6"></a>
## Session 6 — JavaScript Basics: Variables and the Console

**Objectives:** Understand JS as the "brain" of the page; introduce DevTools console.
**Topics:** `<script>` tag, `let`/`const`, strings/numbers, `console.log`.
**Features Built:** No visible change yet — a practice script that logs messages.
**Exercises:** Store their name and age in variables and log a sentence using them.
**Expected Outcome:** Students see their first output in the console and understand variables as "boxes."

### What the code does
A **variable** is a labeled box that stores a value. `let` creates a box whose contents can change later; `const` creates a box that can never be reassigned. `console.log(...)` prints something to the browser's DevTools console (opened with F12 or right-click → Inspect) — it's invisible to normal visitors, but it's the single most useful tool for seeing what our code is actually doing.

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

---

<a id="session-7"></a>
## Session 7 — Functions and Events

**Objectives:** Understand functions as reusable actions; connect a button click to code.
**Topics:** `function`, parameters, `addEventListener`, the `click` event.
**Features Built:** Clicking "Add Goal" shows the typed text in the console. Same for "Add Habit."
**Exercises:** Make the "Add Habit" button do the same as "Add Goal."
**Expected Outcome:** Buttons are "alive" — first real interactivity.

### What the code does
A **function** is a named, reusable recipe for a set of steps — write it once, run it as many times as needed by calling its name followed by `()`. `document.getElementById("...")` finds an HTML element by its `id`, so JavaScript can read or change it. `addEventListener("click", ...)` tells an element "run this function whenever you get clicked" — like a doorbell wired to a specific action.

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

---

<a id="session-8"></a>
## Session 8 — Arrays: Storing Multiple Goals

**Objectives:** Understand arrays as lists of data.
**Topics:** `[]`, `.push()`, indexing, `.length`.
**Features Built:** Clicking "Add Goal" pushes the typed text into a `goals` array (visible via `console.log`).
**Exercises:** Do the same for a `habits` array; log the full array after adding 3 items.
**Expected Outcome:** Data is being collected in memory, even though it isn't shown on screen yet.

### What the code does
An **array** is a list that can hold many values in order, written with square brackets `[]`. `.push(item)` adds a new item to the end of the array. Each item has an **index** (position number, starting at 0) and `.length` tells us how many items are inside.

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

---

<a id="session-9"></a>
## Session 9 — DOM Manipulation: Showing Goals on the Page

**Objectives:** Learn to create and insert real HTML elements from JavaScript.
**Topics:** `document.createElement`, `.textContent`, `.appendChild`, re-rendering.
**Features Built:** Adding a goal now creates a real `<li>` on the page (same for habits). The old hard-coded `<li>`s are removed from the HTML — everything now comes from JavaScript.
**Exercises:** Add an "No goals yet" message that disappears once an item exists.
**Expected Outcome:** The app visibly adds goals/habits to the page — feels like a real app for the first time.

### What the code does
The **DOM** (Document Object Model) is the browser's live, in-memory version of the page — JavaScript can create new pieces of it. `document.createElement("li")` makes a brand new, empty `<li>` element (not yet on the page). `.textContent` sets its text. `.appendChild(...)` attaches it inside a parent element, making it actually appear. This project always follows a **render function** pattern: clear the list, then loop through the array and rebuild it from scratch — that way the screen always matches the data exactly.

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

---

<a id="session-10"></a>
## Session 10 — Objects and Unique IDs

**Objectives:** Understand objects as a way to bundle related data.
**Topics:** `{}` object literals, dot notation, `{ id, text, completed }`.
**Features Built:** Goals/habits are now stored as objects with a unique `id` and `completed: false`, instead of plain text. Rendering is updated to read `.text`.
**Exercises:** Print a full goal object to the console and identify each property.
**Expected Outcome:** The data structure is upgraded to support completing and deleting specific items.

### What the code does
An **object** bundles several related pieces of data together under one value, written with curly braces `{}`. Each piece is a `property: value` pair, read using a dot, like `goal.text`. We give every goal/habit a unique **id** using a simple counter that goes up by 1 each time — this ID is how we'll find and change the *exact right* item later, even if two goals have the same text.

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

---

<a id="session-11"></a>
## Session 11 — Marking Complete & Deleting

**Objectives:** Update and remove specific items using their ID.
**Topics:** `.filter()`, conditional class names, re-rendering after every change.
**Features Built:** A checkbox per item toggles `completed`; a "Delete" button removes the item by ID; completed items show with strikethrough styling.
**Exercises:** Add a "Clear completed" button.
**Expected Outcome:** Full CRUD (minus saving) works — goals and habits can be added, completed, and deleted.

### What the code does
`.filter(...)` builds a *new* array containing only the items that pass a test — perfect for deleting, since "delete item with id 3" really means "keep everything except id 3." Each rendered `<li>` gets its own checkbox and delete button, and both are wired with `addEventListener` to functions that know the item's `id`, change the array, then call `renderGoals()` again so the screen updates.

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

---

<a id="session-12"></a>
## Session 12 — Local Storage: Saving Progress

**Objectives:** Understand that browser memory is temporary, and how localStorage solves that.
**Topics:** `localStorage.setItem`, `localStorage.getItem`, `JSON.stringify`, `JSON.parse`.
**Features Built:** Goals and habits now persist after closing and reopening the browser.
**Exercises:** Save data, close the tab, reopen it, confirm goals are still there; clear localStorage and watch the app reset.
**Expected Outcome:** The core "save progress" requirement is complete.

### What the code does
`localStorage` is a small notebook the browser keeps for each website, even after the tab is closed. It can only store **text**, not arrays or objects directly — so `JSON.stringify(goals)` turns our array into a text version to save, and `JSON.parse(savedText)` turns that text back into a real array when we load the page. We save after every single change (add, complete, delete), and load once when the page first opens.

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

---

<a id="session-13"></a>
## Session 13 — Progress Tracking, Polish & "Start New Day"

**Objectives:** Add a progress summary feature, an Edit feature, finish daily-reset logic, final polish pass.
**Topics:** Counting completed vs. total items, template strings, `prompt()`, a "Start New Day" button, final CSS pass.
**Features Built:** A progress indicator ("3 of 5 goals completed today"); an "Edit" button per goal/habit that lets students change existing text; "Start New Day" button that resets habit completion only (not goals); final visual polish.
**Exercises:** Personalize colors/fonts; write a comment at the top of the file explaining, in their own words, how the app works.
**Expected Outcome:** A complete, working, saved, personalized Daily Goals & Habits Tracker with full create/read/update/delete functionality.

### What the code does
A **template string** (backticks `` ` ` `` instead of quotes) lets us insert variables directly into text using `${...}`, e.g. `` `${done}/${total} completed` `` — much cleaner than joining strings with `+`. The progress count is calculated with `.filter(...).length` — filter down to only the completed items, then count how many are left. "Start New Day" loops through `habits` and sets every `completed` back to `false`, without touching `goals` at all, giving the daily-habit feel without real date logic.

**Editing** uses `prompt(message, defaultValue)` — a simple browser pop-up box pre-filled with the item's current text. It's the simplest possible way to let a beginner edit something: no extra HTML, no tracking "which item is being edited" on the page. `prompt()` returns the new text if the user clicks OK, or `null` if they click Cancel — the code checks for both `null` and an empty box before saving, so canceling or clearing the box safely does nothing instead of erasing the goal's text.

This is the **complete, final application** — the full single file students end the bootcamp with.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daily Goals Tracker</title>
    <style>
        * { box-sizing: border-box; }

        body {
            font-family: Arial, sans-serif;
            background-color: #F4F7F5;
            color: #223027;
            margin: 0;
            padding: 20px;
        }

        h1 { text-align: center; color: #2F6E51; }
        p { text-align: center; }

        #progressSummary {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        #newDayBtn {
            display: block;
            margin: 0 auto 20px auto;
            width: auto;
            padding: 10px 20px;
        }

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

        ul { list-style: none; padding: 0; }

        li {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 8px 0;
            border-bottom: 1px solid #eeeeee;
        }

        li span { flex: 1; font-size: 16px; }

        .completed {
            text-decoration: line-through;
            color: #888888;
        }

        li button {
            width: auto;
            padding: 6px 10px;
            font-size: 14px;
            background-color: #C0392B;
        }

        li button.edit-btn {
            background-color: #2E86AB;
        }

        .empty-message {
            color: #888888;
            font-style: italic;
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

        @media (max-width: 600px) {
            .container { flex-direction: column; }
        }
    </style>
</head>
<body>

    <h1>My Daily Goals Tracker</h1>
    <p>This app will help me set goals and habits, and track my progress every day.</p>

    <div id="progressSummary"></div>
    <button id="newDayBtn">Start New Day</button>

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
        // ----- DATA -----
        // Load any previously saved goals/habits, or start empty
        let goals = JSON.parse(localStorage.getItem("goals")) || [];
        let habits = JSON.parse(localStorage.getItem("habits")) || [];
        let nextId = JSON.parse(localStorage.getItem("nextId")) || 1;

        function saveData() {
            localStorage.setItem("goals", JSON.stringify(goals));
            localStorage.setItem("habits", JSON.stringify(habits));
            localStorage.setItem("nextId", JSON.stringify(nextId));
        }

        // ----- RENDER FUNCTIONS -----
        const goalList = document.getElementById("goalList");
        const habitList = document.getElementById("habitList");
        const progressSummary = document.getElementById("progressSummary");

        function renderGoals() {
            goalList.innerHTML = "";

            if (goals.length === 0) {
                const message = document.createElement("li");
                message.textContent = "No goals yet — add one below!";
                message.classList.add("empty-message");
                goalList.appendChild(message);
            }

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

                // Edit button - lets the user change the goal's text
                const editBtn = document.createElement("button");
                editBtn.textContent = "Edit";
                editBtn.classList.add("edit-btn");
                editBtn.addEventListener("click", function () {
                    editGoal(goal.id);
                });

                const deleteBtn = document.createElement("button");
                deleteBtn.textContent = "Delete";
                deleteBtn.addEventListener("click", function () {
                    deleteGoal(goal.id);
                });

                li.appendChild(checkbox);
                li.appendChild(span);
                li.appendChild(editBtn);
                li.appendChild(deleteBtn);
                goalList.appendChild(li);
            }
        }

        function renderHabits() {
            habitList.innerHTML = "";

            if (habits.length === 0) {
                const message = document.createElement("li");
                message.textContent = "No habits yet — add one below!";
                message.classList.add("empty-message");
                habitList.appendChild(message);
            }

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

                // Edit button - lets the user change the habit's text
                const editBtn = document.createElement("button");
                editBtn.textContent = "Edit";
                editBtn.classList.add("edit-btn");
                editBtn.addEventListener("click", function () {
                    editHabit(habit.id);
                });

                const deleteBtn = document.createElement("button");
                deleteBtn.textContent = "Delete";
                deleteBtn.addEventListener("click", function () {
                    deleteHabit(habit.id);
                });

                li.appendChild(checkbox);
                li.appendChild(span);
                li.appendChild(editBtn);
                li.appendChild(deleteBtn);
                habitList.appendChild(li);
            }
        }

        // Counts completed vs total across BOTH goals and habits
        function renderProgress() {
            const allItems = goals.concat(habits);
            const totalCount = allItems.length;
            const completedCount = allItems.filter(function (item) {
                return item.completed;
            }).length;

            progressSummary.textContent = `${completedCount}/${totalCount} completed today`;
        }

        function renderAll() {
            renderGoals();
            renderHabits();
            renderProgress();
        }

        // ----- GOAL ACTIONS -----
        function toggleGoalComplete(id) {
            for (let i = 0; i < goals.length; i++) {
                if (goals[i].id === id) goals[i].completed = !goals[i].completed;
            }
            renderAll();
            saveData();
        }

        function deleteGoal(id) {
            goals = goals.filter(function (goal) { return goal.id !== id; });
            renderAll();
            saveData();
        }

        // Lets the user change the text of an existing goal
        function editGoal(id) {
            for (let i = 0; i < goals.length; i++) {
                if (goals[i].id === id) {
                    // prompt() pops up a small box pre-filled with the current text
                    const newText = prompt("Edit your goal:", goals[i].text);

                    // If the user clicked "Cancel", prompt() returns null - do nothing
                    // If the user cleared the box, trim() gives an empty string - do nothing
                    if (newText !== null && newText.trim() !== "") {
                        goals[i].text = newText.trim();
                    }
                }
            }
            renderAll();
            saveData();
        }

        const addGoalBtn = document.getElementById("addGoalBtn");
        const goalInput = document.getElementById("goalInput");

        function handleAddGoal() {
            const typedText = goalInput.value.trim();
            if (typedText === "") return; // Ignore empty input

            const newGoal = { id: nextId, text: typedText, completed: false };
            nextId = nextId + 1;
            goals.push(newGoal);

            renderAll();
            saveData();
            goalInput.value = "";
        }

        addGoalBtn.addEventListener("click", handleAddGoal);

        // ----- HABIT ACTIONS -----
        function toggleHabitComplete(id) {
            for (let i = 0; i < habits.length; i++) {
                if (habits[i].id === id) habits[i].completed = !habits[i].completed;
            }
            renderAll();
            saveData();
        }

        function deleteHabit(id) {
            habits = habits.filter(function (habit) { return habit.id !== id; });
            renderAll();
            saveData();
        }

        // Lets the user change the text of an existing habit
        function editHabit(id) {
            for (let i = 0; i < habits.length; i++) {
                if (habits[i].id === id) {
                    const newText = prompt("Edit your habit:", habits[i].text);

                    if (newText !== null && newText.trim() !== "") {
                        habits[i].text = newText.trim();
                    }
                }
            }
            renderAll();
            saveData();
        }

        const addHabitBtn = document.getElementById("addHabitBtn");
        const habitInput = document.getElementById("habitInput");

        function handleAddHabit() {
            const typedText = habitInput.value.trim();
            if (typedText === "") return;

            const newHabit = { id: nextId, text: typedText, completed: false };
            nextId = nextId + 1;
            habits.push(newHabit);

            renderAll();
            saveData();
            habitInput.value = "";
        }

        addHabitBtn.addEventListener("click", handleAddHabit);

        // ----- START NEW DAY -----
        // Resets only habit completion (not goals), simulating a fresh day
        const newDayBtn = document.getElementById("newDayBtn");

        function handleStartNewDay() {
            for (let i = 0; i < habits.length; i++) {
                habits[i].completed = false;
            }
            renderAll();
            saveData();
        }

        newDayBtn.addEventListener("click", handleStartNewDay);

        // ----- INITIAL RENDER -----
        // Show anything already saved from a previous visit
        renderAll();
    </script>

</body>
</html>
```
