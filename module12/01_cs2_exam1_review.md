# CSC164 Exam 1 Review

---

# Exam Instructions/Policies

This assessment is closed resource (no notes, powerpoint, textbook, internet, etc.). If you open another internet browser or tab, it will be considered cheating. You may not leave the testing area for any reason. If you have any extenuating circumstances that may require any exceptions, please let the instructor/proctor know as soon as you can.

This assessment MUST be completed using D2L on a lab computer during the scheduled time and location; you may not use your own device or take this assessment at a different location without prior approval.

---

# Format

- Entirely in D2L
- Multi-select
- Multiple choice
- True/false
- Written Response (short answer)

---

# Programming Style

- Best practices
- Naming conventions
- Formatting and indentation

---

# Variable naming conventions

- Descriptive, avoid single character identifiers unless they are meaningful in the context (such as x, y in a coordinate system, or i as an index/counter for a loop)
- Constants (final) should use all CAPS
- Class names start with upper case
- Variable names start with lower case
- Use camelCase
- with constants, use underscore to separate words
- These are best practices, so they are NOT syntax errors

---

# Data Types and Casting

- Implicit vs explicit casting
- When do data types gets converted automatically?
- smaller to bigger
- Bigger to smaller, MUST explicitly cast otherwise, it’s a syntax error

---

# Casting Practice

- Will this compile?
- Example 1:
- int num = 5;
- double num2 = num;
- Example 2:
- double num = 5.5;
- int num2 = num;
- Example 3:
- double num = 5.5;
- float num2 = (float) num;

---

# Arrays

- Single dimensional arrays
- two dimensional arrays
- Array sizing and memory allocation
- Initializing arrays

---

# Arrays

- MUST provide a size when defining a variable
- explicitly: `int[] arr = new int[5];` // explicit size of 5
- implicitly: `int[] arr = {1,2,3};` // implicit size of 3
- CANNOT be resized
- How does it behave when passed into a method as a parameter?

---

# Control Structures

- Boolean expressions
- If/else if/else
- Switch/case/default
- Loops (while, do while, for)

---

# Tracing Code

- Some questions showing code and asking what is the output…
- Ability to trace code and figure out the execution order

---

# Switch/case

- How does it work?
- break statement and fallthrough behavior
- What is the default case useful for?

---

# Methods

- “Black box” (3 rules)
- Parameters
- Return data
- Defining methods
- Calling/invoking methods

---

# Methods

- For the given method
- What is the return type?
- What are the parameter(s)?
- How would you call/invoke each method?
- static boolean isEven(int num)
- static int sum(int[] arr)
- static double sum(int num1, float num2, double num3)

---

# Debugging

- Debugging Tools
- Breakpoints
- Stepping over
- Stepping into and out of
- Errors/Exceptions
- Compiler Errors
- Logic Errors

---

# Stepping into or over

- What’s the difference?
- Why is it useful to use one or the other?

---

# Breakpoints

---

# Practice

Write a program/method that…

- Displays all the elements of a 1D or 2D array
- The sum of each column or row
- Sum of all elements
- Average of a column or row
- Average of all elements
