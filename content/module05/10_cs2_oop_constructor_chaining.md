# Constructor Chaining

## Overview

- What constructor chaining is
- Using `this(...)` to call another constructor
- Why constructor chaining is useful
- Rules for constructor chaining
- Constructor chaining examples

Goal:

Understand how multiple constructors can work together to initialize objects while avoiding duplicate code.

---

# Constructor Chaining

One constructor can call another constructor from the same class.

Example:

```java
public Car() {
    this("Unknown");
}

public Car(String model) {
    this.model = model;
}
```

<!-- column -->

When this code runs:

```java
Car car = new Car();
```

<!-- column -->

Java first calls:

```java
this("Unknown");
```

which then executes the second constructor.

---

# Why Constructor Chaining?

Without constructor chaining:

```java
public Car() {
    model = "Unknown";
}

public Car(String model) {
    this.model = model;
}
```

If we later change the initialization logic, we must update multiple constructors.

---

With chaining:

```java
public Car() {
    this("Unknown");
}
```

Initialization code exists in one place.

Benefits:

- Less duplicate code
- Easier maintenance
- Fewer bugs

---

# Constructor Chaining Example

Suppose a Car stores both a model and year.

```java
public Car() {
    this("Unknown", 2026);
}
```

```java
public Car(String model,
           int year) {
    this.model = model;
    this.year = year;
}
```
---

Creating:

```java
Car car = new Car();
```

Automatically produces:

```java
model = "Unknown"
year = 2026
```

---

# Chaining Multiple Constructors

A class can have several constructors.

```java
public Car() {
    this("Unknown");
}
```

```java
public Car(String model) {
    this(model, 2026);
}
```

```java
public Car(String model,
           int year) {
    this.model = model;
    this.year = year;
}
```

---

# Visual flow

```text
Car()
  ↓
Car(String)
  ↓
Car(String, int)
```

Each constructor adds more information.

---

# Rules for Constructor Chaining

When using:

```java
this(...)
```

it must be the first statement.

<!-- column -->

Valid:

```java
public Car() {
    this("Unknown");
}
```

<!-- column -->
Invalid:

```java
public Car() {
    model = "Unknown";
    this("Unknown");
}
```
<!-- endcolumns -->

Java requires constructor chaining to happen before other statements.

---

# Constructor Chaining vs this

Notice these two uses of `this`:

```java
this("Unknown");
```

```java
this.model = model;
```

They mean different things.

```java
this(...)
```

calls another constructor.

```java
this.variable
```

refers to the current object's instance variable.

The meaning depends on how `this` is used.

---

# Quick Example

<!-- column -->
Given:

```java
public class Student {
    private String name;

    public Student() {
        this("Unknown");
    }

    public Student(String name) {
        this.name = name;
    }
}
```

<!-- column -->

What happens?

```java
Student s = new Student();
```

Steps:

1. `Student()` executes
2. `this("Unknown")` is called
3. `Student(String name)` executes
4. `name` becomes `"Unknown"`

---

# Key Takeaways

- Constructors initialize objects.
- Constructor chaining uses:

```java
this(...)
```

- Chaining reduces duplicate code.
- `this(...)` calls another constructor.
- `this.variable` refers to the current object's instance variable.
- Every object has its own instance variables.
- Static methods belong to the class, not individual objects.