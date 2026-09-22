
# Classes We've Already Used

Many Java classes are objects.

- `Scanner`
- `String`
- `Random`
- `ArrayList`
- `Math`

We have been using OOP since the beginning of the course.

---

# Revisiting Methods

A **method** belongs to a class or object.

Examples:

```java
String name = "Alex";

name.length();
name.toUpperCase();
```

Methods define behavior associated with objects.

---

# Scanner Example

```java
Scanner input = new Scanner(System.in);

int num = input.nextInt();
```

- `input` is an object
- `nextInt()` is a method
- The method belongs to the Scanner object

---

# String Example

```java
String name1 = "Alex";
String name2 = new String("Alex");
```

Both create String objects.

Common methods:

```java
name1.length();
name1.toUpperCase();
```

---

# Character Input Example

```java
char letter =
        keyboard.next().charAt(0);
```

Explanation:

1. Read a String
2. Access index 0
3. Store the character

---
