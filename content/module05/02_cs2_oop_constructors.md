
# Constructors

How do we give objects starting values when they are created?

Current approach:

```java
Dog dog = new Dog();

dog.name = "Buddy";
dog.age = 3;
```

A constructor lets us do this automatically:

```java
Dog dog = new Dog("Buddy", 3);
```

---

# Constructors

A constructor is a special method that runs when an object is created.

<!-- column -->

```java
public class Dog {
    String name;
    int age;

    Dog() {
        System.out.println("A Dog object was created!");
    }
}
```

<!-- column -->

Creating an object:

```java
Dog dog = new Dog();
```

<!-- endcolumns -->

### Key Idea

- Constructors initialize new objects
- Called automatically when using `new`
- Constructor name must match the class name

---

# Constructor Syntax

A constructor looks similar to a method, but has no return type.

```java
public class Dog {
    Dog() {
        System.out.println("Constructor running...");
    }
}
```

### Constructor Rules

✅ Same name as the class

✅ No return type

✅ Runs automatically during object creation

❌ Not called like a regular method

---

# Default Constructor

If you do not write any constructors, Java provides a default constructor.

<!-- column -->

```java
public class Dog {
    String name;
    int age;

}
```

<!-- column -->

This works:

```java
Dog dog = new Dog();
```

<!-- endcolumns -->

### Important

As soon as you create your own constructor, Java no longer provides the default constructor automatically.

---

# Initializing Fields

Constructors are commonly used to give objects starting values.

<!-- column -->

```java
public class Dog {
    String name;
    int age;

    Dog() {
        name = "Unknown";
        age = 0;
    }
}
```

<!-- column -->

Creating an object:

```java
Dog dog = new Dog();

System.out.println(dog.name);
System.out.println(dog.age);
```

### Output

```text
Unknown
0
```

---

# Parameterized Constructors

Parameters allow different objects to start with different values.

<!-- column -->

```java
public class Dog {
    String name;
    int age;

    Dog(String dogName, int dogAge) {
        name = dogName;
        age = dogAge;
    }
}
```

<!-- column -->

Creating objects:

```java
Dog dog1 = new Dog("Buddy", 3);
Dog dog2 = new Dog("Max", 5);
```

### Result

```text
dog1 → Buddy, 3
dog2 → Max, 5
```

---

# Using `this` in Constructors

Parameter names are often the same as field names.

<!-- column -->

```java
public class Dog {
    String name;
    int age;

    Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

<!-- column -->

### What Does This Mean?

```java
this.name
```

Refers to the object's field.

```java
name
```

Refers to the parameter.

<!-- endcolumns -->

### Key Idea

`this` helps distinguish object variables from constructor parameters.

---

# Multiple Constructors

A class can have more than one constructor.

<!-- column -->

```java
public class Dog {
    String name;
    int age;

    Dog() {
        name = "Unknown";
        age = 0;
    }

    Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

<!-- column -->

Using different constructors:

```java
Dog dog1 = new Dog();

Dog dog2 = new Dog("Buddy", 3);
```

<!-- endcolumns -->

### This Is Called

**Constructor Overloading**

---

# Constructor Overloading

Overloading means having multiple constructors with different parameter lists.

<!-- column -->

```java
public class Student {
    String name;
    double gpa;

    Student() {
        name = "Unknown";
        gpa = 0.0;
    }

    Student(String name) {
        this.name = name;
        gpa = 0.0;
    }

    Student(String name, double gpa) {
        this.name = name;
        this.gpa = gpa;
    }
}
```

<!-- column -->

Valid uses:

```java
Student s1 = new Student();
Student s2 = new Student("Alex");
Student s3 = new Student("Taylor", 3.8);
```

---

# Constructors vs Methods

Constructors and methods look similar but serve different purposes.

### Constructor

```java
Dog(String name) {
    this.name = name;
}
```

### Method

```java
void bark() {
    System.out.println("Woof!");
}
```

---

### Constructors

- Run automatically
- Create and initialize objects
- No return type

### Methods

- Called explicitly
- Perform actions
- Usually have a return type or `void`

---

# Complete Example

<!-- column -->

```java
public class Student {
    String name;
    double gpa;

    Student(String name, double gpa) {
        this.name = name;
        this.gpa = gpa;
    }

    void displayInfo() {
        System.out.println(name + " - GPA: " + gpa);
    }
}
```

<!-- column -->

Using the class:

```java
Student s1 = new Student("Alex", 3.8);
s1.displayInfo();
```

### Output

```text
Alex - GPA: 3.8
```

<!-- endcolumns -->

### Key Idea

A constructor prepares an object for use immediately after it is created.

---

# Summary

### Constructors

- Have the same name as the class
- Have no return type
- Run automatically when an object is created
- Initialize object data

### Common Concepts

- Default Constructor
- Parameterized Constructor
- `this` Keyword
- Constructor Overloading

### Next Topic

**Visibility Modifiers (`public`, `private`, `protected`)**
