# Event Driven Programming

---

# Procedural Programming
- A procedural program describes how to do something step by step.
- Everything is laid out from start to finish.
- Execution typically starts at `main` and proceeds sequentially.

<!-- footer -->
https://www.reddit.com/r/explainlikeimfive/comments/1mjkis/eli5_the_difference_between_procedural_event/

---

# Object Oriented Programming
- OOP starts by identifying objects and the messages those objects should respond to.
- Programs become collections of interacting objects.

<!-- footer -->
https://medium.com/@zedrick.ara/what-is-oop-eli-5-286a7292e2f9

---

# Event Driven Programming
- Event-driven programs have no clear start or end.
- Program flow is controlled by external events.

<!-- footer -->
https://www.reddit.com/r/explainlikeimfive/comments/1mjkis/eli5_the_difference_between_procedural_event/

---

# Events
- Mouse clicks
- Hover events
- Drag events
- Text entered/changed
- Various UI interactions trigger events.
- Event objects can be passed into event handlers.

---

# Event Handlers
- Methods called when events occur.
- Usually receive an event object.

---

# Binding Event Handler in JavaFX
- Select the object.
- Go to the Code section.
- Find the event.
- Enter the handler method name.

![Binding event handler](images/binding-event-handler.png)

---

# Binding Event Handler in JavaFX
- Don't forget to grab the corresponding Controller code.

![Controller event handler code](images/controller-event-handler-code.png)

---

# ListView Class

---

# ListView
- Similar to an ArrayList for viewing data.
- Uses generic type parameters.

```java
ListView<String> myListView = new ListView<>();
```

<!-- footer -->
https://jenkov.com/tutorials/javafx/listview.html

---

# Adding Items

```java
myListView.getItems().add("hello");
```

<!-- footer -->
https://jenkov.com/tutorials/javafx/listview.html

---

# Removing Items
- Remove by index

```java
myListView.getItems().remove(1);
```

- Remove by range

```java
myListView.getItems().remove(0,2);
```

- Remove by object

```java
myListView.getItems().remove(...);
```

- Clear all

```java
myListView.getItems().clear();
```

---

# ListView Selected Item

```java
String selectedString = myListView.getSelectionModel().getSelectedItem();
```

<!-- footer -->
https://jenkov.com/tutorials/javafx/listview.html

---

# Changing ListView Contents
- Think of ListView as a place to view data.
- View, clear, change, and reload items as needed.

---

# Using an ObservableList

```java
ArrayList<String> itemList = new ArrayList<>();
ObservableList<String> observableItems = FXCollections.observableArrayList(itemList);
ListView<String> listView = new ListView<>();
listView.setItems(observableItems);
```

---

# What is an Observable List?
- It is a class.
- Automatically notifies the UI when contents change.
- ArrayList does not automatically notify the UI.
- ObservableList keeps UI and data synchronized.

---

# Manually Viewing

```java
for (String item : itemList) {
    listView.getItems().add(item);
}
```

---

# Clearing, Refreshing

```java
listView.getItems().clear();
listView.getItems().refresh();
```

---

# Fun with JavaFX

---

# Experiment, Explore

Now that we have the basics down, we can experiment!

---

# BorderPane
- Usually a good starting point for applications.

![BorderPane layout](images/borderpane-layout.png)

<!-- footer -->
https://docs.oracle.com/javase/8/javafx/api/javafx/scene/layout/BorderPane.html

---

# BorderPane with HBox and VBox
- Top/bottom often use HBox.
- Left/right often use VBox.
- Regions can be left empty.

---

# User Input

---

# Buttons
- Buttons are user input and interaction.
- Many additional input controls exist.

---

# Other Inputs/Interactions
- Radio button
- Checkbox
- Sliders
- Much more

---

# Using Getters
- Use getters to determine selected values, checked state, and slider position.

---

# Text Input?
- Text and Label are display elements.
- Use TextField for input.
- Assign an `fx:id`.
- Use `getText()`.

---

# “When” to Read Those Values?
- Typically read values when an event occurs.
- Event handlers process user input.

---

# Typical Form

![Typical JavaFX form](images/typical-form.png)

<!-- footer -->
https://docs.oracle.com/javafx/2/ui_controls/text-field.htm

---

# Other Possible Events
- Many possibilities exist.
- Behavior may not always be what you expect.
- Event processing is extensive.

![Event processing diagram](images/event-processing.png)

<!-- footer -->
https://docs.oracle.com/javafx/2/events/processing.htm

---

# Shapes

- Rectangles
- Circles
- Other shapes

---

# Make Them Move Around
- Use setters.
- Layout containers affect positioning.
- Use AnchorPane as a simple solution.
