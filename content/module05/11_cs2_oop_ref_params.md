
# Passing Objects as Parameters

Objects can be sent to methods.

```java
public static void wash(Car car) {
    car.clean();
}
```

Call:

```java
wash(myCar);
```

---

# What Happens Behind the Scenes?

When an object is passed:

- A copy of the reference is passed
- No new object is created
- Both references point to the same object

```text
myCar ----\
           -> Car Object
car   ----/
```

---

# Benefits of Passing Objects

- Efficient
- Reusable methods
- Supports encapsulation
- Enables object collaboration

---
