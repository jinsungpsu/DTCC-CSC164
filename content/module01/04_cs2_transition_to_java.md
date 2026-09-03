# Transition from C++ to Java
## Practical Introduction

<!-- footer -->
Delaware Technical Community College

---

# Setting up a new project in IntelliJ
## (Demo in class)
---

# IntelliJ / Text Editors
## (Demo in class)

---

# How to screenshot
## (Demo in class)

---

# How to submit in D2L
## (Demo in class)

---

# Writing a Program
## In Java

---

# The Basic Java Application
## Textbook Section 2.1

<!-- footer -->

https://math.hws.edu/javanotes/c2/s1.html

---

# What is a Program?

- A program is a sequence of instructions for a computer.
- Instructions must be written in a programming language.
- Programming languages are strict and unambiguous.

---

# Syntax Rules

- Syntax defines the structure and vocabulary of a language.
- Correct syntax is required for successful compilation.
- Syntax errors prevent the program from running.

---

# Semantics of a Program

- Semantics define the meaning of a program.
- A semantically correct program performs the intended task.
- Understanding semantics is key to correct results.

---

# Programming Style (Pragmatics)

- Style makes code readable and maintainable.
- Follow conventions familiar to other programmers.
- Design should make sense to human readers.

---

# Learning and Applying Concepts

- Memorize syntax and understand semantics.
- Practice writing programs.
- Develop experience and taste for good design.

---

# Steps to Run a Java Program

1. Write the program using a text editor.
2. Compile the program into bytecode.
3. Run the compiled bytecode using an interpreter.

---

# Anatomy of Java Program

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```

- Everything has to be inside a class (MUCH more on this later this semester)
- `public static void main(String[] args)` is the entry point of the program.
- Similar to `int main()` in C++.

---

# Output to screen/console

```java
System.out.println("Hello World!");
```

- Uses a built-in subroutine (similar to function) to display output.
- Subroutines are named tasks that can be called.

---

# Comments in Java

```java
// Single-line comment
/* Multi-line comment */
/** Javadoc comment */
```

- Comments are ignored by the computer.
- Comments help human readers understand the code.

---

# Java Program Layout

- Layout (indentation and spacing) is not required by syntax.
- Good layout improves readability.
- Follow style guidelines for clarity and maintainability.

---

# Class and Main Method

- Every Java program is defined in a class.
    - By convention, class names start with an uppercase letter.
        - The compiler does not enforce this convention.
- The `main` method is the entry point of the program.
    - By convention, method names start with a lowercase letter.

```java
public static void main(String[] args) {
  // statements
}
```

---

# Output

<!-- column -->

## C++

```cpp
cout << "Hello World";
cout << endl;
```

<!-- column -->

## Java

```java
System.out.print("Hello World");
System.out.println();
```

---

# Output 2

<!-- column -->

## C++

```cpp
cout << "Hello World\n";
```

<!-- column -->

## Java

```java
System.out.print("Hello World\n");
```

---
