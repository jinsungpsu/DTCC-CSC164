# Java Classes

Java is an **Object-Oriented Programming (OOP)** language.

Throughout this course, we have already worked with classes and objects, even before discussing them in detail.

Two important classes we have used frequently are:

- `String`
- `Scanner`

Today we'll focus on understanding how these classes, their objects, and their methods work together.

---

# What Is a Class?

A **class** is a blueprint used to create objects.

<!-- column -->
Examples from our programs:

- `String` is a class
- `Scanner` is a class

<!-- column -->
Examples of objects:

```java
String name = "Alex";

Scanner input = new Scanner(System.in);
```

<!-- endcolumns -->

In this example:

- `String` and `Scanner` are classes
- `name` is a String object
- `input` is a Scanner object

A class describes what its objects can do.

---

# What Is an Object?

An **object** is an instance of a class.

Think of a class as a blueprint and an object as something created from that blueprint.

<!-- column -->
Example:

```java
String firstName = "Alex";
String lastName = "Smith";
```

Both variables refer to String objects.

<!-- column -->
Another example:

```java
Scanner keyboard = new Scanner(System.in);
```

`keyboard` is a Scanner object.

<!-- endcolumns -->

Objects store data and provide methods that can be used to perform actions.

---

# Most Programming Uses Existing Classes

When programmers write software, they spend much more time **using classes** than creating them.

Examples:

- Reading input with `Scanner`
- Working with text using `String`
- Displaying windows and buttons in GUI applications
- Accessing databases
- Working with files
- Communicating over networks

---

Even professional developers regularly use thousands of classes that were written by other programmers.

Think of programming like building with LEGO pieces:

- Some programmers create the pieces
- Most programmers spend their time combining pieces to build something useful

---

Learning classes helps us:

- Understand how Java libraries work
- Read documentation more effectively
- Use existing code correctly
- Create better programs by combining existing tools

Knowing how to use classes well is often more important than writing new ones from scratch.

---

# Revisiting Methods

A **method** is a named block of code that belongs to a class or object.

Methods define behaviors associated with objects.

Example:

```java
String name = "Alex";

name.length();
name.toUpperCase();
```

Method calls use **dot notation**:

```java
objectName.methodName();
```

---

# String Objects

A String object stores text.

Example:

```java
String name = "Alex";
```

The variable `name` refers to a String object containing:

```
Alex
```

Because it is an object, we can call methods that belong to the String class.

Examples:

```java
name.length();

name.toUpperCase();

name.toLowerCase();
```

---

# String Objects Are Created Automatically

Most objects are created with `new`:

```java
Scanner input =
        new Scanner(System.in);
```

Strings are special.

We often create String objects without explicitly using `new`:

```java
String name = "Alex";
```

---

# String Literal

Behind the scenes, Java still creates a String object.

This syntax is called a **String literal**.

We can also create a String object explicitly:

```java
String name =
        new String("Alex");
```

Both approaches create String objects, but Java allows a shortcut because Strings are used so frequently.

Many details of object creation are hidden from us when working with Strings.

---

# Comparing Strings

A common mistake is using `==` to compare String contents.

Consider:

```java
String name1 = "Alex";
String name2 = "Alex";
```

This may appear to work:

```java
if (name1 == name2)
```

However, `==` checks whether two variables refer to the same object.

---

# Using equals method

To compare the actual text stored in Strings, use:

```java
if (name1.equals(name2))
```

The `equals()` method checks whether the contents are the same.

```java
"Alex".equals("Alex")
```

returns:

```java
true
```

---

# Summary: Equals vs ==

For Strings:

- `==` compares object references
- `equals()` compares character contents

> use `equals()` when checking whether two Strings contain the same text.

---

# The length() Method

The `length()` method returns the number of characters in a String.

Example:

```java
String name = "Alex";

int size = name.length();
```

Visualization:

| Character | A | l | e | x |
|------------|---|---|---|---|
| Index | 0 | 1 | 2 | 3 |

Number of characters:

```java
size == 4
```

The returned value can be stored in a variable or used directly in expressions.

---

# The charAt() Method

The `charAt()` method returns a character at a specific index.

<!-- column -->
Example:

```java
String word = "Java";

char first = word.charAt(0);
```

<!-- column -->

Result:

```java
first == 'J'
```

<!-- endcolumns -->

Visualization:

