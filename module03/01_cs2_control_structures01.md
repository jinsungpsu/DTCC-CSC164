# Control Structures I

## If, Else if, Else, Switch

---

# Boolean Type

The data type boolean can only hold two values, 0 (false) and 1 (true)

Used in control structures

Control Structures are just a way to specify flow of control in programs. Any algorithm or program can be more clear and understood if they use self-contained modules called as logic or control structures. It basically analyzes and chooses in which direction a program flows based on certain parameters or conditions. There are three basic types of logic, or flow of control, known as:

- Sequence logic, or sequential flow
- Selection logic, or conditional flow
- Iteration logic, or repetitive flow

<!-- footer -->

https://www.geeksforgeeks.org/control-structures-in-programming-languages/

---

# Examples in java

```java
boolean answer = true;
boolean repeat = false;
```

---

# Relational operators

Operators like any other operators… unary, binary… one or two operands

Operators like plus:

- 1 + 2
- operator is +
- operands are 1 and 2
- result of the operation is 3
- 4 > 5
- operator is >
- operands are 4 and 5
- result of the operation is false

---

# More examples

- !(4 > 5)
- Two separate operators, > and !
- Order of operations applies
- > operation performed first
- 4 > 5 = false
- ! operation is performed second
- ! is a unary operator, only ONE operand
- ! false = true
- The overall result is true

---

# More examples

- (x < 5) || (x > 10)
- there are 3 operations (<, ||, and >)
- order of operations applies
- Can’t do:
- 10 > x > 5

---

# Summary of Relational Operators

| Operator | Meaning |
|---|---|
| < | less than |
| <= | less than or equal to |
| > | greater than |
| >= | greater than or equal to |
| == | equal (not to be confused with assignment operator =) |
| != | not equal to |

---

# Summary of Logical Operators

| Operator | Meaning |
|---|---|
| ! | NOT |
| && | AND |
| || | OR |

---

# Basic Control Structures

- Control structures are always asking a question, which is evaluated as a boolean data type
- If
- if (true)
- if (5 > 4)
- if (x < 5)
- else if
- else if (false)
- else if (x < 1)
- else if (!(x < -5))
- else
- Catch all - no question is being asked

---

# If statement

- Conditionally executed line or block of code

---

# Else if

- Multiple conditions checked, but ONLY ONE is conditionally executed
- Checked in order, so the order matters!

---

# Else

- Catch all if every other if and else if conditions are false
- When the else is included - guaranteed that ONE of the blocks will be executed

---

# Nesting

- Always think of blocks of code as independent pieces of logic

```java
if (...) {
    // whatever happens here is its own logic…
    // which can include other control structures
}
```

---

# Switch

- Not about asking question using boolean data type
- Instead, it’s about matching…

```java
int x = 5;
switch(x) {
    case 1:
        // if x == 5
        break;
    case 2:
        // if x == 2;
        break;
    default:
        // else
}
```

---

# Useful for menu-driven programs

- Do something
- Do something else
- Exit

```java
What would you like to do?  (Enter 1-3):
switch(userInput) {
    case 1:
        break;
    case 2:
        break;
    case 3:
        break;
    default:
        // invalid input
}
```

---

# Fall through behavior

- If you omit the break statement, the program will just continue to the next instruction
- Often used when multiple cases should be handled the same way:

```java
char letter = ‘a’;
switch(letter) {
    case ‘a’:
    case ‘A’:
        // this handles both ‘a’ and ‘A’
        break;
    case ‘b’:
    case ‘B’:
        // this handles both ‘b’ and ‘B’
        break;
    default:
        // catch all
}
```

---

# Default case

- Catch all
- Recommended to use

---

# Conditional operator

```java
variable = boolean-expression ? exp1 : exp2
```

same as:

```java
if (boolean-expression) {
    variable = exp1;
} else {
    variable = exp2;
}
```

---

# Conditional Operator Example

```java
double grade = 90.5;
boolean passed = (grade > 70.0) ? true : false;
String passingStatus = (grade > 70.0) ? “passed” : “failed”;
```

- Often used to shorten code:

```java
System.out.print(“The student “ + (grade > 70.0) ? “passed” : “failed”);
```
