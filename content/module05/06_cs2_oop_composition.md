# Composition

---

# Objects Inside Other Objects

Objects can contain references to other objects.

```java
class Cat {
    private String name;
    private Food favoriteFood;
}

class Food {
    private String brand;
    private double cost;
}
```

This is called a composition and it is a **has-a relationship**.

---

# Object Relationships Example

```java
Food food = new Food("Purina", 12.99);

Cat cat = new Cat("Milo", food);
```

- Cat object exists
- Food object exists
- Cat stores a reference to Food

---

# Object Arrays with Nested Objects

```java
Cat[] cats = new Cat[2];

cats[0] = new Cat("Milo",
        new Food("Purina", 12.99));

cats[1] = new Cat("Luna",
        new Food("Friskies", 10.50));
```

A single program can contain:

- Arrays
- Objects
- Objects inside objects
