# Processing CSV Files

---

# Overview

- Recognize the structure of plain text and CSV files
- Split simple delimited records into fields
- Identify limitations of basic split-based parsing
- Combine file reading, loops, and record processing

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

# Summary

- CSV represents records as rows of separated fields
- A header row can describe the fields in each record
- String.split handles simple delimiters using a regular expression
- Quoted delimiters require more capable CSV parsing
- A reading loop processes records and can branch for different row formats
