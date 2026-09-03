# Methods

---

# Differences from C++

- Add word “static” in front of return type
- For example…
- `static void printNum() { }`
- Order does NOT matter!
- No prototypes like C++
- Can be in any order before or after main
- MUST BE INSIDE of the class

---

Functions = methods = subroutines (well… kind of)

<!-- footer -->

https://www.quora.com/What-are-the-main-differences-between-a-function-a-method-a-procedure-and-a-subroutine

---

# What is a method?

A SUBROUTINE CONSISTS OF INSTRUCTIONS for performing some task, chunked together and given a name. "Chunking" allows you to deal with a potentially very complicated task as a single concept. Instead of worrying about the many, many steps that the computer might have to go though to perform that task, you just need to remember the name of the subroutine. Whenever you want your program to perform the task, you just call the subroutine. Subroutines are a major tool for dealing with complexity.

<!-- footer -->

https://math.hws.edu/javanotes/c4/s1.html

---

# “Black Box”

A subroutine is sometimes said to be a "black box" because you can't see what's "inside" it (or, to be more precise, you usually don't want to see inside it, because then you would have to deal with all the complexity that the subroutine is meant to hide). Of course, a black box that has no way of interacting with the rest of the world would be pretty useless.

---

# Black Box Rule #1

The interface of a black box should be fairly straightforward, well-defined, and easy to understand.

---

# Black Box Rule #2

To use a black box, you shouldn't need to know anything about its implementation; all you need to know is its interface.

---

# Black Box Rule #3

The implementer of a black box should not need to know anything about the larger systems in which the box will be used.

---

# Method Stubs

- Placeholder methods
- void methods can be completely empty
- value returning methods should just return a hard-coded, “dummy” value

---

# Black Box Interface = Method Header

```java
void printMenu() {...}
```

- What is the return type?
- What is the “output” of this method?
- What are the parameters?
- What are the “input(s)” of this method?
- Its name… should be descriptive
- (and documentation)

---

# Void methods

- They don’t return “something”
- But they do need to return to the point of the program where it was called from…
- You can use a return statement in void methods, too - to exit the method immediately.

---

# Parameters

- Data that is passed in as a parameter (or argument) is a value of whatever was passed in.

---

# Overloaded methods

- A feature in Java that allows multiple methods in the same class to have the same name but different parameters.
- Methods are differentiated based on number, type, or order of parameters.

```java
// Method with
// two integer parameters
int add(int a, int b) {
    return a + b;
}

// Overloaded method
// with two double parameters
double add(double a, double b) {
    return a + b;
}

// Overloaded method
// with three parameters
int add(int a, int b, int c) {
    return a + b + c;
}
```

---

# Array as a parameter

- Passed as a value… but the value is a reference.
- What???
- So it’s practically pass by reference
- The variable for an array is considered to be a reference variable
- A reference variable is an address in memory (RAM) rather than an actual value

---

# Practice

```java
int sum(int num1, int num2) {...}
```

- What is the return type?
- What are the parameters?

---

```java
boolean isEven(int num) {...}
```

- What is the return type?
- What are the parameters?

---

```java
boolean contains(String string, char letter) {...}
```

- What is the return type?
- What are the parameters?

---

```java
char charAt(String string, int index) {...}
```

- What is the return type?
- What are the parameters?

---
# How to Deal with Scanner/Keyboard

- A `Scanner` object follows the same scope rules as any other variable in Java.
- If you declare a Scanner inside a method, it can only be used within that method.
- What should you do if multiple methods need keyboard input?

---

# Scanner/Keyboard Options

- Create another Scanner inside the method
  - Generally not recommended when reading from `System.in`
  - Multiple Scanners reading from the same input stream can cause unexpected behavior

- Pass the Scanner as a parameter
  - A clean and flexible approach
  - Makes it clear where the input is coming from

- Declare the Scanner as a static class variable
  - Allows all static methods in the class to access it
  - Common in small programs and classroom examples

---

# Scanner Passed as Parameter

```java
public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);

    int firstNum = keyboard.nextInt();

    someMethod(keyboard);
}

static void someMethod(Scanner keyboard) {
    double secondNum = keyboard.nextDouble();
}
```

- The same Scanner object is shared between methods.
- Only one Scanner is connected to `System.in`.

---

# Static Scanner Example

```java
public class Main {

    static Scanner keyboard = new Scanner(System.in);

    public static void main(String[] args) {
        int num = keyboard.nextInt();
    }

    static void someMethod() {
        double num = keyboard.nextDouble();
    }
}
```

- The Scanner is declared once for the entire class.
- Any static method can use the Scanner.
- This is convenient for small programs.

---

# Don't Close the Scanner Too Early

```java
Scanner keyboard = new Scanner(System.in);

// Read input here

keyboard.close();
```

- Closing the Scanner also closes `System.in`.
- Once `System.in` is closed, keyboard input can no longer be read.
- For simple programs, close the Scanner at the very end of the program.

---

# Course Recommendation

For the rest of this course and your assignments, use a single static Scanner:

```java
static Scanner keyboard = new Scanner(System.in);
```

Why?

- It keeps our examples shorter and easier to read.
- Any method in the class can access the Scanner.
- We only create one Scanner attached to `System.in`.
- It avoids having to pass the Scanner to every method.

**Note:** In larger software projects, programmers often pass objects as parameters instead of using static variables. For this course, however, a single static Scanner is the simplest and most convenient approach.

---

# Practice

Write a method that…

- Checks whether a pin number is correct or incorrect (as in a ATM machine or phone/tablet)

---

# Parameters?

Write a method that…

- Checks whether a pin number is correct or incorrect (as in a ATM machine or phone/tablet)
- In other words, what data does this black box need in order to do the work?

---

# What’s the return type?

Write a method that…

- Checks whether a pin number is correct or incorrect (as in a ATM machine or phone/tablet)
- In other words, once this black box is finished doing what it’s doing, what is the output/result of the work it has completed?

---

# More practice

Write a method that does input validation - for example, an integer between 1 and 5

- Return type?
- Parameters?

---

Write a method that adds up a specific row of values in a 2 dimensional array of integers.

- Return type?
- Parameters?

---

# Method we’ve already used…

```java
int num = keyboard.nextInt();
```

- What is the return type of nextInt()?
- What are the parameters?
- This is an example of an instance method (much more on this later this semester), so it is invoked on a Scanner/keyboard.

---

# String examples

```java
String word = "Hello World";
for (int i = 0; i < word.length(); i++) {
   System.out.print(word.charAt(i));
}
```

---

# Return type? Parameters?

```java
String word = "Hello World";
for (int i = 0; i < word.length(); i++) {
   System.out.print(word.charAt(i));
}
```

---

# String length vs array length

- Unlike the length method for String, an array’s length property is NOT a method:
- Notice the lack of parenthesis after the word “length”

---

# Static method example

```java
public static void main(String[] args) {
   someMethod();
}

static void someMethod() {
   System.out.println("Hello World!");
}
```

---

# Static method

When it’s called, it’s not associated with some other variable - as we saw with Scanner and String methods in previous examples

---

# Other ways to invoke static methods

```java
class Main {
   public static void main(String[] args) {
      Main.someMethod();
   }
   static void someMethod() {
      System.out.println("Hello World!");
   }
}
```

- Can call static methods by using the class name

---

# Other examples of static methods

- Integer.parseInt
- Integer.valueOf
- Arrays.copyOf
- We’ll call these methods by using the name of the class, followed by the name of the method and any parameters, as needed.

---

# Arrays.copyOf

```java
import java.util.Arrays;
public class Main {
   public static void main(String[] args) {
       int[] arr1 = {1,2,3};
       int[] arr1copy = Arrays.copyOf(arr1, 3);
   }
}
```

---

# Integer.parseInt

String is considered an inconvertible type to int, but, often, we have to parse the information from a string.

```java
String word = "1";
int numInWord = Integer.parseInt(word);
```

---

# Getting a char input

There’s no nextChar method for the Scanner.

Instead, we get a String using next, then just get the first character of the String.

```java
char letter = keyboard.next().charAt(0);
```

---

# 2 step process

```java
String word = keyboard.next();
char letter = word.charAt(0);
```

---