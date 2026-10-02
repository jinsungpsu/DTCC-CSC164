

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

# Getter Naming Isn't Always get...

The usual getter pattern is:

```java
private String name;

public String getName()
{
    return name;
}
```

However, boolean values often use different names.

---

# Boolean Values

Examples:

<!-- column -->

```java
private boolean active;

public boolean isActive()
{
    return active;
}
```

<!-- column -->

```java
private boolean enrolled;

public boolean isEnrolled()
{
    return enrolled;
}
```

<!-- endcolumns -->

When a variable represents a true/false condition, getters often begin with:

- `is`
- `has`
- Sometimes `can`

These getter names read more naturally in code.

---

# Boolean Getters

Consider this class:

```java
private boolean fullTime;

public boolean isFullTime()
{
    return fullTime;
}
```
<!-- column -->

Using the getter:

```java
if (student.isFullTime())
k{
    System.out.println("Full-time student");
}
```

<!-- column -->

Or:

```java
private boolean honorsStudent;

public boolean isHonorsStudent()
{
    return honorsStudent;
}
```

---

# Readability

The method call reads almost like an English sentence:

```java
student.isHonorsStudent()
```

This is one reason Java programmers often prefer `is...` getters for boolean values.

---

# Another Common Pattern: has...

Sometimes a boolean field represents whether an object possesses something.

<!-- column -->

Example:

```java
private boolean parkingPermit;
k
public boolean hasParkingPermit()
{
    return parkingPermit;
}
```

<!-- column -->

Usage:

```java
if (student.hasParkingPermit())
{
    System.out.println("Allowed to park");
}
```

---

# Readability Summary

The getter does the same job as any other getter:

- Reads private data
- Returns a value
- Provides controlled access

The naming is different because it makes the code easier to read.

---

# Setters Still Follow the Normal Pattern

Even when getters use `is` or `has`, setters usually follow the standard naming convention.

Example:

```java
private boolean active;

public boolean isActive()
{
    return active;
}

public void setActive(boolean active)
{
    this.active = active;
}
```
---

# Set Method Unchanged

Notice:

```java
isActive()
```

and

```java
setActive(boolean active)
```

The getter changes, but the setter typically remains a `set...` method.

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