# Instance vs Static

## Overview

- Instance variables
- Instance methods
- Static variables
- Static methods
- Differences between instance and static members
- When to use each

Goal:

Understand which members belong to individual objects and which belong to the class itself.

---

# Two Types of Class Members

Classes commonly contain:

- Instance members
- Static members

Instance members belong to objects.

Static members belong to the class.

Example:

```java
public class Car
{
    private String model;      // Instance

    private static int count;  // Static
}
```

Understanding the difference is essential when designing classes.

---

# Instance Variables

**Instance variables belong to objects.**

Example:

```java
public class Car
{
    private String model;
    private int year;
}
```

Characteristics:

- Declared inside a class
- Outside methods
- Store object data
- Every object gets its own copy

Instance variables describe the state of an object.

---

# Instance Variable Example

Creating objects:

```java
Car car1 = new Car("Ford");
Car car2 = new Car("Tesla");
```

Conceptually:

```text
car1.model -> Ford
car2.model -> Tesla
```

Each object stores its own values.

Changing one object does not automatically change another.

---

# Another Instance Variable Example

Suppose the class contains:

```java
private int speed;
```

Two objects:

```java
Car car1 = new Car();
Car car2 = new Car();
```

After:

```java
car1.setSpeed(60);
car2.setSpeed(30);
```

Conceptually:

```text
car1.speed -> 60
car2.speed -> 30
```

Every object has its own copy of instance variables.

---

# Instance Methods

Instance methods belong to objects.

Example:

```java
public void accelerate()
{
    speed++;
}
```

Method call:

```java
car.accelerate();
```

Instance methods typically work with the data stored inside an object.

---

# Instance Methods Work With Object Data

Example:

```java
private String model;

public void printModel()
{
    System.out.println(model);
}
```

Method call:

```java
car.printModel();
```

The method can access the object's instance variables because it belongs to that object.

---

# Example: Multiple Objects

Suppose we have:

```java
Car car1 = new Car();
Car car2 = new Car();
```

Method call:

```java
car1.accelerate();
```

Only `car1` is affected.

Conceptually:

```text
car1.speed -> increased
car2.speed -> unchanged
```

Instance methods work with one object at a time.

---

# Static Variables

**Static variables belong to the class, not individual objects.**

Example:

```java
public class Car
{
    public static int count = 0;
}
```

Characteristics:

- Shared by all objects
- Only one copy exists
- Created when the class is loaded

Every object sees the same static variable.

---

# Visualizing Static Variables

Instance variables:

```text
car1.model -> Ford
car2.model -> Tesla
```

Static variables:

```text
Car.count -> 2
```

There is only one shared copy.

All objects access the same variable.

---

# Why Use Static Variables?

Static variables are useful when data should be shared.

Examples:

- Counting objects
- Shared settings
- Application-wide values
- Constants

Example:

```java
Car.count++;
```

All Car objects see the same value.

---

# Static Variable Example

```java
public class Car
{
    public static int count = 0;

    public Car()
    {
        count++;
    }
}
```

Creating objects:

```java
new Car();
new Car();
```

Display:

```java
System.out.println(Car.count);
```

Output:

```text
2
```

The count is shared among all Car objects.

---

# Instance vs Static Variables

Instance variable:

```java
private String model;
```

Static variable:

```java
private static int count;
```

Key difference:

```text
Instance -> One copy per object
Static   -> One copy per class
```

Ask yourself:

"Should every object have its own value?"

If yes, use an instance variable.

---

# Static Methods

Static methods belong to the class.

Example:

```java
public static void sayHello()
{
    System.out.println("Hello");
}
```

Method call:

```java
MyClass.sayHello();
```

No object is required.

---

# Common Static Method Examples

You have already used static methods.

Example:

```java
Math.sqrt(25);
```

Example:

```java
Math.pow(2, 3);
```

Example:

```java
Integer.parseInt("42");
```

Notice:

```java
Math
```

and

```java
Integer
```

are class names, not object names.

---

# Why Make a Method Static?

A method should often be static when it does not need object data.

Example:

```java
public static int add(int a,
                      int b)
{
    return a + b;
}
```

The method only uses parameters.

It does not rely on object-specific data.

No object is necessary.

---

# Static Methods Cannot Directly Access Instance Variables

Suppose a class contains:

```java
private String model;
```

This is invalid:

```java
public static void printModel()
{
    System.out.println(model);
}
```
---

# Why?

Because a static method belongs to the class.

There may be many Car objects, each with a different model.

Java would not know which object's model to use.

---

# Instance Methods Can Access Static Variables

Instance methods can use shared class data.

Example:

```java
public void displayInfo()
{
    System.out.println(count);
}
```

Since there is only one shared copy of a static variable, every object can access it.

---

# Static vs Instance Methods

| Static Method | Instance Method |
|---|---|
| Belongs to class | Belongs to object |
| No object required | Object required |
| Called with class name | Called with object reference |
| Usually works with shared data | Usually works with object data |
| Cannot directly access instance variables | Can access instance variables |

---

# Memory Summary

Suppose:

```java
Car car1 = new Car("Ford");
Car car2 = new Car("Tesla");
```

Conceptually:

```text
car1.model -> Ford
car2.model -> Tesla

Car.count -> 2
```

Notice:

- Each object has its own model
- The class has one shared count

This is the fundamental difference between instance and static members.

---

# Looking Ahead

We have seen that instance methods work with object data.

Example:

```java
car1.accelerate();
```

```java
car2.accelerate();
```

The same method can be called by different objects.

How does Java know which object's data a method should work with?

In the next lesson, we'll learn about the special keyword:

```java
this
```

which allows an object to refer to itself.

---

# Key Takeaways

- Instance variables belong to individual objects.
- Each object gets its own copy of instance variables.
- Instance methods operate on object data.
- Static variables belong to the class.
- Static variables are shared by all objects.
- Static methods belong to the class.
- Static methods are called using the class name.
- Instance methods can access static variables.
- Static methods cannot directly access instance variables.
- Use instance members for object-specific data and static members for shared data.