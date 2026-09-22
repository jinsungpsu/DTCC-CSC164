
# Constructor Chaining

One constructor can call another.

```java
public Car() {
    this("Unknown");
}

public Car(String model) {
    this.model = model;
}
```

Benefits:

- Avoid duplicate code
- Easier maintenance

---

# Quick Check

1. What does `this` refer to?
2. Can static methods access instance variables directly?
3. What is constructor chaining?
4. Does every object have its own instance variables?

---
