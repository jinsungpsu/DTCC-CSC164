# CSC164 Exam 4 Review

---

# Exam Instructions/Policies

This assessment is closed resource (no notes, powerpoint, textbook, internet, etc.). If you open another internet browser or tab, it will be considered cheating. You may not leave the testing area for any reason. If you have any extenuating circumstances that may require any exceptions, please let the instructor/proctor know as soon as you can.

This assessment MUST be completed using D2L on a lab computer during the scheduled time and location; you may not use your own device or take this assessment at a different location without prior approval.

---

# Exam Format and Review Priorities

- 25 questions in D2L at 4 points each
- Multiple choice and select all that apply
- Practice explaining how a JavaFX interface is built and what happens when a user interacts with it.
- Practice tracing Java code that reads input, parses data, and handles exceptions.

---

# Procedural and Event-Driven Programming

- **Procedural flow:** The program controls the order of operations. A console program might prompt for a name, read it, and print a greeting.
- **Event-driven flow:** Events determine which code runs and when. A JavaFX app might wait for a user to click Save, then run the registered handler.
- An event handler can still execute a sequence of instructions. The event determines when that sequence starts.

---

# MVC and Object-Oriented GUIs

- **Model:** Holds application data and business rules.
- **View:** Displays information and provides controls for the user.
- **Controller:** Handles user actions, coordinates changes to the model, and updates the view as needed.
- JavaFX represents buttons, fields, and windows as objects. Reusable components and classes with clear responsibilities help you maintain and extend a complex GUI.

---

# OOP Principles to Study

- **Abstraction:** Expose essential operations and hide implementation details. A caller uses a list's add method without needing to know how the list stores items.
- **Encapsulation:** Bundle state with behavior and control access. Keep a balance field private and change it through methods that enforce the rules.
- **Inheritance:** A subclass acquires accessible behavior from a superclass and can extend or customize it.
- **Polymorphism:** Code can use a shared type while different objects supply their own behavior through overriding.

---

# Review: Events and MVC

### In a grade-entry app, which part handles the Save click, which part enforces the valid grade range, and which part shows the result?

<div class="fragment">

**Controller:** Handles the click. **Model:** Enforces the grade rule. **View:** Shows the result.

</div>

<div class="fragment">

The click triggers the handler, so this interaction is event-driven.

</div>

---

# Building a JavaFX Interface

- **Java code:** Construct JavaFX controls and layout panes, then assemble them in code.
- **Handwritten FXML:** Describe the interface structure, layout, and initial property values in markup.
- **Scene Builder:** Visually design or edit the interface and save the result as FXML.
- A Java controller handles events and connects the interface to application data. FXML can name that controller and refer to its handler methods.

---

# JavaFX Windows and Layout

- A **Stage** represents a window. Its **Scene** holds the interface through a root node.
- An **HBox** arranges children in a horizontal row. Use it for a footer with copyright text and links on one line.
- A **VBox** arranges children in a vertical column. Use it to stack buttons in a left navigation bar.
- The parent layout determines where the row or column goes. A BorderPane, for example, can put the HBox at the bottom and the VBox at the left.

---

# FXML Injection and Controller Initialization

- Match a control's fx:id in FXML to a controller field. Annotate a private field with @FXML so the loader can inject the control.
- FXMLLoader constructs the interface, injects the fields, and then calls the controller's initialize() automatically.
- Use initialize() to configure controls that have already been injected. The controller constructor runs before injection.
- Initialization is part of loading FXML. It can finish before the root is put in a Scene or the Stage is shown.

---

# JavaFX Controls: Reading and Updating Text

- Set a Label's initial text in Scene Builder or by editing its text attribute in FXML.
- To change a Label while the app runs, call setText() on the injected Label reference.
- To read what the user typed in a TextField, call getText() on that TextField.

```java
@FXML private TextField nameField;
@FXML private Label greetingLabel;

@FXML
private void showGreeting() {
    String name = nameField.getText();
    greetingLabel.setText("Hello, " + name);
}
```

---

# JavaFX Controls: Typed Lists

- ListView<T> uses a generic type to specify which items it displays, much like ArrayList<T> specifies which items it stores.
- ListView<String> displays strings. ListView<Student> can display custom Student objects.
- A ListView is a UI control. Its items list holds the data displayed by the control.

