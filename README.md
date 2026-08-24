# DTCC CSC164 Lecture Slides

Welcome to the CSC164 lecture slide repository.

This site contains lecture materials for:

**CSC164 – Computer Science II**

Slides are provided as interactive Reveal.js presentations and are organized by module.

---

## Accessing the Lectures

Start here:

```text
https://jinsungpsu.github.io/DTCC-CSC164/
```

From the home page, select the lecture you would like to view.

---

## Viewing a Lecture

Each lecture opens as an interactive slide deck.

You may navigate using:

### Keyboard

```text
→ Right Arrow    Next slide
← Left Arrow     Previous slide
Space            Next slide
Esc              Slide overview
F                Fullscreen
S                Presenter View (Speaker Notes)
```

### Toolbar

The toolbar appears at the top of the presentation.

```text
↩  Return to lecture list

◀  Previous slide

▶  Next slide

🔍 Search slides

⛶ Enter Fullscreen

✕ Exit Fullscreen

🖨 Print / Save as PDF
```

---

## Searching Within a Lecture

The Search feature lets you quickly find topics in the current lecture.

Examples:

```text
classes
inheritance
polymorphism
ArrayList
recursion
```

Search is useful when reviewing material before quizzes, exams, and programming assignments.

---

## Fullscreen Mode

For the best viewing experience:

1. Open a lecture.
2. Click the fullscreen button:

```text
⛶
```

or press:

```text
F
```

Fullscreen mode makes code examples and diagrams easier to read.

To exit fullscreen:

```text
✕
```

or press:

```text
Esc
```

---

## Code Examples

Many lectures contain Java code.

Code blocks include syntax highlighting to make examples easier to read and understand.

Example:

```java
ArrayList<String> names = new ArrayList<>();

names.add("Alice");
names.add("Bob");

for(String name : names)
{
    System.out.println(name);
}
```

---

## Mobile Devices

Lectures can be viewed on phones and tablets.

Navigation options:

- Swipe left/right
- Use on-screen controls
- Rotate device to landscape for the best experience

---

## Printing

Certain lectures may be printed or saved as PDF using the toolbar print button.

Printing is intended primarily for note-taking and offline review.

---

## Speaker Notes

Most students can ignore this section.

Speaker Notes are intended for instructors presenting the lecture.

Notes are not visible in the normal presentation view.

### Presenter View

Reveal.js includes a special Presenter View that displays:

- Current slide
- Next slide
- Speaker notes
- Presentation timer
- Clock

Presenter View can be opened by pressing:

```text
S
```

while viewing a presentation.

### Typical Classroom Setup

Instructor Screen:

```text
Current Slide
Next Slide
Speaker Notes
Timer
```

Projector Screen:

```text
Slides Only
```

Students see only the presentation.

### Notes in Lecture Source Files

Speaker notes are stored inside lecture Markdown files.

Example:

```markdown
# Inheritance

Inheritance allows one class to extend another.

Note:
Remind students:
- Discuss "is-a" relationships
- Compare inheritance vs composition
- Show Person/Student example
```

Anything following:

```markdown
Note:
```

appears only in Presenter View.

Students never see these notes.

---

## Technical Information

The site is built using:

- Markdown
- Reveal.js
- GitHub Pages

Lecture content is maintained in Markdown and rendered as interactive presentations.

---

# Writing Lecture Content

This section covers how to create and format lecture slides using Markdown.

## Basic Slide Structure

Each slide is separated by:

```markdown
---
```

Example:

```markdown
# Slide Title

Content goes here.

---

# Next Slide

More content.
```

---

## Two-Column Layouts

You can create multi-column layouts using the `<!-- column -->` marker.

### Basic Two Columns

```markdown
## Two Columns

<!-- column -->
**Left Column**
- Item 1
- Item 2
- Item 3

<!-- column -->
**Right Column**
1. One
2. Two
3. Three
```

### Three or More Columns

