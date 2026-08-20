# Output Formatting
## Making things look pretty
<!-- footer -->
Delaware Technical Community College

---

# Output formatting
- print
    - regular output
- println
    - output followed by printing a \n (new line)
- printf
    - formatted output

---

# print()
  - Displays text
  - Cursor stays on the same line

```java
System.out.print("Hello");
System.out.print(" World");
```

Output:

```text
Hello World
```

---
# println()

  - Displays text
  - Automatically moves to the next line

```java
System.out.println("Hello");
System.out.println("World");
```

Output:

```text
Hello
World
```

---

# printf()
  - Formatted output
  - Uses placeholders called format specifiers

```java
String name = "Jin";
int age = 21;

System.out.printf("%s is %d years old", name, age);
```

Output:

```text
Jin is 21 years old
```

---

# Formatting Decimal Numbers

<!-- column -->

```java
double a = 3.14159265359;

System.out.printf("%f\n", a);
System.out.printf("%5.3f\n", a);
System.out.printf("%5.2f\n", a);
```

Format Specifier Syntax:

```java
%[width].[precision]f
```

<!-- column -->


Example:

```text
%5.2f
││ │└─ f = floating-point
││ └── 2 digits after decimal
│└──── minimum width = 5
└───── start format specifier
```

Output:

```text
3.141593
3.142
 3.14
```

<!-- footer -->
https://www.geeksforgeeks.org/formatted-output-in-java/

---

# Common Format Specifiers

<!-- column -->
```text
%s  String
%d  Integer
%f  Floating-point
%c  Character
%b  Boolean
%n  Newline
```

<!-- column -->
Examples:

```java
String name = "Alice";
int age = 20;
double gpa = 3.75;

System.out.printf("%s %d %.2f",
                  name, age, gpa);
```

Output:

```text
Alice 20 3.75
```

---

# Width and Precision

<!-- column -->

Format Specifier

```text
%10.2f
```

- Width = 10
- Precision = 2

<!-- column -->

Output:

```text
      3.14
```

Meaning:

- Total field width is at least 10
- Number is rounded to 2 decimal places
- Extra space is filled with blanks

---

# String Placeholders

<!-- column -->
```java
String firstName = "Jane";
String lastName = "Smith";

System.out.printf(
    "Student: %s %s",
    firstName,
    lastName
);
```

<!-- column -->
Output:

```text
Student: Jane Smith
```

- `%s` inserts a String value
- Values replace placeholders in order

---

# Multiple Placeholders

<!-- column -->

```java
String name = "Bob";
int age = 18;
double grade = 92.456;

System.out.printf(
    "%s is %d years old and has a %.1f average",
    name,
    age,
    grade
);
```

<!-- column -->

Output:

```text
Bob is 18 years old and has a 92.5 average
```

- First placeholder receives first variable
- Second placeholder receives second variable
- Third placeholder receives third variable

---

# Placeholder Matching

<!-- column -->
Correct:

```java
int age = 21;

System.out.printf("%d", age);
```

Incorrect:

```java
int age = 21;

System.out.printf("%s", age);
```
<!-- column -->
Rule:

- `%d` → integer
- `%f` → decimal number
- `%s` → string
- `%c` → character

Use the placeholder that matches the data type.

---

# Quick Reference

<!-- column -->
```text
%f      default decimal formatting
%.2f    2 digits after decimal
%8.2f   width 8, precision 2
%d      integer
%s      string
%c      character
%b      boolean
%n      newline
```
<!-- column -->
Remember:

- Width controls spacing
- Precision controls decimal places
- `printf()` combines text and variables into a formatted message

---

# More Examples
## Simplify output code
```java
System.out.printf("Hi my name is %s", name);
```
   instead of 
```java
System.out.printf("Hi my name is " + name);
```
---
# More Examples
## Multiple variables
```java
System.out.printf("i my name is %s %s", firstName, lastName);
System.out.printf("Hi my name is %s %s and my age is %d and my grade is %.2f", 
    firstName, lastName, age, grade);
```

---
