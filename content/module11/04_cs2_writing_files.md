# Writing Text Files

---

# Overview

- Create, replace, and append to text files.
- Use FileWriter, BufferedWriter, and try-with-resources.
- Convert objects into CSV rows and save a collection in one pass.
- Follow a JavaFX roster from CSV import through editing and saving.

---

# From Java Data to a Text File

- A writer takes characters and sends them to a destination, such as a file.
- Saving a collection means choosing a text format and writing each record in that format.
- A relative path such as `students.csv` points to a file in the program's working directory. In an IDE, check the run configuration for that directory.
- Java can create the file when it opens a writer. Create any missing parent folders before opening the file.

---

# File and FileWriter

- A `File` represents a pathname. Constructing one gives Java a path to work with.
- `createNewFile()` creates an empty file and returns `false` if one already exists. Use it when you specifically need to create an empty file.
- Opening a `FileWriter` can create the file and prepare it for writing in one step.

```java
try (FileWriter writer = new FileWriter("message.txt")) {
    writer.write("Hello from CSC164!");
} catch (IOException e) {
    System.err.println("Could not save the message. " + e.getMessage());
}
```

These snippets use classes from `java.io`. Import the classes you use.

---

# Replace or Append

| Open the writer | Result if the file exists |
| --- | --- |
| `new FileWriter("roster.txt")` | Clears the old content when opened |
| `new FileWriter("roster.txt", true)` | Writes at the end of the existing file |

- **Replace** when saving a complete roster after edits. Each student should appear once in the new version.
- **Append** when recording a new entry in a log. Make sure existing text ends with a line break before adding another record.
- Both forms can create the file if it is missing. These constructors use the platform's default character encoding.

---

# FileWriter Inheritance Chain

![FileWriter inheritance chain](images/filewriter-inheritance-chain.png)

`FileWriter` inherits the character-writing operations defined by `Writer`.

---

# Writing Text and Line Breaks

- `write("text")` writes the given text. Add a line break when each record needs its own line.
- `write(65)` writes the character `A`. To write the digits `65`, use `write(Integer.toString(65))`.
- `BufferedWriter.newLine()` writes the system's line separator.
- `flush()` sends pending characters to the underlying writer and leaves the writer open. Closing a `BufferedWriter` flushes pending characters and releases the resource.

---

# Buffering and Closing a Writer

A `BufferedWriter` groups small writes so the underlying writer can handle larger chunks. Wrap a `FileWriter` to add buffering and the `newLine()` method.

```java
try (BufferedWriter out =
         new BufferedWriter(new FileWriter("activities.log", true))) {
    out.write("Roster updated");
    out.newLine();
} catch (IOException e) {
    System.err.println("Could not write the log. " + e.getMessage());
}
```

The try-with-resources block closes `out` and its underlying writer when the block exits, including when writing fails.

---

# Writing a CSV Snapshot

- Write the header once, then write one line per object.
- Keep the column order consistent between reading and writing.
- Choose the same encoding on both sides. `Files.newBufferedWriter(path, StandardCharsets.UTF_8)` opens a buffered UTF-8 writer for a new or replacement file.
- For this lecture's simple CSV format, fields contain ordinary text or numbers. A general CSV writer also needs to handle commas, quotes, and line breaks inside fields.

```java
out.write("id,name");
out.newLine();
out.write(101 + "," + "Avery Chen");
out.newLine();
```

---

# Putting It Together: Student Roster

```text
students.csv
    ↓ BufferedReader reads rows and creates Student objects
ArrayList<Student>
    ↕ ObservableList wraps the same ArrayList
ListView<Student>
    ↓ Rename replaces one student through the wrapper
ArrayList<Student>
    ↓ BufferedWriter writes the header and all rows
A new CSV copy
```

`setItems()` connects the view to the observable list. Saving reads the current roster from the backing ArrayList.

---

# Project Setup and Sample Input

In a JavaFX project, place `students.csv` in the working directory. Put `roster.fxml` on the classpath alongside `RosterApp.class`. The example uses the default package. In a named package, add the package prefix to the FXML controller name.

```csv
id,name
101,Avery Chen
102,Morgan Lee
103,Jordan Patel
```

Assume the first row is a header and the remaining rows contain an integer ID and a name. Use names without commas, quotes, or line breaks.

---

# 1. Define the Student Object

Save this as `Student.java`. The ListView displays each object using `toString()`. The writer uses the getters to produce a CSV row.