```markdown
## Three Columns

<!-- column -->
Column one content.

<!-- column -->
Column two content.

<!-- column -->
Column three content.
```

### Features

- **Auto-detects** number of columns (2, 3, 4+)
- **Columns scroll** if content is too long
- **Images** automatically scale to fit columns
- **Lists** and **code blocks** work inside columns
- **Responsive** and stacks vertically on mobile

### Images in Columns

```markdown
<!-- column -->
images/diagram.jpg

<!-- column -->
- List item 1
- List item 2
```

---

## Footers

Add a footer to any slide using the `<!-- footer -->` marker.

### Basic Footer

```markdown
# Slide Title

Content here.

<!-- footer -->
© 2026 | CSC164 | Computer Science II
```

### Footer Features

- **Centered** at bottom of slide
- **Supports Markdown** (links, bold, italic)
- **Scales** with font settings
- **Auto-spacing** to prevent overlap

---

## Images

Store all images under:

```text
images/
```

Example:

```text
images/oop/inheritance-diagram.png
```

Reference in Markdown:

```markdown
images/oop/inheritance-diagram.png
```

### Image Size Helpers

```markdown
images/small.png{.small}
!Medium Image{.medium}
images/large.png{.large}
```

| Class | Size |
| ------- | ------ |
| `.small` | 30% width |
| `.medium` | 60% width |
| `.large` | 90% width |

---

## Code Blocks

Code blocks include syntax highlighting.

### Java Example

```java
public class Student extends Person
{
    private double gpa;

    public Student(String name, double gpa)
    {
        super(name);
        this.gpa = gpa;
    }
}
```

### Supported Languages

- Java
- Python
- JavaScript
- C++
- HTML/CSS
- And more...

---

## Font Scaling

The entire presentation can be scaled using the `--font-scale` variable in `styles/slides.css`:

```css
:root {
    --font-scale: 1.0;
}
```

### Common Values

```text
--font-scale: 0.8   → 20% smaller
--font-scale: 0.9   → 10% smaller
--font-scale: 1.0   → Normal
--font-scale: 1.1   → 10% larger
--font-scale: 1.2   → 20% larger
--font-scale: 1.3   → 30% larger
```

---

## Complete Slide Example

```markdown
# Object-Oriented Programming

## Inheritance vs Composition

<!-- column -->
**Inheritance**
- IS-A relationship
- Code reuse
- Polymorphism
- Extends existing class

images/inheritance.png

<!-- column -->
**Composition**
- HAS-A relationship
- More flexible
- Promotes encapsulation
- Uses object references

images/composition.png

<!-- footer -->
slides/05_inheritance.md | CSC164 | Spring 2026

---

## Next Topic

Polymorphism and Dynamic Binding
```

---

# Repository Maintenance Notes

The information below is primarily for instructors and future maintainers.

## Repository Structure

```text
DTCC-CSC164-Slides/
│
├── index.html
├── slide.html
├── README.md
│
├── styles/
│   └── slides.css
│
├── module01/
│   ├── 01_course_review.md
│   └── images/
│
├── module02/
│   ├── 01_classes_objects.md
│   └── images/
│
├── module03/
│   ├── 01_inheritance.md
│   └── images/
│
├── module04/
│   ├── 01_polymorphism.md
│   └── images/
│
├── module05/
│   ├── 01_abstract_classes.md
│   └── images/
│
├── module06/
│   ├── 01_interfaces.md
│   └── images/
│
├── module07/
│   ├── 01_gui_intro.md
│   └── images/
│
└── images/
    └── (shared images)
```

---

## Creating a New Lecture

### Step 1

Create a Markdown file:

```text
module03/01_inheritance.md
```

### Step 2

Add slides separated by:

```markdown
---
```

Example:

````markdown
# Inheritance

---

# Benefits of Inheritance

- Reuse code
- Extend functionality
- Support polymorphism

<!-- footer -->
Module 3 | CSC164

---

# Example

```java
public class Student extends Person
{
}
```
