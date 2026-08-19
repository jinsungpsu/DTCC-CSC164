# File Input/Output

---

# This is ALL OOP
- Without understanding OOP, all we can hope for is to memorize/google things every time.

---

# Scanner class
- `Scanner input = new Scanner(System.in);`
- Scanner → class
- input → reference variable
- Scanner() → constructor
- System.in → argument for overloaded constructor
- Standard input
- Instance methods:
  - `nextInt()`
  - `next()`
  - `nextLine()`
  - `nextBoolean()`
  - `nextFloat()`
  - `nextDouble()`
  - `next().charAt(0)`

<!-- footer -->
https://docs.oracle.com/javase/8/docs/api/java/lang/System.html

---

# Different constructor

```java
Scanner fileInput = new Scanner(new File("myfile.txt"));

File myFile = new File("myfile.txt");
Scanner fileInput = new Scanner(myFile);
```

```java
import java.io.File;
import java.util.Scanner;
```

---

# Understanding Relative vs Absolute Paths

## Absolute Path
```java
File file = new File("C:\\Users\\John\\Documents\\data.txt");
Scanner sc = new Scanner(file);
```

## Relative Path
```java
File file = new File("resources/data.txt");
Scanner sc = new Scanner(file);
```

---

# Absolute vs Relative Path

| Feature | Absolute Path | Relative Path |
|---|---|---|
| Portability | ❌ Hard to move across systems | ✅ Works across environments |
| Readability | ❌ Long and cluttered | ✅ Clean and concise |
| Usage Example | Requires full OS-based path | Relative to project folder |

---

# Best Practice

Use relative paths in projects to avoid hardcoding system-specific locations.

Java IDEs like IntelliJ usually treat the root folder as the working directory.

---

# Example Using Scanner

```java
File myFile = new File("sample.txt");
Scanner fileInput = new Scanner(myFile);
String name = fileInput.nextLine();
int age = fileInput.nextInt();
double gpa = fileInput.nextDouble();
System.out.println(name + "\n" + age + "\n" + gpa);
```

![Sample input file](images/sample-input-file.png)

---

# That won't work, though…

![Compilation error](images/file-not-found-error.png)

---

# The fix

![Exception handling fix](images/file-exception-fix.png)

---

# Exceptions

---

# What is an exception?

An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

---

# We've already seen exceptions

```java
int ar[] = {1,2,3,4,5};
for (int i = 0; i <= ar.length; i++)
    System.out.println(ar[i]);
```

---

# Checked vs Unchecked Exceptions

[Diagram showing checked vs unchecked exceptions]

---

# Checked exceptions

- Use `throws`
- Or use a `try-catch` block

---

# Option 1

```java
public static void main(String[] args) throws IOException
```

- Whoever calls this method must handle the exception.

---

# Option 2

```java
try {
    Scanner fileInput = new Scanner(myFile);
} catch (FileNotFoundException e) {
    // do something
}
```

---

# Try and catch

- `try` defines code to test for errors.
- `catch` defines code to execute if an error occurs.

---

# In practice

- The catch block should allow the program to continue safely or exit gracefully.

---

# Multiple Catch Blocks

```java
try {
    // risky code
} catch (IOException e) {
    // handles IOException
} catch (ArithmeticException e) {
    // handles ArithmeticException
} catch (Exception e) {
    // handles any other exceptions
}
```

---

# Throwable superclass

- The `Throwable` class is the superclass of all errors and exceptions in Java.

<!-- footer -->
https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html

---

# Best Practice

- Place the most general exception (`Exception`) at the end.
- General catches can hide useful information.

![Exception ordering](images/exception-ordering.png)

---

# Other Exceptions

- NumberFormatException
- InputMismatchException
- Many more

<!-- footer -->
https://www.w3schools.com/java/java_try_catch.asp

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

# Input File Formatting

---

# Plain text

- Contains only text characters.
- No formatting.
- Can be opened with any text editor.

---

# Comma Separated Values (CSV)

- CSV = Comma-Separated Values.
- Each line is a row.
- Each value is a column.