| Character | J | a | v | a |
|------------|---|---|---|---|
| Index | 0 | 1 | 2 | 3 |



Remember:

- Strings start at index 0
- The index must be valid
- The return type is `char`

---

# Combining Methods

Method calls can be chained together.

Example:

```java
keyboard.next().charAt(0);
```

Java evaluates the expression from left to right.

1. `next()` reads a word and returns a String
2. `charAt(0)` is called on that String
3. The first character is returned

This works because methods can return objects or values that are immediately used by another method.

---

# Character Input Example

Suppose the user enters:

```
Hello
```

Code:

```java
char letter =
        keyboard.next().charAt(0);
```

Step by step:

1. `next()` returns `"Hello"`
2. `charAt(0)` accesses index 0
3. `'H'` is returned
4. `'H'` is stored in `letter`

Result:

```java
letter == 'H'
```
---

# Method Chaining

Methods can return objects.

When a method returns an object, we can immediately call another method on the returned object.

<!-- column -->

Example:

```java
keyboard.next().charAt(0);
```


<!-- column -->

Step by step:

```java
keyboard.next()
```

returns a String.

Then:

```java
.charAt(0)
```

is called on that String.

---

# Method Chaining In General

This technique is called **method chaining**.

General pattern:

```java
object.method1().method2().method3();
```

Each method returns something that the next method can use.

---

# Method Chaining with Multiple Objects

Method chaining is common when objects contain other objects.

Suppose we have these classes:

<!-- column -->

```java
public class Adkdress
{
    private String city;

    public String getCity()
    {
        return city;
    }
}
```

<!-- column -->

```java
public class Student
{
    private Address address;

    public Address getAddress()
    {
        return address;
    }
}
```

---

A Student object contains an Address object.

We can access the city using:

```java
student.getAddress().getCity();
```

Step by step:

1. `getAddress()` returns an Address object
2. `getCity()` is called on that Address object
3. The city name is returned

This is another example of method chaining.

---

# Following the Chain

<!-- column -->

Suppose:

```java
Student student = new Student();
```

And the Student contains an Address object whose city is:

```java
"Portland"
```

This statement:

```java
String city =
        student.getAddress().getCity();
```

<!-- column -->

can be visualized as:

```text
student
   ↓
Address object
   ↓
"Portland"
```

The first method gets an object.

The second method uses that object.

The final result is stored in `city`.

```java
city == "Portland"
```

<!-- endcolumns -->

> Method chaining allows us to navigate through related objects with a single expression.
`
---

# More Examples: Scanner Objects

The Scanner class allows programs to read user input.

Example:

```java
Scanner input =
        new Scanner(System.in);
```

This creates a Scanner object connected to the keyboard.

Once created, we can call Scanner methods to read data from the user.

Example:

```java
int age = input.nextInt();
```

The method reads an integer and returns its value.

---

# Common Scanner Methods

Different Scanner methods read different kinds of input.

```java
input.nextInt();
input.nextDouble();
input.next();
input.nextLine();
```

| Method | Reads |
|----------|----------|
| `nextInt()` | Integer |
| `nextDouble()` | Decimal number |
| `next()` | One word |
| `nextLine()` | Entire line |

The Scanner object stays the same, but we call different methods depending on the type of input we want to read.

---

# Scanner Example

<!-- column -->
Suppose the user enters:

```
25
```

<!-- column -->

Code:

```java
Scanner input =
        new Scanner(System.in);

int age = input.nextInt();
```

<!-- endcolumns -->

What happens?

1. The Scanner object waits for input
2. The user enters `25`
3. `nextInt()` converts the input to an `int`
4. The value is stored in `age`

Result:

```java
age == 25
```

---

# Objects and Methods

<!-- column -->

Notice the pattern:

```java
name.length();
```

```java
name.toUpperCase();
```

```java
name.charAt(0);
```

```javak
input.nextInt();
```

```java
input.nextLine();
```

<!-- column -->

In every example:

1. We have an object
2. We use dot notation
3. We call a method that belongs to that object

<!-- endcolumns -->

> This object-method relationship is a core idea of Object-Oriented Programming.

---

# Key Takeaways

- `String` and `Scanner` are classes.
- Objects are created from classes.
- A String object stores text.
- A Scanner object reads user input.
- Methods define behaviors associated with objects.
- Method calls use dot notation.
- Many Java statements involve calling methods on objects.

> Understanding classes, objects, and methods helps explain how the Java code we write every day works.