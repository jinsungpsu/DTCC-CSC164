
# Visibility Modifiers

Visibility modifiers control **who can access fields, methods, and constructors**.

They are an important part of **encapsulation**, which helps protect an object's data from unwanted changes.

Java provides four access levels:

- `public`
- `private`
- `protected`
- `default` (package-private)

Think of visibility modifiers as determining **who is allowed through the door.**

---

# Why Visibility Matters

Without access control, any code could modify an object's data.

<!-- column -->

```java
public class BankAccount {
    double balance;
}
```

<!-- column -->

Anywhere in the program:

```java
BankAccount account = new BankAccount();
account.balance = -5000;
```

<!-- endcolumns -->

### Problem

The object's data can be changed in ways the programmer may not want.

Visibility modifiers help protect object state.

---

# Public Members

A `public` member can be accessed from anywhere.

<!-- column -->

```java
public class Student {
    public String name;
}
```

<!-- column -->

Usage:

```java
Student s = new Student();
s.name = "Alex";
System.out.println(s.name);
```

<!-- endcolumns -->

### Characteristics

- Accessible from any class
- No restrictions on access
- Often used for methods
- Less commonly used for fields

### Think Of It As

A public website that anyone can visit.

---

# Private Members

A `private` member can only be accessed within the same class.

```java
public class Student {
    private String name;
}
```

<!-- column -->

This is allowed:

```java
public class Student {
    private String name;

    void printName() {
        System.out.println(name);
    }
}
```

<!-- column -->

This is NOT allowed:

```java
Student s = new Student();
s.name = "Alex";      // Compile-time error
```

---

# Private Members

### Characteristics

- Most restrictive access level
- Hides implementation details
- Protects object data
- Commonly used for fields

### Think Of It As

Your password. Only you should have direct access.

---

# Protected Members

A `protected` member is accessible:

- Within the same package
- By subclasses, even in different packages

> More on this later!

<!--
```java
public class Animal {

    protected String name;

}
```

Subclass:

```java
public class Dog extends Animal {

    void display() {
        System.out.println(name);
    }

}
```

### Characteristics

- Useful when inheritance is involved
- Gives subclasses access to important data
- More restrictive than `public`
- Less restrictive than `private`

### Think Of It As

A family key that relatives can use but strangers cannot.
-->

---

# Default Access (Package-Private)

If no access modifier is specified, Java uses **default access**.

```java
public class Student {
    String name;
}
```

Notice there is no modifier before `String`.

---

# Default Access

<!-- column -->

### Accessible By

- Classes in the same package

<!-- column -->

### Not Accessible By

- Classes in different packages

<!-- endcolumns -->

Example:

```java
class Course {
    void display() {
        // Can access package-private members
    }
}
```

### Think Of It As

A classroom where only students enrolled in that course may enter.

---

# Visibility Comparison

Imagine a school building:

| Modifier | Who Has Access? |
|----------|----------------|
| public | Everyone |
| protected | Same package + subclasses |
| default | Same package only |
| private | Same class only |

---

### Most Open

```text
public
```

↓

```text
protected
```

↓

```text
default
```

↓

```text
private
```

### Most Restricted

---

# Summary

| Modifier | Can Be Accessed By | Usage Example |
|----------|-------------------|---------------|
| public | Anywhere | `public void display()` |
| private | Only within the same class | `private String model` |
| protected | Same package and subclasses | `protected void display()` |
| default | Only within the same package | `void display()` |

### General Rule

- Fields are usually `private`
- Methods are often `public`
- `protected` is common with inheritance
- `default` is used when access should stay within a package
