
# Using this

`this` refers to the current object.

```java
public void drive() {
    this.accelerate();
}
```

Equivalent to:

```java
accelerate();
```

---

# Using this with Variables

```java
public Car(String model) {
    this.model = model;
}
```

- Left side: instance variable
- Right side: parameter

`this` removes ambiguity.

---

# This in Static Contexts

Invalid:

```java
public static void test() {
    this.drive();
}
```

Why?

- Static methods belong to the class
- No current object exists
- Therefore `this` cannot be used

---
