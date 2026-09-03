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