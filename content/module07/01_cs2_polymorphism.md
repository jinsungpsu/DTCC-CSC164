# Polymorphism in Java

## Overview
- What polymorphism means
- The relationship between inheritance and polymorphism
- Superclass references
- Subclass objects
- Why polymorphism is useful
- The `instanceof` operator
- Practical examples
- Real-world uses of polymorphism

---

# What Is Polymorphism?

The word **polymorphism** comes from:

- **Poly** = many
- **Morph** = forms

Polymorphism means that the same piece of code can work with objects in many different forms.

---

# Inheritance Comes First

Consider:

```java
class Animal {

}

class Cat extends Animal {

}

class Dog extends Animal {

}
```

Inheritance creates relationships between classes.

Polymorphism uses those relationships.

---

# A Cat Is an Animal

Because:

```java
class Cat extends Animal {

}
```

A cat **is an** animal.

That means a `Cat` object can be treated as an `Animal`.

This idea is the foundation of polymorphism.

---

# Superclass References

Consider:

```java
Animal animal;
```

The variable type is:

```java
Animal
```

This is called a **reference type**.

The variable can refer to an Animal object.

---

# Polymorphic References

```java
Animal a1 = new Animal();
Animal a2 = new Cat();
Animal a3 = new Dog();
```

All three variables use the same reference type:

```java
Animal
```

But each variable may refer to a different object type.

---

# Visualizing References

```text
Animal a1 → Animal object
Animal a2 → Cat object
Animal a3 → Dog object
```

One reference type can work with many related object types.

This is polymorphism.

---

# What Is Allowed?

Suppose:

```java
Animal pet = new Cat();
```

This is allowed because:

```text
Cat is an Animal
```

The subclass object can be stored in a superclass reference.

---

# What Is NOT Allowed?

```java
Cat pet = new Animal();
```

This is illegal.

Why?

```text
Animal is not necessarily a Cat
```

Not every animal is specifically a cat.

---

# Why Use Polymorphism?

Without polymorphism:

```java
washCat(Cat cat)
washDog(Dog dog)
washBird(Bird bird)
```

Lots of duplicated code.

---

# With Polymorphism

```java
public void washAnimal(Animal animal) {

}
```

Now a single method can work with:

- Cats
- Dogs
- Birds
- Any future Animal subclass

Polymorphism makes code more reusable.

---

# Example: Feeding Animals

```java
public void feed(Animal animal) {
    System.out.println("Feeding animal");
}
```

Calls:

```java
feed(new Cat());
feed(new Dog());
feed(new Bird());
```

One method works for many object types.

---

# Arrays and Polymorphism

Arrays can store polymorphic references.

```java
Animal[] animals = {
    new Cat(),
    new Dog(),
    new Cat()
};
```

Every element is stored as an `Animal` reference.

---

# Iterating Through Animal Objects

```java
Animal[] animals = {
    new Cat(),
    new Dog(),
    new Cat()
};

for (Animal animal : animals) {
    System.out.println(animal);
}
```

The loop does not need to know the exact subclass.

---

# What Is an ArrayList?

`ArrayList` is a Java class that stores a collection of objects.

Think of it as a more flexible array.

Features:

- Stores multiple values
- Keeps items in order
- Supports indexing
- Automatically grows as needed
- Automatically shrinks when items are removed

---

# Why Not Just Use Arrays?

Arrays have a fixed size.

```java
int[] numbers = new int[5];
```

Once created, the size cannot change.

ArrayLists can grow automatically:

```java
ArrayList<Integer> numbers =
    new ArrayList<>();
```

This makes ArrayLists useful when you do not know how much data you will need to store.

---

# Arrays vs ArrayLists

| Arrays | ArrayLists |
|----------|----------|
| Fixed size | Dynamic size |
| Use `[]` | Use methods |
| `length` field | `size()` method |
| Must know size ahead of time | Can grow automatically |
| Built into Java language | Class in Java library |

Both support indexing and ordered data.

---

# Importing and Creating an ArrayList

Before using ArrayList:

```java
import java.util.ArrayList;
```

Creating an ArrayList:

```java
ArrayList<String> names =
    new ArrayList<>();
```

- `ArrayList` is the class name
- `String` is the type of data stored
- `new` creates the object

---

# Adding Items

```java
ArrayList<String> names =
    new ArrayList<>();

names.add("Alice");
names.add("Bob");
names.add("Charlie");
```

Contents:

```text
[Alice, Bob, Charlie]
```

`add()` inserts a new item into the list.

---

# Accessing Items

```java
ArrayList<String> names =
    new ArrayList<>();

names.add("Alice");
names.add("Bob");
names.add("Charlie");

System.out.println(names.get(1));
```

Output:

```text
Bob
```

ArrayLists use zero-based indexing just like arrays.

---

# Modifying Items

```java
ArrayList<String> names =
    new ArrayList<>();

names.add("Alice");
names.add("Bob");

names.set(1, "Charlie");
```

Contents:

```text
[Alice, Charlie]
```

`set(index, value)` replaces an existing item.

---

# Finding the Number of Items

Arrays:

```java
arr.length
```

ArrayLists:

```java
names.size()
```

Example:

```java
System.out.println(names.size());
```

Output:

```text
2
```

Notice that arrays and ArrayLists use different syntax.

---

# Iterating Through an ArrayList

