# JavaFX Basics

---

# JavaFX Introduction
- JavaFX is a GUI (graphical user interface) library.
- It is a collection of classes used to build graphical programs.
- IntelliJ can automatically configure JavaFX projects.

---

# OOP at work
- **Classes**: JavaFX components such as `Text`, `Pane`, `Button`, and `Scene` are classes.
- **Objects**: Every piece of the interface is an object.
- **Inheritance**: Most visual components inherit from `Node`.
- **Polymorphism**: `getChildren().add()` can add different subclasses of `Node`.

```java
Text text = new Text("Hello World");
```

---

# Inheritance
- Many classes share common features.
- JavaFX classes inherit from Node, Parent, etc.
- Shared functionality is inherited.

---

# Why It Matters
- OOP is how real applications are structured.
- Helps build modular, maintainable code.
- Essential for JavaFX, Android, and Java Collections.

---

# Creating a new project
![JavaFX project setup](images/javafx-project-setup.png)

---

# Be patient…
![Background processes](images/javafx-background-processes.png)

---

# Project structure details
![Project structure](images/project-structure-details.png)

---

# The code… but not really
![Project code view](images/project-code-view.png)

---

# FXML
![FXML overview](images/fxml-overview.png)

---

# FXML
- FXML is a language used to describe the View (UI).
- UI components can also be created directly in Java.

```java
Text text = new Text();
text.setText("Hello World");
```

---

# Controller
![Controller overview](images/controller-overview.png)

---

# FXML, Controllers
- Controllers provide the logic behind GUIs represented in FXML.
- Multiple GUI instances can each have their own data and behavior.

---

# MVC (Model View Controller) Architecture
- Model
- View
- Controller

---

# Model
- Manages data, logic, and rules.
- Think of it as: "What the app does."

---

# Model in JavaFX
- Data is often stored in databases.
- Course examples may use instance or static variables.

---

# View
- Responsible for what the user sees and interacts with.
- Think of it as: "What the app looks like."

---

# View in JavaFX
- UI can be created using Java or FXML.
- CSS can also be used.

---

# Controller
- Handles user input.
- Interacts with the model.
- Updates the view.

---

# Controller in JavaFX
- Just another class.

---

# Why?
- Organized codebase
- Separation of concerns
- Reusability
- Team collaboration

---

# The program
![Program screenshot](images/javafx-program.png)

---

# Stage, Scene, and Layout Containers
![Stage scene layout diagram](images/stage-scene-layout.png)

<!-- footer -->
https://www.tutorialspoint.com/javafx/javafx_application.htm

---

# Stage
A stage (window) contains all the objects of a JavaFX application.

<!-- footer -->
https://www.tutorialspoint.com/javafx/javafx_application.htm

---

# Scene
A scene represents the physical contents of a JavaFX application.

<!-- footer -->
https://www.tutorialspoint.com/javafx/javafx_application.htm

---

# Layout Containers
- HBox
- VBox
- BorderPane
- StackPane
- TextFlow
- AnchorPane
- TilePane
- GridPane
- FlowPane

<!-- footer -->
https://www.tutorialspoint.com/javafx/javafx_layout_panes.htm

---

# So, finally…

```java
primaryStage.setTitle("My First JavaFX App");
Text text = new Text();
text.setText("Hello World");
Pane pane = new Pane();
pane.getChildren().add(text);
Scene scene = new Scene(pane, 400, 200);
primaryStage.setScene(scene);
primaryStage.show();
```

<!-- footer -->
https://www.javaguides.net/2019/07/javafx-hello-world-example-tutorial.html

---

# OOP
- JavaFX is Object-Oriented Programming applied to user interfaces.
- Text, Pane, Scene, and Stage are objects.

---

# OOP Components
- Text, Pane, and Scene are classes.
- Objects expose methods like `setText()` and `getChildren().add()`.
- Objects can contain other objects.
- `primaryStage` is provided by the framework.

---

# Using SceneBuilder

---

# Setting up the IDE
- Use IntelliJ together with SceneBuilder.

<!-- footer -->
https://gluonhq.com/products/scene-builder/

---

# A simpler way to write FXML
- Drag and drop
- A GUI for building GUIs

![SceneBuilder](images/scenebuilder-drag-drop.png)

---

# In the end… it’s all just code (and classes/objects)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?import javafx.scene.layout.Pane?>
<?import javafx.scene.text.Text?>
<Pane>
  <children>
     <Text text="Hello World" />
  </children>
</Pane>
```

---

# Library
![Library panel](images/scenebuilder-library.png)

---

# Hierarchy
![Hierarchy panel](images/scenebuilder-hierarchy.png)

---

# Nesting Objects
![Nesting objects](images/scenebuilder-nesting.png)

---

# Inspector
![Inspector panel](images/scenebuilder-inspector.png)

---

# Layout
![Layout panel](images/scenebuilder-layout.png)

---

# Controller
![Controller settings](images/scenebuilder-controller.png)

---

# Code
![Code panel](images/scenebuilder-code.png)

---

# fx:id
- GUI components need an `fx:id` to be accessed from the Controller.
- The `fx:id` becomes the reference variable.

![fxid assignment](images/scenebuilder-fxid.png)

---

# Sample Controller Skeleton (1)
- Access via View → Show Sample Controller Skeleton.

![Controller skeleton menu](images/controller-skeleton-menu.png)

---

# Sample Controller Skeleton (2)
- Copy generated code back into IntelliJ.

![Controller skeleton example](images/controller-skeleton-example.png)

---

# Where do I put the code?
- Procedural programming starts from `main`.
- Event-driven programming uses event handlers.
- Initialization code still needs a starting location.

---

# Initialize vs Constructor
- Constructors cannot directly access FXML-created objects.
- `initialize()` is called after the FXML file loads.

---

# Initialize method

```java
@FXML
void initialize() {
    titleText.setText("Hello World!");
}
```

---

# Try it yourself! Experiment…
- Download and install SceneBuilder.
- Create a JavaFX project.
- Configure SceneBuilder in IntelliJ.
- Explore UI components.

---

# User Interfaces & User Experience Design

---

# Try this…

https://userinyerface.com/

---

# UI/UX

The concept of UI/UX focuses on layout, appearance, functionality, and design.

---

# What is UX?

“User experience encompasses all aspects of the end-user’s interaction with the company, its services, and its products.”

– Don Norman

---

# What is UI?

A user interface is the point of interaction between the user and a digital device or product.

---

# UI vs UX

- UX is about the overall feel of the experience.
- UI is about how interfaces look and function.

---

# What is Good UI?

- Clarity & Simplicity
- Consistency
- Responsiveness
- Visual Hierarchy
- Accessibility

---

# What is Good UX?

- User-Centered Design
- Efficiency
- Feedback & Interaction
- Error Prevention & Recovery
- Satisfaction

---

# Find Examples
- Good?
- Bad?
- Why?

---

# What is a wireframe?

A two-dimensional skeletal outline of a webpage or app.

---

# Purpose of wireframe

- Keep concepts user-focused.
- Clarify and define features.
- Quick and inexpensive to create.

---

# Some simple tools
- https://app.diagrams.net/
- https://wireframe.cc/
- PowerPoint
- Whiteboard

---

# Resources
- https://careerfoundry.com/en/blog/ux-design/the-difference-between-ux-and-ui-design-a-laymans-guide/
- https://careerfoundry.com/en/blog/ux-design/what-is-a-wireframe-guide/
