# The `this` Keyword

## Overview

- What `this` refers to
- Calling methods with `this`
- Accessing instance variables with `this`
- Resolving naming conflicts
- Why `this` cannot be used in static methods

Goal:

Understand how `this` refers to the current object and how it helps objects access their own data and behavior.

---

# What Is `this`?

`this` refers to the **current object**.

When a method is running, Java knows which object called that method.

Inside the method:

```java
this
```

represents that object.

Example:

```java
Car car1 = new Car();

car1.drive();
```

While `drive()` is executing:

```java
this
```

refers to:

```java
car1
```

---

# Using `this` with Methods

An object can call its own methods using `this`.

Example:

```java
public void drive()
{
    this.accelerate();
}
```

Equivalent to:

```java
public void drive()
{
    accelerate();
}
```

Java automatically assumes the method belongs to the current object.

Using `this` is optional in many cases but can improve readability.

---

# Visualizing `this`

Suppose we have:

```java
Car myCar = new Car();
```

Method call:

```java
myCar.drive();
```

Inside `drive()`:

```java
this.accelerate();
```

Java interprets it as:

```java
myCar.accelerate();
```

Visualization:

```text
this
 |
 v
myCar
```

`this` points to the object currently executing the method.

---

# Accessing Instance Variables

`this` is commonly used to access instance variables.

Example:

```java
public void setModel(String model)
{
    this.model = model;
}
```

The current object stores its value in:

```java
this.model
```

Using `this` makes it clear we are working with the object's data.

---

# Why Do We Need `this`?

Consider:

```java
public Car(String model)
{
    model = model;
}
```

This does **not** do what we want.

Both references point to the parameter:

```java
model
```

The instance variable never changes.

---

# Resolving Naming Conflicts

The correct version is:

```java
public Car(String model)
{
    this.model = model;
}
```

Left side:

```java
this.model
```

The object's instance variable.

Right side:

```java
model
```

The constructor parameter.

Visualization:

```text
this.model = model
     ↑        ↑
 instance  parameter
 variable
```

`this` removes the ambiguity.

---

# Another Example

Suppose the class contains:

```java
private int year;
```

Constructor:

```java
public Car(int year)
{
    this.year = year;
}
```

Without `this`, Java cannot distinguish between:

- The instance variable
- The parameter

Using `this` clearly identifies the object's variable.

---

# `this` Refers to the Current Object

Imagine two objects:

```java
Car car1 = new Car("Honda");

Car car2 = new Car("Toyota");
```

When `car1` executes a method:

```java
this
```

refers to `car1`.

When `car2` executes the same method:

```java
this
```

refers to `car2`.

Each object gets its own version of `this`.

---

# Common Uses of `this`

You will most often see `this` used for:

Accessing instance variables:

```java
this.model
```

Calling methods:

```java
this.accelerate();
```

Constructor chaining:

```java
this("Unknown");
```

In every case, `this` refers to the current object.

---

# `this` in Static Methods

Consider:

```java
public static void test()
{
    this.drive();
}
```

This code is invalid.

Java will generate an error.

---

# Why Doesn't This Work?

Static methods belong to the class itself.

Example:

```java
Math.sqrt(25);
```

No object is involved.

Because static methods are not associated with a specific object:

- No current object exists
- No instance variables exist
- No `this` reference exists

Therefore:

```java
this
```

cannot be used inside a static method.

---

# Instance Methods vs Static Methods

Instance method:

```java
public void drive()
{
    this.accelerate();
}
```

Works because an object is executing the method.

Static method:

```java
public static void test()
{
    this.accelerate();
}
```

Invalid because no object is involved.

Rule:

- Instance methods can use `this`
- Static methods cannot use `this`

---

# Key Takeaways

- `this` refers to the current object.
- `this` can access instance variables.
- `this` can call other instance methods.
- `this.variable` helps distinguish instance variables from parameters.
- `this` is commonly used in constructors and setters.
- Every object has its own `this` reference while executing methods.
