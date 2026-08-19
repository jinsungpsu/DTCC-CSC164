# Intro to Programming in Java
## Practical Introduction
## and transitioning from C++

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
<div style="font-size:0.6em;">

# Data Types

| Type | Used For | Example |
|--------|----------|---------|
| `byte` | Small integers | `127` |
| `short` | Medium integers | `32000` |
| `int` | Regular integers | `100` |
| `long` | Large integers | `123456789L` |
| `float` | Decimal numbers | `19.99F` |
| `double` | Precise decimal numbers | `3.14159` |
| `char` | One character | `'A'` |
| `boolean` | True/False values | `true` |
| `String` | Text | `"Hello"` |

<!-- footer -->

https*//*ww.w3schools.com/java/java_data_ty*es.asp
</div>

---
<div style="font-size:0.6em;">

# Java Primitive Type Ranges

| Type | Minimum Value | Maximum Value |
|--------|--------|--------|
| `byte` | -128 | 127 |
| `short` | -32,768 | 32,767 |
| `int` | -2,147,483,648 | 2,147,483,647 |
| `long` | -9,223,372,036,854,775,808 | 9,223,372,036,854,775,807 |
| `float` | ±1.4 × 10^-45 | ±3.4 × 10^38 |
| `double` | ±4.9 × 10^-324 | ±1.8 × 10^308 |
| `char` | 0 (`'\u0000'`) | 65,535 (`'\uffff'`) |
| `boolean` | `false` | `true` |

</div>
---

# String

- Slightly different from the primitive data types.
- `String` is actually a class.
- We'll discuss classes in more detail later.

---

# Defining Variables

- Same as C++

```java
int age = 20;
double gpa = 3.5;
char grade = 'A';
String name = "Alex";
```

---

# Numeric Operators
- Addition (`+`)
- Subtraction (`-`) 
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)

---

# Augmented Operators

- Each numeric operator has a corresponding shorthand assignment operator.

```java
+=
-=
*=
/=
%=
```

Example:

```java
count += 1;
total *= 2;
```

---

# Literals vs Variables

- A literal is a value written directly into source code.
- A variable stores a value in memory RAM.

Examples of literals:

```java
1
1.5
'A'
"hello"
```

Example using variables:

```java
int x = 1; 
// in this case, 
// 1 is a literal, 
// x is a variable
```

---

# Numeric Literals

* Numeric literals can include suff*xes to specify their type.

```java
1.23L   // long
1.23F   // float
1.23D   // double
```


## Scientific Notation

```java
1e3
```

Equivalent to:

```text
1 × 10^3 or 1000
```

---

<div style="font-size:0.7em;">

# Java Operator Precedence


| Precedence | Operators | Description |
|------------|------------|-------------|
| Highest | `()` `[]` `.` | Parentheses, array access, member access |
| 2 | `++` `--` `+` `-` `!` | Unary operators |
| 3 | `*` `/` `%` | Multiplication, Division, Modulus |
| 4 | `+` `-` | Addition, Subtraction |
| 5 | `<` `<=` `>` `>=` | Relational operators |
| 6 | `==` `!=` | Equality operators |
| 7 | `&&` | Logical AND |
| 8 | `||` | Logical OR |
| 9 | `=` `+=` `-=` `*=` `/=` `%=` | Assignment operators |


<!-- footer -->
https://www.programiz.com/java-programming/operator-precedence

</div>

---

# Operator Precedence

### Example

```java
int result = 2 + 3 * 4;
```

Evaluates as:

```java
int result = 2 + 12;
int result = 14;
```

Because `*` has higher precedence than `+`.

---

# Remember PEMDAS

1. Parentheses `()`
2. Multiplication, Division, Modulus `* / %`
3. Addition, Subtraction `+ -`
4. Comparisons `< > <= >=`
5. Equality `== !=`
6. Logical AND `&&`
7. Logical OR `||`
8. Assignment `=`

### Example

```java
boolean answer =
    (5 + 2 > 3) && (10 % 2 == 0);
```

- `5 + 2` evaluated first
- `10 % 2` evaluated next
- Comparisons evaluated
- `&&` evaluated last