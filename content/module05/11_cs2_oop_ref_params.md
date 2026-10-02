# Passing Objects as Parameters

## Overview

- Passing objects to methods
- How object parameters work
- References and memory
- Comparing objects and primitives
- Benefits of passing objects
- Object collaboration

Goal:

Understand what happens when an object is passed to a method and how multiple parts of a program can work with the same object.

---


# Passing Objects as Parameters

Variables are often passed to methods.

We can pass:

- Primitive values
- Objects

Example:

```java
public static void wash(Car car)
{
    car.clean();
}
```

Method call:

```java
wash(myCar);
```

The object stored in `myCar` is passed to the method so it can be used inside the method.

---

# Objects Can Work Together

One major goal of OOP is allowing objects and methods to work together.

Example:

```java
public static void printCar(Car car)
{
    System.out.println(
            car.getModel());
}
```

Method call:

```java
printCar(myCar);
```

The method does not create a Car.

Instead, it receives an existing Car object and uses its methods.

---

# Example: Student Object

Suppose we have a Student class:

```java
Student student =
        new Student("Alex");
```

Method:

```java
public static void greet(
        Student student)
{
    System.out.println(
        student.getName());
}
```

Call:

```java
greet(student);
```

Output:

```text
Alex
```

Objects can be passed just like variables.

---

# What Happens Behind the Scenes?

When an object is passed to a method:

- A copy of the reference is passed
- No new object is created
- Both references point to the same object

Example:

```java
wash(myCar);
```

Visualization:

```text
myCar ----\
           --> Car Object
car   ----/
```

Both variables refer to the same object in memory.

---

# No New Object Is Created

Consider:

```java
Car myCar = new Car();
```

Then:

```java
wash(myCar);
```

The method receives a reference to the existing object.

Java does **not** perform:

```java
new Car();
```

automatically.

The same Car object is used both inside and outside the method.

---

# Changes Affect the Same Object

Suppose:

```java
public static void wash(Car car)
{
    car.setClean(true);
}
```

Method call:

```java
wash(myCar);
```

After the call:

```java
myCar.isClean()
```

returns:

```java
true
```

The object's data changed because both references point to the same object.

---

# Example Walkthrough

Before the call:

```text
myCar
  |
  v
Car Object
clean = false
```

Method call:

```java
wash(myCar);
```

Inside the method:

```java
car.setClean(true);
```

After the call:

```text
myCar
  |
  v
Car Object
clean = true
```

The object itself was modified.

---

# Passing Primitive Values

Primitives behave differently.

Example:

```java
public static void addOne(int num)
{
    num++;
}
```

Call:

```java
int x = 5;

addOne(x);
```

After the method:

```java
x == 5
```

The original variable is unchanged.

---

# Comparing the Two

Object example:

```java
wash(myCar);
```

The method can modify the object's state.

Primitive example:

```java
addOne(x);
```

The method only receives a copy of the value.

General rule:

- Objects share access to the same object
- Primitives receive their own copy of the value

---

# Why Pass Objects?

Passing objects allows methods to:

- Read object data
- Update object data
- Reuse functionality
- Work with many different objects

Example:

```java
printCar(car1);

printCar(car2);

printCar(car3);
```

One method can work with many objects.

---

# Object Collaboration

Objects frequently work together in larger programs.

Examples:

- A Student object passed to a registration method
- A Car object passed to a repair method
- A BankAccount object passed to a deposit method

Example:

```java
deposit(account, 100);
```

Methods can receive objects, use their methods, and update their state when necessary.

This allows classes to cooperate while keeping responsibilities separate.

---

# Key Takeaways

- Objects can be passed as parameters to methods.
- Java passes a copy of the object's reference.
- No new object is created when an object is passed.
- Multiple references can refer to the same object.
- Methods can access and modify an object's state.
- Primitive values and objects behave differently when passed to methods.
- Passing objects allows methods and classes to work together effectively.