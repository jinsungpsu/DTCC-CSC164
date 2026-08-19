

# User Input
- The Scanner object

---

# Baby steps towards OOP (Object Oriented Programming)
- What is a class?
- What is an object?

---

# Classes and Objects
- In object-oriented programming (OOP), a class is a blueprint or template for creating objects, which are instances of the class. It defines the structure and behavior of the objects by encapsulating data and methods (functions) that operate on that data.

---

# Not all that different from any data type…
- int num1;
- int num2;
- int would be similar to a class.  It’s a general description of what an integer holds (data) and what it can do (operations like +, -).
- num1 and num2 would be similar to objects.  You can create many unique version of this “class” such as num1 and num2.

---

# Scanner class
- https://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html
- Get comfortable looking at documentation
- https://www.w3schools.com/java/java_user_input.asp
- But tutorial sites are great, too

---

# Scanner object
- like any other variable
- needs a name
- only one needed for the program

---

# Scanner example
- Scanner input = new Scanner(System.in);
- Scanner is the class (type)
- input is the identifier (name) of the object
- new Scanner(System.in) ← more on this later in this semester

---

# Scanner example (continued)
- int num = input.nextInt();
- float num2 = input.nextFloat();
- double num3 = input.nextDouble();
- String name = input.next();
- String sentence = input.nextLine();
- ** Note that there is no nextChar() - more on this later in the semester!
- char letter = input.next().charAt(0);

---

# Import
- Need to import java.util.Scanner - similar to #include <iostream>
- Can explicitly import java.util.Scanner or import the entire java.util library using the * wildcard.
- import java.util.*;
- No performance impact

---

# System.exit(1)
- If you ever need to end your program at any point, you can use the System.exit(1) statement.
- The value “1” is a value that is sent back to the operating system to indicate whether the application ended normally or unexpectedly…
- Can also use “return”

---