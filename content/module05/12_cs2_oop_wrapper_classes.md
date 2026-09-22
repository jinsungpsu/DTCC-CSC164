
# Wrapper Classes

Java provides object versions of primitive types.

---

# Primitive Types and Wrappers

| Primitive | Wrapper Class |
|---|---|
| byte | Byte |
| short | Short |
| int | Integer |
| long | Long |
| float | Float |
| double | Double |
| char | Character |
| boolean | Boolean |

---

# Why Do Wrapper Classes Exist?

Collections such as `ArrayList` store objects.

This is invalid:

```java
ArrayList<int> numbers;
```

This is valid:

```java
ArrayList<Integer> numbers;
```

Wrapper classes allow primitives to be treated as objects.

---

# Autoboxing and Unboxing

Java converts automatically.

```java
Integer num = 5;      // Autoboxing
int value = num;      // Unboxing
```

Java performs the conversion behind the scenes.

---

# Useful Wrapper Methods

```java
int num = Integer.parseInt("42");
```

```java
double d =
    Double.parseDouble("3.14");
```

Convert strings into primitive values.

---

# Integer Constants

```java
System.out.println(
    Integer.MAX_VALUE);

System.out.println(
    Integer.MIN_VALUE);
```

Output:

```text
2147483647
-2147483648
```

Useful for validation and boundary checks.

---

# Predict the Output

```java
Integer num = 25;

System.out.println(num + 5);
```

What is printed?

- A. 255
- B. 30
- C. Integer30
- D. Compilation Error

**Answer:** B. 30

---

# Summary

- Arrays of objects store object references
- Objects can contain other objects
- Instance members belong to objects
- Static members belong to classes
- `this` refers to the current object
- Objects can be passed to methods
- Wrapper classes provide object versions of primitives
- Autoboxing and unboxing simplify conversions