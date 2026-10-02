# Inheritance in Java

## Overview
- What inheritance is
- Superclasses and subclasses
- The "is-a" relationship
- Why inheritance is useful
- Using the `super` keyword
- Constructor chaining
- Method overriding
- The `Object` class
- Overriding `toString()`

---

# What Is Inheritance?

Inheritance allows one class to build upon another class.

Benefits:

- Reuse existing code
- Reduce duplication
- Create organized class hierarchies
- Extend existing functionality

A subclass inherits members from a superclass.

---

# Superclasses and Subclasses

A **superclass** is a class that other classes inherit from.

A **subclass** is a class that inherits from another class.

```java
class Animal {
    
}

class Cat extends Animal {
    
}
```

- `Animal` is the superclass
- `Cat` is the subclass

---

# Defining a Subclass

Use the `extends` keyword.

```java
class Animal {

}

class Cat extends Animal {

}
```

A subclass can:

- Inherit data fields
- Inherit methods
- Add new data fields
- Add new methods
- Override inherited methods

---

# Example: Inheriting Data

```java
class Animal {
    protected int age;
}

class Cat extends Animal {
    private String name;
}
```

A `Cat` object contains:

- `age` inherited from `Animal`
- `name` declared in `Cat`

Subclasses gain access to inherited members.

---

# Thinking in "Is-A" Relationships

Inheritance models an **is-a** relationship.

Examples:

- A cat is an animal
- A dog is an animal
- A savings account is a bank account
- A student employee is an employee

If the relationship is not "is-a", inheritance may not be appropriate.

---

# Cat or Animal?

Consider:

```java
class Animal {
    int age;
}

class Cat extends Animal {
    String name;
}
```

Facts:

- A cat is an animal
- Every cat has an age
- Cats can add additional data
- Not every animal is necessarily a cat

Inheritance is one-way.

---

# Inheritance Chains

Inheritance can span multiple levels.

```java
class Animal {

}

class Mammal extends Animal {

}

class Cat extends Mammal {

}
```

`Cat` inherits from `Mammal`.

`Mammal` inherits from `Animal`.

---

# Inheritance Chain Visualization

```text
Animal
   ↑
 Mammal
   ↑
   Cat
```

A `Cat` object inherits accessible members from:

- Mammal
- Animal

Inheritance accumulates up the chain.

---

# Why Use Inheritance?

Without inheritance:

```java
class Cat {
    int age;
}

class Dog {
    int age;
}

class Horse {
    int age;
}
```

The same code is repeated.

Inheritance allows common functionality to be written once.

---

# Common Functionality

```java
class Animal {
    protected int age;

    public void eat() {
        System.out.println("Eating...");
    }
}
```

```java
class Cat extends Animal {

}
```

```java
class Dog extends Animal {

}
```

Both classes automatically inherit `age` and `eat()`.

---

# The `super` Keyword

`super` refers to the superclass portion of the current object.

Common uses:

- Call a superclass constructor
- Call a superclass method
- Access a superclass field

Examples:

```java
super();
super.display();
super.age;
```

---

# Calling a Superclass Constructor

```java
class Animal {
    Animal() {
        System.out.println("Animal constructor");
    }
}

class Cat extends Animal {
    Cat() {
        super();
        System.out.println("Cat constructor");
    }
}
```

`super()` calls the superclass constructor.

---

# Constructor Execution Order

Suppose:

```java
Cat cat = new Cat();
```

Java executes:

1. Animal constructor
2. Cat constructor

Superclass constructors always run first.

This helps ensure inherited data is initialized properly.

---

# Implicit Constructor Chaining

```java
class Animal {
    Animal() {
        System.out.println("Animal");
    }
}

class Cat extends Animal {
    Cat() {
        System.out.println("Cat");
    }
}
```

Output:

```text
Animal
Cat
```

Even though `super()` is not written, Java inserts it automatically.

---

# Passing Data to a Superclass Constructor

```java
class Animal {
    Animal(int age) {
        this.age = age;
    }

    protected int age;
}
```

```java
class Cat extends Animal {
    Cat(int age) {
        super(age);
    }
}
```

Arguments can be passed to superclass constructors.

---

# Calling a Superclass Method

```java
class Animal {
    public void speak() {
        System.out.println("...");
    }
}
```

```java
super.speak();
```

Useful when a subclass wants to reuse behavior already defined in the superclass.

---

# Accessing a Superclass Variable

```java
class Animal {
    protected int age = 5;
}
```

```java
System.out.println(super.age);
```

`super` can access inherited fields when appropriate.

---

# Method Overriding

A subclass can replace inherited behavior.

```java
class Animal {
    public void speak() {
        System.out.println("...");
    }
}
```

```java
class Cat extends Animal {
    @Override
    public void speak() {
        System.out.println("Meow");
    }
}
```

---

# Rules for Overriding

When overriding:

- Same method name
- Same parameter list
- Same return type (or compatible return type)

Example:

```java
@Override
public String toString() {
    return "example";
}
```

The `@Override` annotation helps catch mistakes.

---

# Overriding vs Overloading

Overriding:

```java
class Cat extends Animal {
    @Override
    public void speak() {

    }
}
```

- Requires inheritance
- Same signature

Overloading:

```java
print();
print(String message);
```

- Different parameter list
- Inheritance not required

---

# The Object Class

The `Object` class is the root of Java's class hierarchy.

Every Java class ultimately extends:

```java
Object
```

Even if you never write:

```java
extends Object
```

it is still there.

---

# Object Class Hierarchy Example

```text
Object
   ↑
 Animal
   ↑
   Cat
```

Every `Cat` object is also:

- a Cat
- an Animal
- an Object

---

# Methods Inherited from Object

Some commonly inherited methods include:

```java
toString()
equals()
hashCode()
getClass()
```

Every Java object has access to these methods.

---

# What Is `toString()`?

`toString()` returns a string representation of an object.

Java automatically calls it in situations like:

```java
System.out.println(cat);
```

This makes `toString()` useful for debugging and displaying objects.

---

# Default `toString()` Behavior

Suppose:

```java
Cat cat = new Cat();
System.out.println(cat);
```

Output may look similar to:

```text
Cat@7adf9f5f
```

This default behavior comes from the Object class.

---

# Object Class `toString()`

The Object class defines:

```java
public String toString() {
    return getClass().getName()
        + "@"
        + Integer.toHexString(hashCode());
}
```

Most classes benefit from replacing this with more meaningful output.

---

# Overriding `toString()`

```java
class Cat extends Animal {

    private String name;

    @Override
    public String toString() {
        return "Cat named " + name +
               ", age " + age;
    }
}
```

---

# Improved Output

Without overriding:

```text
Cat@7adf9f5f
```

With overriding:

```text
Cat named Whiskers, age 3
```

The object becomes much easier to understand.

---

# Why Override `toString()`?

Benefits:

- Easier debugging
- More readable output
- Better logging
- Easier testing

Many classes override `toString()` for these reasons.

---

# Summary

- Inheritance allows classes to build upon other classes
- Subclasses inherit from superclasses
- Inheritance models an "is-a" relationship
- `super` accesses superclass functionality
- Constructors chain through the inheritance hierarchy
- Methods can be overridden in subclasses
- Every class ultimately extends `Object`
- `toString()` is commonly overridden to provide useful output