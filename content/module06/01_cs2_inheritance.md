# Inheritance & Polymorphism

---

# Superclasses and Subclasses

A **superclass** is a class that is inherited from by one or more subclasses.

A **subclass** is a class that inherits from a superclass.

---

# Defining a Subclass

- Add new properties
- Add new methods
- Override methods of the superclass

```java
class Cat extends Animal {
    // ...
}
```

---

# Examples

```java
class Animal {
    int age;
}

class Cat extends Animal {
    String name;
}
```

---

# Cat or animal

- A cat is an animal.
- All animals have an age.
- Cats have names.
- Animals do not have names.

---

# Inheritance Chain

- class Animal
- class Mammal extends Animal
- class Cat extends Mammal

---

# … is a … relationship

- A mammal is an animal
- A cat is a mammal

---

# Keyword super

The super keyword is used in Java to refer to the parent (superclass) of a subclass.

---

# Access Parent Class Constructors

```java
class Parent {
    Parent() {
        System.out.println("Parent Constructor");
    }
}

class Child extends Parent {
    Child() {
        super();
        System.out.println("Child Constructor");
    }
}
```

---

# Call Superclass Methods

```java
super.display();
```

---

# Access Parent Class Variables

```java
System.out.println(super.x);
```

---

# Constructors and Inheritance

- Constructors are still just constructors.
- Used to initialize objects.

---

# Constructor Chaining

- Each constructor call is implicitly or explicitly called up the inheritance chain.

---

# Overriding

- Subclasses override behavior defined in a superclass.
- Methods have the same signature.

---

# Overriding vs Overloading

- Overriding methods has to do with inheritance.
- Overloading methods has to do with method signatures.

---

# Object Class

- The Object class is the root class of all Java classes.
- Every class in Java implicitly extends Object.

---

# toString()

- Returns a string representation of an object.
- Commonly overridden.

---

# Object class toString definition

```java
public String toString() {
    return getClass().getName() + "@" + Integer.toHexString(hashCode());
}
```

---

# Why Override toString()?

- Makes debugging easier.
- Provides meaningful object descriptions.
- Enhances readability.

---

# Cat class toString

```java
@Override
public String toString() {
    return "Cat named: " + name + ", age: " + age;
}
```

---

# Polymorphism

---

# Poly, Morph

- Many
- Forms

---

# Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass.

---

# Practically…

A supertype reference variable can refer to ANY subclass object.

---

# Generic Programming

An Animal reference variable can be used for:
- Cat objects
- Animal objects

---

# Object class…

An Object reference variable can refer to ANY object.

---

# instanceof Operator

The `instanceof` operator checks whether an object is an instance of a specified type.

---

# Why Learn OOP?

---

# Use Existing Classes

- OOP isn't just about writing classes.
- It's about using powerful, reusable classes.
- Real software is built from many interacting objects.

---

# Using Existing Classes

- Java gives us thousands of ready-made classes.
- Example: ArrayList.

---

# OOP Simplifies Complex Tasks

- Objects bundle data and behavior.
- We call simple methods; the object handles the details.

---

# Abstraction

- OOP hides complicated internal code.
- We just use the public methods.

---

# Polymorphism

- Methods can work with many object types.
- Makes code flexible and reusable.

---

# ArrayList Class

---

# ArrayList Introduction

- It's a class.
- Must import `java.util.ArrayList`.
- Handles resizing automatically.

---

# Public methods

- Constructors
- Setters
- Getters
- toString

---

# Constructors

```java
ArrayList<Integer> nums = new ArrayList<>();
```

---

# Setters

```java
nums.set(2, 99);
```

---

# Getters

```java
int someNum = nums.get(2);
```

---

# And much, much more

![ArrayList methods](images/arraylist-methods-reference.png)

---

# Java documentation

- contains
- clear
- indexOf
- remove
- toString

---

# Differences and Similarities vs Array

---

# Resources

- https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html
- https://www.w3schools.com/java/java_arraylist.asp

---

# Practice

- https://www.w3resource.com/java-exercises/collection/index.php#arraylist
