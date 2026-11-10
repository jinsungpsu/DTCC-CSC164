# Building a Functional Add/Remove Button System

---

# Overview

- Lay out a TextField, ListView, and buttons in Scene Builder
- Write event handlers that add, remove, and clear items in an ObservableList
- Validate input: empty text, missing selection, and duplicates
- Test the app and avoid common mistakes
- Extend the pattern with edit, move, and mark-complete features

---

# The Real-World Pattern: A Simple Task Manager

This lesson puts together everything you've learned:
- **ListView** + **ObservableList** (automatic UI sync)
- **TextField** (capture user input)
- **Buttons** (trigger events)
- **Event handlers** (react to clicks)

Result: A fully functional add/remove system.

---

# Scene Builder Setup: The Visual Foundation

### Step 1: Create Your Layout
1. Start with a `BorderPane`
2. In the **top** region, add an `HBox`
3. In the **center** region, add your `ListView`
4. In the **bottom** region, add another `HBox` for remove/clear buttons

### Step 2: Add the Controls

**Top HBox:**
- `TextField` (for user input) → `fx:id="inputField"`
- `Button` labeled "Add" → `fx:id="addButton"` → `On Action="onAddClick"`

**Center:**
- `ListView<String>` → `fx:id="myListView"`

**Bottom HBox:**
- `Button` labeled "Remove Selected" → `fx:id="removeButton"` → `On Action="onRemoveClick"`
- `Button` labeled "Clear All" → `fx:id="clearButton"` → `On Action="onClearClick"`

---

# The Complete Controller Code

```java
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import java.net.URL;
import java.util.ResourceBundle;

public class TaskManagerController implements Initializable {
    private ObservableList<String> taskList;
    
    @FXML
    private ListView<String> myListView;
    
    @FXML
    private TextField inputField;
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // Step 1: Create the ObservableList
        taskList = FXCollections.observableArrayList();
        
        // Step 2: Connect it to the ListView
        myListView.setItems(taskList);
    }
    
    @FXML
    private void onAddClick() {
        String task = inputField.getText().trim();
        
        // Validate: Don't add empty strings
        if (!task.isEmpty()) {
            taskList.add(task);        // ← Change the DATA
            inputField.clear();        // Clear the input field
        }
    }
    
    @FXML
    private void onRemoveClick() {
        String selected = myListView.getSelectionModel().getSelectedItem();
        
        // Validate: Make sure something is selected
        if (selected != null) {
            taskList.remove(selected);  // ← Change the DATA
        }
    }
    
    @FXML
    private void onClearClick() {
        taskList.clear();  // ← Empty the entire list
    }
}
```

---

# Code Walkthrough: onAddClick()

```java
@FXML
private void onAddClick() {
    String task = inputField.getText().trim();
    
    if (!task.isEmpty()) {
        taskList.add(task);
        inputField.clear();
    }
}
```

**Line 2:** `getText()` pulls the string from the TextField  
**Line 2:** `.trim()` removes leading/trailing whitespace  

**Line 4:** Check if the string is empty (prevent adding blank items)

**Line 5:** `taskList.add()` — Add to the data list, NOT `myListView.getItems().add()`  
**Line 6:** Clear the TextField so users can type the next item

---

# Code Walkthrough: onRemoveClick()

```java
@FXML
private void onRemoveClick() {
    String selected = myListView.getSelectionModel().getSelectedItem();
    
    if (selected != null) {
        taskList.remove(selected);
    }
}
```

**Line 2:** Get the currently selected item  
→ Returns `null` if nothing is selected

**Line 4:** Always check for `null` before removing  
**Line 5:** Remove from the data list

---

# Code Walkthrough: onClearClick()

```java
@FXML
private void onClearClick() {
    taskList.clear();
}
```

**One line:** Removes everything from the list and the ListView simultaneously.

---

# Edge Cases: What Could Go Wrong?

## Empty Input
**Problem:** User clicks "Add" without typing anything.  
**Solution:** Use `.trim()` and check `.isEmpty()` before adding.

```java
if (!task.isEmpty()) {
    taskList.add(task);
}
```

---

