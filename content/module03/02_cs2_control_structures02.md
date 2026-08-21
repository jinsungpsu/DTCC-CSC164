# Control Structures II

For, While, Do While, Break, Continue

---

# Asking questions…

- Always about using boolean expressions
- Ask the question and evaluate to true/false to determine what to do

---

# While

- Pretest

---

# do … while

- Post-test
- Executes at least once

---

# For

- Normally used when number of iterations is known
- Uses a counter
- Often used with arrays

---

# Anatomy of a for loop

```java
for (initial action; condition to continue looping; action after each iteration)
```

- MOST for loops look like this
- for (int i = 0; i < count; i++)
- However, you can do some crazy stuff like
- for (int i = 0, j = 10; i < 10 && j > 5; i++, j--)
- for (;true;)
- for (int i = 10;i < 99;)
- for (int i = 10;i < 99;i = i + 20)

---

# Break

- Immediately exits the entire loop, meaning it stops the loop execution and jumps to the next statement following the loop code; it is used when a specific condition is met within the loop that requires you to terminate the loop early

---

# Continue

- Terminates execution of the statements in the current iteration and continues execution of the loop with the next iteration

---

# while(true)

- sometimes, infinite loops are useful, but need a break/exit condition

---

# Nested loops

- Nesting blocks of code to solve problems
- multi-dimensional arrays
- 2D arrays, nested for loops
- “rows” and “columns”
- outer loop goes through rows
- inner loop goes through columns

---

# Debugging

- Getting familiar with your debugging tools will be very helpful when dealing with loops - especially nested loops
