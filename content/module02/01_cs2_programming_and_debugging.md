# Programming and Debugging in Review
<!-- footer -->
Delaware Technical Community College

---

# Pseudocode and Stepwise Refinement
## Textbook Section 3.2.1

<!-- footer -->
https://math.hws.edu/javanotes/c3/s2.html

---

# Programming in the Small
- Basic elements: variables, assignment, input/output
- Use of subroutines and objects
- Control structures: while loops, if statements

---

# Stepwise Refinement
- Start with a general task description
- Gradually add steps and details
- Refine into a complete algorithm
- Supports top-down design

---

# Using Pseudocode
- Informal instructions resembling programming syntax
- Helps outline logic before coding
- Not strict on syntax, but must be clear

---

# Loop Design and Generalization
- Identify repetitive tasks
- Use loops to reduce repetition
- Counting loops for fixed iterations

---

# Translating Algorithms into Code
- Choose variable names and syntax
- Ensure complete specification of inputs and outputs
- Use braces and parentheses correctly in Java

---

# Complete Problem Specification
- Define what the program should do
- Specify inputs, outputs, and computations
- Avoid ambiguity before coding

---

# Coding, Testing, Debugging
## Textbook Section 3.2.3

<!-- footer -->
https://math.hws.edu/javanotes/c3/s2.html

---

# From Algorithm to Code
- Coding translates design into Java or another language
- Syntax errors are common and must be fixed
- Compiler messages may be misleading

---

# Basic Coding Guidelines
- Understand syntax rules thoroughly
- Always match braces and indent code properly
- Use consistent naming conventions
- Fix errors in order of appearance

---

# Importance of Testing
- Ensure program works for all reasonable inputs
- Test each stage of development
- Write extra code for testing if needed

---

# Debugging Techniques
- Debugging finds semantic errors in behavior
- Read code step-by-step like a computer
- Use breakpoints and debuggers
- Insert print statements to trace execution

---

# Golden Rule of Debugging
- If you're sure everything is right and it still doesn't work...
- Then something you're sure of is actually wrong

---

# More on Java Programming and Review

---

# Blocks
- What is a Code Block?
    - A code block is a group of statements that are treated as a single unit.
    - In Java and many other languages, code blocks are enclosed in curly braces {}.
- Purpose of Code Blocks
    - Define the body of control structures like if, while, for, and methods.
    - Help organize code logically and visually.
    - Ensure that multiple statements are executed together.

---

# Indentation
- Indentation refers to the spaces or tabs used at the beginning of lines of code.
- It helps organize code visually and logically.
- Most programming languages ignore indentation, but it is essential for readability.

---

# When to use comments
- Comments are for humans (including yourself)

---

# Naming conventions
- Descriptive/meaningful variable names
- start with lower case for variable names
- start with upper case for class names
- use camelCase for multiple words
    - For class names, variable names, function/method names

---

# Naming Conventions
## Specific identifier name rules in java
- Consists of letters, digits, underscores, and dollar signs
- Must start with a letter, underscore, or dollar sign (cannot start with number)

---

# Constants
- use keyword final
- use all upper case
- can’t use camelCase, since it’s all upper case, use under_score between words
- must be initialized with a value

```java
final int NUM_STUDENTS = 5;
```
---

# Modulus review
- Simply the remainder part of division
- Uses of %
    - even, odd
    - “wrapping around”
        - something that happens every n-th time in a loop

---

# Increment / Decrement
- preincrement/predecrement
    - ++var, --var
    - Change the value and use the new value in the statement
- postincrement/postdecrement
    - var++, var--
    - Use the value and use the old value in the statement

---

# Java Numeric Type Promotion & Demotion
### Promotion ↑ (Automatic Promotion)

double

⬆

float

⬆

long

⬆

int

⬆

short

⬆

byte

---
# Java Numeric Type Promotion & Demotion

### Demotion ↓ (Explicit Demotion)
double

⬇ cast

float

⬇ cast

long

⬇ cast

int

⬇ cast

short

⬇ cast

byte

---
# Java Numeric Type Promotion & Demotion Examples
```java
byte b = 100;
int n = b;          // promotion

double d = 3.14;
int x = (int)d;     // demotion
```
---

# Type casting

```java
int smallNum = 5;

System.out.print(smallNum / 2); 
// will print 2

System.out.print((double)smallNum / 2); 
// will print 2.5
```
---

# Analogy

<!-- column -->

- Overflow *can* occur when converting from a bigger type to a smaller type - so it must be done explicitly.
```java
double bigNumber = 1234.5678;

int smallNumber = (int) bigNumber; 
// this works

int smallNumber = bigNumber; 
// this is an error
```
<!-- column -->

![Overflow illustration pouring large amount of water from a 5 gallon bucket into small 8 oz cup and water overflowing](images/overflow.png)

---

# String concatenation for output
```java
int students = 5;
System.out.print("The number of students is " + students);
```
- What’s actually happening?
- The students variable is being converted to a string, then “added” to the rest of the string

---

# Print examples of conversion
```java
System.out.print(1 + 1);
// this outputs 2
System.out.print("The sum is " + 1 + 1);
// the output is The sum is 11
// because the 1’s are being treated as strings
System.out.print("The sum is " + (1+1));
// the output is The sum is 2
// because the (1+1) makes the operator precedence
// add the 1+1 as integers first,
// THEN gets converted to a string
// before being added to the "The sum is " string
```
---
