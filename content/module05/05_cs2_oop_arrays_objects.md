# Arrays of Objects

**Definition:** An array of objects is a collection of references to objects of the same class.

- Stores many related objects in one structure
- Each element holds a reference to an object
- All objects must be the same type
- Similar to arrays of primitives, but stores references instead of values

---

# Why Use Arrays of Objects?

Imagine storing information for multiple cars:

```java
String car1 = "Ford";
String car2 = "BMW";
String car3 = "Audi";
```

Problems:

- Hard to manage many variables
- Difficult to loop through data
- Does not take advantage of OOP

Arrays of objects solve these problems.

---

# Declaring an Array of Objects

```java
Car[] cars = new Car[5];
```

- Creates an array with 5 elements
- Each element can reference a `Car` object
- No `Car` objects exist yet
- All elements currently contain `null`

---

# Visualizing the Array

```java
Car[] cars = new Car[3];
```

| Index | Value |
|---------|---------|
| 0 | null |
| 1 | null |
| 2 | null |

The array exists, but the objects have not been created yet.

---

# Instantiating Objects in an Array

Two steps are required:

1. Create the array
2. Create each object

```java
Car[] cars = new Car[3];

cars[0] = new Car("Ford");
cars[1] = new Car("BMW");
cars[2] = new Car("Audi");
```

---

# Initializing an Array of Objects

Java allows initialization in one statement:

```java
Car[] cars = {
    new Car("Tesla"),
    new Car("BMW"),
    new Car("Audi")
};
```

- Compact syntax
- Useful when values are known ahead of time

---

# Processing Arrays of Objects

Loop through each object just like any other array.

```java
for (Car car : cars) {
    System.out.println(car.getModel());
}
```

Output:

```text
Tesla
BMW
Audi
```

---

# Passing Arrays of Objects to Methods

```java
printCarModels(cars);
```

Method:

```java
public static void printCarModels(Car[] cars) {
    for (Car car : cars) {
        System.out.println(car.getModel());
    }
}
```

- Arrays can be passed as parameters
- The method can access every object in the array

---

# Predict the Output

```java
Car[] cars = {
    new Car("Tesla"),
    new Car("BMW")
};

System.out.println(cars[1].getModel());
```

What is printed?

- A. Tesla
- B. BMW
- C. null
- D. Compilation Error
> <p class="fragment"><strong>Answer:</strong> B. BMW</p>

---
