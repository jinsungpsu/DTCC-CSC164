# CSC164 Exam 2 Review

---

# Exam Instructions/Policies

This assessment is closed resource (no notes, powerpoint, textbook, internet, etc.). If you open another internet browser or tab, it will be considered cheating. You may not leave the testing area for any reason. If you have any extenuating circumstances that may require any exceptions, please let the instructor/proctor know as soon as you can.

This assessment MUST be completed using D2L on a lab computer during the scheduled time and location; you may not use your own device or take this assessment at a different location without prior approval.

---

## Topics Covered

- OOP Fundamentals
- Classes vs Objects
- Primitive vs Reference Types
- Encapsulation
- Constructors and Overloading
- Setters and Getters
- Static vs Instance Members
- Reference Variables and null
- Arrays of Objects
- Reading and Tracing Code

---

# What Should You Expect?

The exam focuses heavily on:

- Understanding OOP terminology
- Reading Java code
- Determining whether code compiles
- Determining what code outputs
- Understanding objects and references
- Writing simple methods
- Writing constructors
- Working with arrays of objects

---

# What is OOP?

Object-Oriented Programming (OOP) organizes code into objects.

Objects contain:

- State (variables)
- Behavior (methods)

Example:

```java
Student student = new Student();

student.study();
student.takeExam();
```

Benefits:

- Organization
- Reusability
- Easier maintenance
- Better modeling of real-world concepts

---

# Class vs Object

<!-- column -->

## Class

Blueprint

Defines:

- Variables
- Methods
- Constructors

Example:

```java
class Student {

}
```

<!-- column -->

## Object

An instance of a class

Example:

```java
Student s1 = new Student();
Student s2 = new Student();
```

Each object has its own data.

---

# Practice Check

### Which is the class?

```java
Student s1 = new Student();
```

### Answer

<div class="fragment">

```java
Student
```

The class acts as the blueprint.

</div>

---

# Practice Check

### Which is the object reference variable?

```java
Student s1 = new Student();
```

### Answer

<div class="fragment">

```java
s1
```

The reference variable stores a reference to the object.

</div>

---

# Primitive vs Reference Types

<!-- column -->

## Primitive Types

Store actual values.

Examples:

```java
int
double
char
boolean
```

<!-- column -->

## Reference Types

Store references to objects.

Examples:

```java
String
Scanner
Student
Integer
```

<!-- footer -->
Nearly every type that begins with a capital letter is a class/reference type.

---

# Reference Type or Primitive?

### Determine whether each is primitive or reference.

```text
boolean
String
double
Integer
Scanner
char
```

### Answer

<div class="fragment">

Primitive:

```java
boolean
double
char
```

Reference:

```java
String
Integer
Scanner
```

</div>

---

# Encapsulation

Encapsulation means:

- Keeping data and methods together
- Restricting direct access to data

Usually:

```java
private
```

variables

and

```java
public
```

methods

---

# Why Use Private Variables?

Instead of:

```java
account.balance = -1000000;
```

We can control access through methods.

Example:

```java
account.deposit(100);
```

Benefits:

- Protects data
- Allows validation
- Reduces bugs

---

# Setters and Getters

Setter:

```java
public void setName(String name) {
    this.name = name;
}
```

Getter:

```java
public String getName() {
    return name;
}
```

Remember:

- Setters modify values
- Getters return values

---

# The this Keyword

`this` refers to the current object.

```java
private String title;

public void setTitle(String title) {
    this.title = title;
}
```

Without `this`, Java cannot distinguish between:

```java
title
```

- parameter

and

```java
title
```

- instance variable

---

# Practice Check

### What does `this` refer to?

```java
public void setYear(int year){
    this.year = year;
}
```

### Answer

<div class="fragment">

`this.year`

refers to the instance variable belonging to the current object.

</div>

---

# Constructors

Constructors initialize objects.

Example:

```java
public Student() {

}
```

Rules:

- Same name as class
- No return type
- Runs automatically when an object is created

---

# Constructor Example

```java
public Student(String name) {
    this.name = name;
}
```

Usage:

```java
Student s =
    new Student("Alice");
```

---

# Constructor Overloading

A class may have multiple constructors.

```java
public Student() {

}

public Student(String name) {

}

public Student(String name, double gpa) {
  ...
}
```

Different parameter lists are required.

---

# Important: No Return Type

Correct:

```java
public Student() {

}
```

Wrong:

```java
public void Student() {

}
```

Once a return type appears, it becomes a regular method.

---

# Default Constructors

If no constructor is written:

```java
class Student {

}
```

Java automatically provides a default constructor.