```java
ListView<String> courses = new ListView<>();
courses.getItems().add("CSC164");
```

---

# Review: JavaFX Layout and Controls

### A photo gallery has Previous and Next buttons side by side. Under each photo, it stacks a title above a caption. How would you group those controls?

```text
      +----------------------+
      |        Photo         |
      +----------------------+
            Sunset Trail
        A view from the ridge

      [ Previous ]  [ Next ]
```

<div class="fragment">

Use an **HBox** to group Previous and Next in a row. Use a **VBox** to stack the title and caption.

</div>

---

# UI, UX, and Wireframes

- **UI:** The screens, controls, and interactions the user works with.
- **UX:** The overall experience of using the product, including how easy or frustrating it is to accomplish a task.
- **Wireframe:** A quick, inexpensive sketch of where content and controls go and what users can do on each screen.
- Sketch the basic layout before spending time on exact colors, fonts, or a detailed mockup or interactive prototype.

---

# Checked and Unchecked Exceptions

- A **checked exception** such as IOException or FileNotFoundException must be caught or declared with throws when it can escape the method.
- An **unchecked exception** such as IndexOutOfBoundsException can escape without a catch or a throws declaration.
- RuntimeException extends Exception. Its subclasses are unchecked. The Error branch of Throwable is also unchecked and sits outside Exception.
- FileNotFoundException extends IOException, so catching IOException also handles FileNotFoundException.

---

# Multiple Catch Blocks

- One try block can have several catch clauses. Java runs the first matching clause.
- Put a specific type before a superclass that would also match it. Putting the superclass first makes the later specific clause unreachable.
- catch (Exception e) can handle many exception types, including checked exceptions and runtime exceptions.
- A plain try statement needs a catch or finally. Try-with-resources can stand on its own, but checked exceptions still need to be caught or declared if they can escape.

---

# Review: Handling a Failed Import

### An import screen should ask the user to choose another file when the selected file cannot be opened. Why might the import controller handle the exception itself?

<div class="fragment">

The controller can catch FileNotFoundException, show a message, and let the user try again. A lower-level file-reading method can declare throws FileNotFoundException so the controller can make that recovery decision.

</div>

---

# File Paths and Scanner Input

- An **absolute path** starts at a filesystem root, such as C:/data/courses.csv on Windows. It identifies the same location regardless of the current working directory.
- A **relative path** such as data/courses.csv is resolved from the program's current working directory. Relative paths can improve portability when the expected folder structure is preserved.
- new Scanner(System.in) reads standard input, usually the keyboard. The overloaded constructor new Scanner(new File(path)) reads from a file.
- Scanner reads input. Use a writer when you need to produce file output.

---

# Scanner: Check Before Reading

- hasNext() checks whether another token is available and leaves it unread.
- next() consumes the token. Calling next() when input is exhausted can throw NoSuchElementException.
- For line-based input, such as one CSV record per line, pair hasNextLine() with nextLine().

```java
while (input.hasNext()) {
    String token = input.next();
    System.out.println(token);
}
```

---

# Parsing Simple CSV Rows

- line.split(",") separates simple comma-delimited fields and returns a String[].
- Call trim() on each field when the input may include surrounding spaces.
- If the file has a header, skip it explicitly before reading data rows.
- Use this pattern for simple data without commas inside quoted fields.

```java
String line = "CSC164, Java Programming";
String[] fields = line.split(",");
String courseCode = fields[0].trim();
String title = fields[1].trim();
```

---

# Review: Tracing File Input

### A program must read a portable file path, skip a known header, and extract each course code. What does the code do at each step?

```java
try (Scanner input = new Scanner(new File("data/courses.csv"))) {
    if (input.hasNextLine()) {
        input.nextLine();
    }
    while (input.hasNextLine()) {
        String[] fields = input.nextLine().split(",");
        System.out.println(fields[0].trim());
    }
} catch (FileNotFoundException e) {
    System.out.println("Could not open the course file.");
}
```

<div class="fragment">

The path is relative to the working directory. The first nextLine() consumes the expected header if the file has any lines. The loop reads each remaining line, splits it at commas, trims the first field, and prints it. The catch handles a failure to open the file.

</div>