```java
ArrayList<String> names =
    new ArrayList<>();

names.add("Alice");
names.add("Bob");
names.add("Charlie");

for (int i = 0; i < names.size(); i++) {
    System.out.println(names.get(i));
}
```

Use:

- `size()` for the loop condition
- `get()` to access each item

---

# Common ArrayList Methods

```java
names.add("Alice");
names.get(0);
names.set(0, "Bob");
names.remove(0);
names.clear();
names.contains("Bob");
```

ArrayList provides many useful methods that arrays do not have built in.

---

# Collections and Polymorphism

Polymorphism becomes even more useful in collections.

```java
ArrayList<Animal> animals =
    new ArrayList<>();
```

We can store different kinds of animals together.

---

# Example

```java
ArrayList<Animal> animals =
    new ArrayList<>();

animals.add(new Cat());
animals.add(new Dog());
animals.add(new Bird());
```

All objects share the same superclass.

---

# Why This Matters

Imagine a zoo application.

Without polymorphism:

```java
ArrayList<Cat>
ArrayList<Dog>
ArrayList<Bird>
```

With polymorphism:

```java
ArrayList<Animal>
```

Much simpler.

---

# Generic Programming

A superclass reference can represent many subclasses.

```java
Animal animal;
```

Can refer to:

```java
new Animal()
new Cat()
new Dog()
new Bird()
```

The code becomes more flexible.

---

# Why Can One ArrayList Store Many Animal Types?

Consider:

```java
ArrayList<Animal> animals =
    new ArrayList<>();
```

This list can store:

```java
animals.add(new Cat());
animals.add(new Dog());
animals.add(new Bird());
```

At first this may seem strange because arrays and ArrayLists are designed to store a single type.

---

# The Key: A Common Superclass

<!-- column -->
Remember:

```text
Animal
   ↑
 Cat

Animal
   ↑
 Dog

Animal
   ↑
 Bird
```

<!-- column -->
Although these are different objects, they all inherit from:

```java
Animal
```

From Java's perspective, every element can be stored as an `Animal`.

---

# What Is Actually Stored?

```java
ArrayList<Animal> animals =
    new ArrayList<>();
```

The list stores:

```java
Animal references
```

Examples:

```java
Animal a1 = new Cat();
Animal a2 = new Dog();
Animal a3 = new Bird();
```

These assignments are legal because each subclass object is also an Animal.

ArrayLists use this same idea internally.

---

# Inheritance Makes It Possible

Without inheritance:

```java
class Cat { }
class Dog { }
class Bird { }
```

Java would see three completely unrelated types.

With inheritance:

```java
class Cat extends Animal { }
class Dog extends Animal { }
class Bird extends Animal { }
```

all three can be treated as `Animal` objects.

Inheritance creates the relationship.

Polymorphism allows us to use that relationship.

---

# The Object Class Is the Ultimate Superclass

Every Java class ultimately extends:

```java
Object
```

Because of this:

```java
Object[] values = {
    "Hello",
    42,
    new Cat()
};
```

is legal.

All of these objects share a common superclass:

```java
Object
```

The Java type hierarchy is what makes this possible.

---


# The Object Class

Remember:

```java
Object
```

is the root class of Java.

Every class ultimately extends `Object`.

---

# Object References

Because every class extends Object:

```java
Object obj;
```

can refer to:

```java
new String("Hello")
new Integer(42)
new Cat()
new Dog()
```

An Object reference can point to any object.

---

# Example

```java
Object[] values = {
    "hello",
    42,
    3.14,
    new Cat()
};
```

All entries are stored as Object references.

---

# The `instanceof` Operator

Sometimes we want to determine an object's type.

Java provides:

```java
instanceof
```

---

# Basic Example

```java
Animal animal = new Cat();

System.out.println(
    animal instanceof Cat
);
```

Output:

```text
true
```

The object is actually a Cat.

---

# More Examples

```java
Animal animal = new Cat();
```

```java
animal instanceof Cat
```

Result:

```text
true
```

```java
animal instanceof Animal
```

Result:

```text
true
```

---

# Another Example

```java
Animal animal = new Dog();
```

```java
animal instanceof Cat
```

Result:

```text
false
```

The object is a Dog, not a Cat.

---

# Why Use `instanceof`?

Sometimes behavior depends on the object's actual type.

```java
if (animal instanceof Cat) {
    System.out.println("Found a cat!");
}
```

It allows type checking at runtime.

---

# Real-World Examples of Polymorphism

Java libraries use polymorphism heavily.

Examples:

```java
ArrayList
LinkedList
HashSet
TreeSet
```

Different objects can often be used through common interfaces or parent types.

---

# Polymorphism Is Everywhere

Examples you will encounter:

- Java collections
- Graphical user interfaces
- Game development
- Business applications
- Web applications

Polymorphism is one of the most important ideas in OOP.

---

# Why Learn Polymorphism?

Benefits:

- Less duplicated code
- More reusable code
- More flexible programs
- Easier maintenance
- Easier expansion of existing systems

Many Java libraries depend heavily on polymorphism.

---

# Summary

- Polymorphism means "many forms"
- A superclass reference can refer to subclass objects
- Inheritance makes polymorphism possible
- One method can work with many object types
- Arrays and collections often use polymorphism
- Every Java class ultimately extends Object
- Object references can refer to any object
- `instanceof` checks an object's type
- Polymorphism helps create flexible, reusable software