This works:

```java
Student s =
    new Student();
```

---

# Default Constructor Rule

Suppose we write:

```java
public Student(String name){

}
```

Now Java does NOT automatically provide:

```java
Student()
```

This would fail:

```java
new Student();
```

unless we write that constructor ourselves.

---

# Practice Check

### Will this compile?

```java
class Course {

    public Course(String name){

    }

}

Course c = new Course();
```

### Answer

<div class="fragment">

No.  The only constructor available is:

```java
Course(String name)
```

A no-argument constructor does not exist.

</div>

---

# Method Overloading

Methods may have the same name if parameter lists differ.

```java
public void addScore(int score)

public void addScore(
    int score1,
    int score2
)
```

This is called overloading.

---

# Visibility Modifiers

## public

Accessible from other classes.

```java
public void study() {

}
```

## private

Accessible only inside the class.

```java
private double gpa;
```

---

# Static vs Instance Variables

<!-- column -->

## Instance Variable

One copy per object.

```java
private String name;
```

Each object has its own value.

<!-- column -->

## Static Variable

One copy for entire class.

```java
private static int count;
```

Shared by all objects.

---

# Static vs Instance Methods

Static:

```java
Math.sqrt(16);
```

No object needed.

Instance:

```java
student.study();
```

Requires an object.

---

# Practice Check

### True or False

A static method may be called without creating an object.

### Answer

<div class="fragment">

True

Example:

```java
Math.sqrt(25);
```

</div>

---

# Reference Variables

A reference variable refers to an object.

Example:

```java
Book myBook;
```

The variable does not contain the object itself.

It refers to the object.

---

# The null Value

```java
Book myBook = null;
```

Means:

```text
No object exists
```

or

```text
Refers to nothing
```

---

# Practice Check

### Will this compile?

```java
double x = null;
```

### Answer

<div class="fragment">

No.

`null` may only be assigned to reference variables.

</div>

---

# Reference Assignment

Consider:

```java
Book b1 =
    new Book();

Book b2 =
    new Book();

b1 = b2;
```

After assignment:

```text
b1 and b2
refer to the same object
```

---

# Reference Assignment Example

```java
Book b1 =
    new Book();

Book b2 =
    new Book();

b1 = b2;
```

Remember:

```java
=
```

copies the reference,

NOT the object.

---

# Practice Check

### How many objects remain referenced?

```java
Book b1 =
    new Book();

Book b2 =
    new Book();

b1 = b2;
```

### Answer

<div class="fragment">

One.

The original object referenced by `b1`
no longer has a reference pointing to it.

</div>

---

# Arrays of Objects

```java
Movie[] movies =
    new Movie[5];
```

Creates:

```text
5 reference variables
```

It does NOT create five Movie objects.

---

# What Does the Array Contain?

```java
Movie[] movies =
    new Movie[3];
```

Immediately after creation:

```text
movies[0] = null
movies[1] = null
movies[2] = null
```

No Movie objects exist yet.

---

# Creating Objects Inside the Array

```java
Movie[] movies =
    new Movie[3];

movies[0] =
    new Movie();
```

Now:

```text
movies[0]
```

contains a Movie object.

---

# Practice Check

### What is wrong?

```java
Movie[] movies =
    new Movie[3];

movies[0].play();
```

### Answer

<div class="fragment">

`movies[0]` is still null.

A Movie object must be created first:

```java
movies[0] =
    new Movie();
```

</div>

---

# Reading Object Creation Statements

```java
Course myCourse =
    new Course();
```

Know how to identify each part.

---

# Practice Check

### Identify each part

```java
Course myCourse =
    new Course();
```

### Answer

<div class="fragment">

```java
Course
```

Reference Type

```java
myCourse
```

Reference Variable

```java
Course()
```

Constructor

</div>

---

# Mini Review

Know how to:

<!-- column -->
- Identify classes and objects

- Identify primitive and reference types

- Explain encapsulation

- Write setters

- Write getters

- Explain `this`


- Write constructors
<!-- column -->

- Explain overloading

- Explain default constructors

- Explain static vs instance members

- Explain null

- Trace references

- Use arrays of objects

- Identify common runtime errors

---

# Practice Programming

Create a `VideoGame` class.

Requirements:

- title
- genre
- hoursPlayed

Include:

- Constructor
- Setters
- Getters

Then create an array capable of storing 5 VideoGame objects.

---

# Practice Programming

Create a `Student` class.

Requirements:

- name
- major
- gpa

Write:

- A no-argument constructor
- A parameterized constructor
- Getters
- Setters

In `main`, create two Student objects and print their information.