## No Selection on Remove
**Problem:** User clicks "Remove" without selecting an item.  
**Solution:** Check for `null` before removing.

```java
String selected = myListView.getSelectionModel().getSelectedItem();
if (selected != null) {
    taskList.remove(selected);
}
```

---

## Duplicate Entries
**Problem:** User adds the same task twice.  
**Decision:** Do you allow duplicates?

**Option A: Allow duplicates** (current code)
```java
taskList.add(task);  // User can add "Homework" twice
```

**Option B: Prevent duplicates**
```java
if (!taskList.contains(task)) {
    taskList.add(task);
} else {
    // Show an error message or just do nothing
}
```

---

# Testing Your System

### Basic Flow
1. Type "Buy groceries" → Click "Add" → Should appear in ListView
2. Type "Call Mom" → Click "Add" → Should appear below first item
3. Click "Buy groceries" → Click "Remove" → Should disappear
4. Click "Clear All" → Entire list should empty

### Edge Case Testing
1. Click "Add" without typing anything → Nothing should happen
2. Click "Remove" without selecting → Nothing should happen (no crash!)
3. Add the same item twice → Check if your design allows it

---

# Common Mistakes to Avoid

## Mistake #1: Using `myListView.getItems().add()`

```java
// WRONG
@FXML
private void onAddClick() {
    myListView.getItems().add(inputField.getText());
}
```

**Why?** The data list (`taskList`) is out of sync. If you refresh or reload, items disappear.

```java
// RIGHT
@FXML
private void onAddClick() {
    taskList.add(inputField.getText()); 
}
```

---

##  Mistake #2: Forgetting to Check for Empty/Null

```java
// WRONG
@FXML
private void onRemoveClick() {
    taskList.remove(myListView.getSelectionModel().getSelectedItem());  // Crash if null!
}
```

**Why?** Null pointer exception if nothing is selected.

```java
// RIGHT
@FXML
private void onRemoveClick() {
    String selected = myListView.getSelectionModel().getSelectedItem();
    if (selected != null) {
        taskList.remove(selected); 
    }
}
```

---

## Mistake #3: Forgetting to Clear the Input Field

```java
// WRONG
@FXML
private void onAddClick() {
    taskList.add(inputField.getText());
    // User has to manually delete their text!
}
```

**Why?** Poor UX. The user expects the field to clear after they submit.

```java
// RIGHT
@FXML
private void onAddClick() {
    taskList.add(inputField.getText());
    inputField.clear(); 
}
```

---

# Extending the Pattern

Once you master add/remove, you can extend this:

### Edit Functionality
```java
@FXML
private void onEditClick() {
    String selected = myListView.getSelectionModel().getSelectedItem();
    if (selected != null) {
        int index = taskList.indexOf(selected);
        taskList.set(index, inputField.getText());  // Replace item
        inputField.clear();
    }
}
```

### Move Up/Down
```java
@FXML
private void onMoveUp() {
    int selectedIndex = myListView.getSelectionModel().getSelectedIndex();
    if (selectedIndex > 0) {
        String item = taskList.get(selectedIndex);
        taskList.remove(selectedIndex);
        taskList.add(selectedIndex - 1, item);
    }
}
```

### Mark Complete
```java
@FXML
private void onMarkComplete() {
    String selected = myListView.getSelectionModel().getSelectedItem();
    if (selected != null) {
        taskList.set(taskList.indexOf(selected), selected + " ✓");
    }
}
```

---

# Summary

1. **Scene Builder wires the UI** → TextField, ListView, Buttons
2. **Controller creates the data list** → `initialize()` sets up the ObservableList
3. **Event handlers modify the data** → Always change `taskList`, not `myListView`
4. **Validation prevents crashes** → Check for empty strings and null selections
5. **The UI stays in sync** → Because ObservableList broadcasts changes

This pattern is the **foundation for any data-entry application** you'll build.

---

<!-- references -->
- https://docs.oracle.com/javase/8/javafx/api/javafx/collections/FXCollections.html
- https://docs.oracle.com/javase/8/javafx/api/javafx/scene/control/ListView.html
- https://docs.oracle.com/javase/8/javafx/api/javafx/scene/control/TextField.html
