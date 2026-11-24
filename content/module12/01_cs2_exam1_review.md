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

# Review: Casting and Division

### What values are stored in hours and roundedDown?

```java
int minutes = 95;
double hours = (double) minutes / 60;
int roundedDown = (int) hours;
```

<div class="fragment">

**hours** is approximately 1.58. Casting before the division makes it floating-point division. **roundedDown** is 1 because converting this positive value to int discards the fractional part.

</div>

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

# Review: Programming Style

### Improve the names and indentation in this code. Which changes affect the calculation?

```java
final int seatsperrow = 8;
int r = 3;
if (r > 0) {
System.out.println(seatsperrow * r);
}
```

<div class="fragment">

Use SEATS_PER_ROW and rowCount, then indent the print statement inside the if block. Apply the names consistently at their declarations and uses. The result stays 24.

</div>

---

# Review: Conditions and Switches

### Trace this switch for "bus", then for "bike". What changes if you add a break after the bus case?

```java
switch (mode) {
    case "bus":
        System.out.print("Show pass. ");
    case "train":
        System.out.print("Board now.");
        break;
    default:
        System.out.print("Check route.");
}
```

<div class="fragment">

**bus** prints both messages through fallthrough. **bike** reaches default and prints "Check route." Adding a break after the bus case makes "bus" print only "Show pass."

</div>

<div class="fragment">

### If discounts apply to riders under 12 or at least 65, what condition would you write?

**age < 12 || age >= 65**

</div>

---

# Review: Tracing Loops

### What is total at the end? Which array index would you inspect first if the goal were to include every value?

```java
int[] hours = {3, 1, 4, 2};
int total = 0;
for (int i = 1; i < hours.length; i++) {
    total += hours[i];
}
```

<div class="fragment">

**total is 7.** The loop visits indices 1, 2, and 3. Start at index 0 to include the first value.

</div>

---

# Review: Arrays and Method Calls

### After update(scores) runs, what are the two values in scores? Explain each assignment.

```java
int[] scores = new int[2];
update(scores);

static void update(int[] values) {
    values[0] = 9;
    values = new int[] {4, 5};
}
```

<div class="fragment">

**scores contains 9 and 0.** The first assignment changes the shared array. The second changes only the local parameter because Java passes a copy of the reference. The original array still has length 2 and its second element keeps the default value of 0.

</div>

---

# Review: Methods and Debugging

### A program calls double cost = calculateCost(3) with a method that takes an int quantity and returns a double. What should callers know about this method? How would you investigate a wrong total?

<div class="fragment">

Callers need the method's name, expected input, and what the returned value represents. Here the parameter is int quantity, the argument is 3, and the return type is double.

</div>

<div class="fragment">

Set a breakpoint at the call. Step Into to inspect quantity and the calculation inside the method, or Step Over to execute the call and inspect cost from the caller.

</div>

---

# Practice Programming: Count Values in a Range

### Write countInRange(int[] readings, int low, int high) to return how many readings are within the inclusive bounds. For {8, 12, 17, 21} and bounds 10 and 17, it should return 2.

<div class="fragment">

```java
static int countInRange(int[] readings, int low, int high) {
    int count = 0;
    for (int reading : readings) {
        if (reading >= low && reading <= high) {
            count++;
        }
    }
    return count;
}
```

</div>

---

# Practice Programming: Search a 2D Array

### Write containsValue(int[][] grid, int target) to report whether any cell contains target. Use the actual length of each row.

<div class="fragment">

```java
static boolean containsValue(int[][] grid, int target) {
    for (int[] row : grid) {
        for (int value : row) {
            if (value == target) {
                return true;
            }
        }
    }
    return false;
}
```

</div>
