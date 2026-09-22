
# Instance Variables

**Instance variables belong to objects.**

```java
class Car {
    private String model;
    private int year;
}
```

- Declared inside a class
- Outside methods
- Every object gets its own copy

---

# Instance Variable Example

```java
Car car1 = new Car("Ford");
Car car2 = new Car("Tesla");
```

Memory concept:

```text
car1.model -> Ford
car2.model -> Tesla
```

Each object stores its own data.

---

# Instance Methods

Instance methods operate on object data.

```java
public void accelerate() {
    speed++;
}
```

Called using an object:

```java
car.accelerate();
```

---

# Static Variables

**Static variables belong to the class, not objects.**

```java
class Car {
    public static int count = 0;
}
```

There is only one shared copy.

---

# Why Use Static Variables?

Examples:

- Count objects created
- Store application settings
- Shared constants
- Information common to all objects

```java
Car.count++;
```

---

# Static Variable Example

```java
class Car {
    static int count = 0;

    public Car() {
        count++;
    }
}
```

```java
new Car();
new Car();

System.out.println(Car.count);
```

Output:

```text
2
```

---

# Static Methods

Static methods belong to the class.

```java
public static void sayHello() {
    System.out.println("Hello");
}
```

Called using:

```java
MyClass.sayHello();
```

---

# Static vs Instance Methods

| Static Method | Instance Method |
|---|---|
| Belongs to class | Belongs to object |
| No object required | Object required |
| Cannot directly access instance variables | Can access instance variables |
| Called with class name | Called with object reference |

---
