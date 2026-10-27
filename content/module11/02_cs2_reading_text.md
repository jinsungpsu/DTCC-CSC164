# Reading and Parsing Text Files

---

# Overview

- Read text with BufferedReader
- Use loops to process files of unknown length
- Pair Scanner checks with matching read methods
- Convert text into numeric values

---

# BufferedReader class

---

# Very similar to Scanner

- Uses a buffer for efficiency.
- Reads chars and strings.
- Useful for processing text data.

---

# Buffering

![Buffering concept](images/buffering-concept.png)

<!-- footer -->
https://cloudinary.com/blog/how_to_implement_smooth_video_buffering_for_a_better_viewing_experience

---

# BufferedReader Example

```java
import java.io.*;

public class SimpleRead {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(
            new FileReader("example.txt")
        );

        String line = reader.readLine();
        System.out.println(line);
        reader.close();
    }
}
```

---

# Input using a loop

---

# Why use a loop?

- Avoid repeated code.
- File size is often unknown.

---

# General Algorithm for Reading a File

1. Is there something to read?
2. Read it.
3. Repeat.

---

# Example - methods used in pairs

```java
while (scanner.hasNext()) {
    String input = scanner.next();
}

while (scanner.hasNextInt()) {
    int input = scanner.nextInt();
}

while (scanner.hasNextDouble()) {
    double input = scanner.nextDouble();
}
```

---

# Using Scanner

```java
Scanner fileScanner = new Scanner(myFile);
ArrayList<String> fileContents = new ArrayList<>();

while (fileScanner.hasNext()) {
    String line = fileScanner.next();
    fileContents.add(line);
}
```

---

# Using BufferedReader

```java
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
```

---

# String Input Processing

---

# Files Store Data as Text

- File content is read as characters.
- Numbers and booleans are stored as text.
- `BufferedReader.readLine()` returns String values.

---

# Parsing Converts Strings to Data Types

```java
int num = Integer.parseInt(line);
double price = Double.parseDouble(line);
```

---

# Benefits of This Approach

- Keeps reading simple.
- Supports validation.
- Works with mixed-type files.

---

# Summary

- BufferedReader reads characters and lines through a buffer
- File-reading loops continue until no more input remains
- Scanner hasNext methods check for compatible input
- BufferedReader readLine returns null at the end of a file
- Parsing converts strings into data types and may require validation