```text
name,age,city
Alice,30,New York
```

---

# Why Use CSV Files?

- Simple and lightweight
- Easy to read and write
- Compatible with many applications
- Good for structured data

---

# Structure of a CSV File

- First line usually contains headers.
- Remaining lines contain data.
- Commas separate fields.

Things to watch out for:
- Commas inside quotes
- Missing fields
- Different newline characters

---

# Reading a CSV File in Java

```java
String line = "Alice,30,New York";
String[] parts = line.split(",");

System.out.println(parts[0]);
System.out.println(parts[1]);
System.out.println(parts[2]);
```

---

# How the split() Method Works

```java
String csv = "apple,banana,cherry";
String[] fruits = csv.split(",");
```

Result:

```text
["apple", "banana", "cherry"]
```

---

# What is a Regular Expression?

- Pattern used to match text.
- Useful for searching, validating, and splitting.
- `,` matches a comma.
- `\s+` matches whitespace.
- `\d+` matches digits.

<!-- footer -->
https://regexone.com/

---

# Limitations of Basic split()

```java
String line = "John,\"New York, NY\",25";
String[] parts = line.split(",");
```

Output:

```text
["John", "\"New York", " NY\"", "25"]
```

---

# Better CSV Parsing Approaches

- OpenCSV
- Apache Commons CSV

Handles:
- Quoted values
- Escaped characters
- Different delimiters

---

# Split Visualized

```java
String sentence = "hello, world, my, name, is, Alex";
String[] partsOfSentence = sentence.split(",");
```

---

# Split Visualized (2)

```text
partsOfSentence[0]
partsOfSentence[1]
partsOfSentence[2]
partsOfSentence[3]
partsOfSentence[4]
partsOfSentence[5]
```

---

# Reading CSV files- putting it all together

---

# How to read CSV files

- Use Scanner or BufferedReader.
- Use try/catch.
- Handle headers.
- Loop through remaining data.
- Split lines into values.

---

# Using Scanner

```java
Scanner scanner = new Scanner(new File(filePath));
while (scanner.hasNext()) {
    String line = scanner.next();
    String[] values = line.split(",");
}
```

---

# Using BufferedReader

```java
BufferedReader br = new BufferedReader(new FileReader(csvFile));
while ((line = br.readLine()) != null) {
    String[] data = line.split(",");
}
```

---

# Different Rows in CSV

Different row formats can be handled using conditional logic during parsing.

Example:
- If position == "QB", process differently than position == "RB".

---

# Writing to Files

---

# Creating Files

```java
File myObj = new File("filename.txt");
if (myObj.createNewFile()) {
    System.out.println("File created: " + myObj.getName());
}
```

---

# FileWriter class

```java
FileWriter myWriter = new FileWriter("filename.txt");
myWriter.write("Files in Java might be tricky, but it is fun enough!");
myWriter.close();
```

---

# FileWriter constructors

![FileWriter constructors](images/filewriter-constructors.png)

<!-- footer -->
https://docs.oracle.com/javase/7/docs/api/java/io/FileWriter.html

---

# FileWriter Inheritance Chain

![FileWriter inheritance chain](images/filewriter-inheritance-chain.png)

---

# Methods

![Writer methods](images/writer-methods.png)

<!-- footer -->
https://docs.oracle.com/javase/7/docs/api/java/io/Writer.html

---

# BufferedWriter class

- Uses buffering to increase efficiency.

---

# References

- https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html
- https://www.geeksforgeeks.org/array-index-out-of-bounds-exception-in-java/
- https://www.geeksforgeeks.org/checked-vs-unchecked-exceptions-in-java/
- https://www.w3schools.com/java/java_try_catch.asp
- https://www.geeksforgeeks.org/java-io-bufferedreader-class-java/
- https://docs.oracle.com/javase/8/docs/api/java/io/BufferedReader.html
- https://www.geeksforgeeks.org/scanner-class-in-java/
- https://www.w3schools.com/java/java_files_create.asp
- https://www.programiz.com/java-programming/bufferedwriter