```java
public class Student {
    private final int id;
    private final String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() { return id; }
    public String getName() { return name; }

    @Override
    public String toString() {
        return id + " - " + name;
    }
}
```

---

# 2. Connect the FXML Controls

The existing TextField supplies the new name. Its `fx:id` connects it to a controller field. The buttons name their event handlers with `onAction`.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.scene.control.Button?>
<?import javafx.scene.control.ListView?>
<?import javafx.scene.control.TextField?>
<?import javafx.scene.layout.VBox?>

<VBox spacing="8" xmlns:fx="http://javafx.com/fxml/1"
      fx:controller="RosterApp$Controller">
    <ListView fx:id="view"/>
    <TextField fx:id="nameField" promptText="New student name"/>
    <Button text="Rename selected student" onAction="#renameSelected"/>
    <Button text="Save a new CSV" onAction="#saveRoster"/>
</VBox>
```

---

# 3. Open the Screen

Combine this Java block and the next three into `RosterApp.java`. The launcher loads the FXML, then tells the controller to load the file. At that point, FXMLLoader has already injected the ListView and TextField.

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class RosterApp extends Application {
    @Override
    public void start(Stage stage) {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("roster.fxml"));
        Parent root;
        try {
            root = loader.load();
        } catch (IOException e) {
            System.err.println("Could not load the roster screen: " + e.getMessage());
            return;
        }
        Controller controller = loader.getController();
        if (!controller.loadRoster()) return;

        stage.setTitle("Student Roster");
        stage.setScene(new Scene(root, 380, 300));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
```

---

# 4. Read the CSV into the ArrayList

Read and skip the header. Each call to `readLine()` gives the next data row, or `null` at the end of the file. Split each row into fields, use them to construct a Student, and add that object to the ArrayList.

```java
    public static class Controller {
        @FXML private ListView<Student> view;
        @FXML private TextField nameField;

        private final ArrayList<Student> roster = new ArrayList<>();
        private final ObservableList<Student> items =
                FXCollections.observableList(roster);

        private boolean loadRoster() {
            Path source = Paths.get("students.csv");
            try {
                BufferedReader in = Files.newBufferedReader(source, StandardCharsets.UTF_8);
                try (in) {
                    in.readLine(); // Skip the header.
                    String line;
                    while ((line = in.readLine()) != null) {
                        String[] fields = line.split(",", 2);
                        int id = Integer.parseInt(fields[0]);
                        roster.add(new Student(id, fields[1]));
                    }
                }
            } catch (IOException e) {
                System.err.println("Could not read the roster: " + e.getMessage());
                return false;
            }
            view.setItems(items);
            return true;
        }
```

`observableList(roster)` wraps the same ArrayList. The initial import fills the ArrayList before the view is connected. Once the view is connected, make edits through `items` so the view gets notified.

---

# 5. Update the Selected Student

Select a student, enter a name in the TextField, and click Rename. `items.set()` replaces the student in the backing ArrayList and tells the ListView to update that row. The new Student keeps the original ID.

```java
        @FXML
        private void renameSelected() {
            int index = view.getSelectionModel().getSelectedIndex();
            if (index < 0) return;

            Student selected = items.get(index);
            items.set(index, new Student(selected.getId(), nameField.getText()));
        }
```

---

# 6. Write the ArrayList to a New CSV

`createTempFile()` creates a uniquely named file in the working directory each time Save runs. The writer adds the header and then one row per student. Check the run console for the exact filename.

```java
        @FXML
        private void saveRoster() {
            try {
                Path target = Files.createTempFile(
                        Paths.get("."), "students-edited-", ".csv");

                BufferedWriter out = Files.newBufferedWriter(target, StandardCharsets.UTF_8);
                try (out) {
                    out.write("id,name");
                    out.newLine();
                    for (Student student : roster) {
                        out.write(student.getId() + "," + student.getName());
                        out.newLine();
                    }
                }
                System.out.println("Saved to " + target.toAbsolutePath());
            } catch (IOException e) {
                System.err.println("Could not save the roster: " + e.getMessage());
            }
        }
    }
}
```

---

# Trace an Edit and Save

1. Run the app and select `102 - Morgan Lee`.
2. Type `Morgan Rivera` in the TextField and click Rename. The ListView should show `102 - Morgan Rivera`.
3. Click Save. Open the new CSV shown in the run console and find the row `102,Morgan Rivera`.
4. Save again to create a second copy. The app still imports `students.csv` at startup.
