# Session 1 — What Is a Website? (HTML Basics)

**Bootcamp Curriculum: Daily Goals & Habits Tracker (Ages 13–16)**

---

## Session Details

- **Objectives:** Understand HTML as the "skeleton" of a webpage; open and edit a file; view it in a browser.
- **Topics:** `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, `<title>`, tags vs. elements.
- **Features Built:** A page with a title, a heading, and a short paragraph.
- **Exercises:** Change the heading text; add a second paragraph about themselves; try adding an `<h2>` and see what happens.
- **Expected Outcome:** A working, personalized HTML page opened in a browser.

---

## Teaching Aids & Explanations

### Everyday Analogy
Think of an HTML document as building the **skeleton of a house**:
- `<!DOCTYPE html>` & `<html>` are the land and foundations.
- `<head>` is the blue-print room containing info *about* the house (like the title on the deed) that visitors don't walk through directly.
- `<body>` is the visible rooms inside the house where people actually live and interact.
- `<h1>` is the main entrance sign over the front door.
- `<p>` represents the normal furniture and text items inside the rooms.

### What the Code Does
Every HTML file has the same skeleton structure. `<!DOCTYPE html>` tells the browser "this is a modern HTML5 page." `<html>` wraps everything. `<head>` holds information *about* the page (like the browser-tab title) that visitors don't see directly. `<body>` holds everything visitors actually see. `<h1>` is the biggest heading — only one per page. `<p>` is a paragraph of normal text. Tags almost always come in pairs: an opening tag (e.g. `<p>`) and a closing tag with a slash (`</p>`), wrapping content in between.

---

## Session Code

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
