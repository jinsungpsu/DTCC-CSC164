# Wrapper Classes

## Overview

- Primitive types vs object types
- Wrapper classes and why they exist
- Wrapper classes for each primitive type
- Autoboxing
- Unboxing
- Useful wrapper methods
- Wrapper class constants

Goal:

Understand how Java represents primitive values as objects and how wrapper classes provide additional functionality.

---

# Wrapper Classes

Java has two major categories of data types:

- Primitive types
- Object types

<!-- column -->

Primitive examples:

```java
int
double
char
boolean
```

<!-- column -->

Object (Reference) examples:

```java
String
Scanner
Integer
Double
```

<!-- endcolumns -->

For every primitive type, Java provides a corresponding wrapper class.

---

# Primitive Types and Wrappers

| Primitive | Wrapper Class |
|------------|------------|
| byte | Byte |
| short | Short |
| int | Integer |
| long | Long |
| float | Float |
| double | Double |
| char | Character |
| boolean | Boolean |

---

Examples:

```java
int age = 18;

Integer ageObj = 18;
```

```java
double gpa = 3.75;

Double gpaObj = 3.75;
```

The wrapper stores the primitive value inside an object.

---

# Primitives vs Objects

Consider:

```java
int num = 42;
```

`num` is a primitive value.

Now compare:

```java
Integer numObj = 42;
```

`numObj` is an object.

Because wrapper classes are objects, they can:

- Have methods
- Have constants
- Be passed around like other objects
- Participate in object-oriented programming

---

# Why Do Wrapper Classes Exist?

Java's primitive types are simple and efficient.

```java
int score = 100;
```

However, primitives cannot contain methods.

Wrapper classes provide an object-oriented version of primitive data.

Example:

```java
Integer score = 100;
```

Wrapper classes give Java a place to provide useful methods and constants related to primitive values.

---

# Wrapper Objects Behave Like Other Objects

We have already used objects such as:

```java
String name = "Alex";
```

```java
Scanner input =
        new Scanner(System.in);
```

Wrapper classes create objects too:

```java
Integer age = 18;

Double price = 4.99;
```

Even though they represent numbers, they are still objects created from classes.

---

# Autoboxing

Java automatically converts primitives into wrapper objects.

Example:

```java
Integer num = 5;
```

Behind the scenes, Java converts:

```java
5
```

into an Integer object.

This automatic conversion is called **autoboxing**.

Another example:

```java
Double d = 3.14;
```

Java automatically creates the wrapper object.

---

# Unboxing

Java can also convert wrapper objects back into primitives.

Example:

```java
Integer num = 25;

int value = num;
```

Java automatically extracts the primitive value.

This process is called **unboxing**.

Result:

```java
value == 25
```

---

# Autoboxing and Unboxing Together

Java frequently performs these conversions automatically.

Example:

```java
Integer num = 25;

System.out.println(num + 5);
```

What happens?

1. `num` is an Integer object
2. Java unboxes it to an `int`
3. The addition occurs
4. The result is displayed

Output:

```text
30
```

Most of the time these conversions happen behind the scenes.

---

# Useful Wrapper Methods

Wrapper classes provide many useful methods.


<!-- column -->
Convert text into numbers:


```java
int num =
        Integer.parseInt("42");
```

```java
double d =
        Double.parseDouble("3.14");
```

<!-- column -->

Results:

```java
num == 42
```

```java
d == 3.14
```

<!-- endcolumns -->

These methods are commonly used when working with text input.

---

# Converting Numbers to Other Formats

The Integer class contains several utility methods.

Example:

```java
Integer.toBinaryString(10);
```

Result:

```text
1010
```

Example:

```java
Integer.toHexString(255);
```

Result:

```text
ff
```

Wrapper classes provide many tools beyond simply storing values.

---

# Integer Constants

The Integer class also provides useful constants.

Example:

```java
System.out.println(
        Integer.MAX_VALUE);
```

Output:

```text
2147483647
```

Example:

```java
System.out.println(
        Integer.MIN_VALUE);
```

Output:

```text
-2147483648
```

These values represent the largest and smallest possible `int`.

---

# Common Wrapper Classes

Some wrapper classes are used more frequently than others.

```java
Integer
Double
Character
Boolean
```

Examples:

```java
Integer.parseInt("100");
```

```java
Double.parseDouble("4.5");
```

```java
Character.isDigit('7');
```

```java
Boolean.parseBoolean("true");
```

Each wrapper class contains methods related to its data type.

---

# Summary

- Wrapper classes are object versions of primitive types.
- Every primitive type has a corresponding wrapper class.
- Wrapper objects behave like other Java objects.
- Autoboxing converts primitives into wrapper objects.
- Unboxing converts wrapper objects back into primitives.
- Wrapper classes contain useful methods and constants.
- Common wrapper classes include:
  - `Integer`
  - `Double`
  - `Character`
  - `Boolean`
- Wrapper classes help connect primitive data with object-oriented programming.