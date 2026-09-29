

# Setters and Getters

Since private fields cannot be accessed directly, we often provide special methods.
---

# Encapsulation

Encapsulation means:

> Hiding an object's internal data and controlling how that data is accessed.

A common pattern is:

```java
public class Student {
    private String name;
}
```

Why?

Because the object's data should not be modified freely by outside code.

Instead, the class decides how access should occur.

---

# Setter and Getter Syntax

<!-- column -->
### Getter

Returns a value.

```java
public String getName() {
    return name;
}
```

<!-- column -->
### Setter

Updates a value.

```java
public void setName(String name) {
    this.name = name;
}
```
<!-- endcolumns -->

Together, these methods provide controlled access to private data.

---

# Creating a Getter

Example:

```java
public class Student {
    private String name;

    public String getName() {
        return name;
    }
}
```

Usage:

```java
Student s = new Student();

System.out.println(s.getName());
```

### Purpose

Allows outside code to read private data safely.

---

# Creating a Setter

Example:

```java
public class Student {
    private String name;

    public void setName(String name) {
        this.name = name;
    }
}
```

Usage:

```java
Student s = new Student();
s.setName("Alex");
```

### Purpose

Allows outside code to modify private data safely.

---

# Why Not Make Everything Public?

<!-- column -->

Consider this class:

```java
public class Student {
    public double gpa;
}
```

<!-- column -->

Outside code can do anything:

```java
student.gpa = 100.0;
student.gpa = -15.0;
```

<!-- endcolumns -->

Both values are invalid.

Using a setter allows validation:

```java
public void setGpa(double gpa) {
    if(gpa >= 0.0 && gpa <= 4.0) {
        this.gpa = gpa;
    }
}
```

### Benefit
> The class protects its own data.

---

# Example: Getter and Setter Together

```java
public class Student {

    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}
```

Usage:

```java
Student s = new Student();

s.setName("Alex");

System.out.println(s.getName());
```

Output:

```text
Alex
```

---

# Complete Encapsulation Example

```java
public class BankAccount {
    private double balance;

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {

        if(amount > 0) {
            balance += amount;
        }
    }
}
```

<!-- column -->

Usage:

```java
BankAccount account = new BankAccount();
account.deposit(100);
System.out.println(account.getBalance());
```

<!-- column -->

Output:

```text
100.0
```

<!-- endcolumns -->

### Important

The account balance cannot be changed directly.

All changes must go through the class's methods.

---

# Setters/Getters Summary

Setters and getters are essential for **encapsulation** and **controlled access to private data**.

<!-- column -->

### Getter

```java
public String getName()
```

- Reads data
- Returns a value
- Provides controlled access

<!-- column -->

### Setter

```java
public void setName(String name)
```

- Updates data
- Can validate input
- Protects object integrity

---

# Setters/Getters Summary

### Common Java Pattern

```java
private String name;

public String getName() {
    return name;
}

public void setName(String name) {
    this.name = name;
}
```

### Key Takeaway

Keep data `private` and expose it through well-designed methods whenever access is needed.