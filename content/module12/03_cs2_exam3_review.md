# CSC164 Exam 3 Review

---

# Exam Instructions/Policies

This assessment is closed resource (no notes, powerpoint, textbook, internet, etc.). If you open another internet browser or tab, it will be considered cheating. You may not leave the testing area for any reason. If you have any extenuating circumstances that may require any exceptions, please let the instructor/proctor know as soon as you can.

This assessment MUST be completed using D2L on a lab computer during the scheduled time and location; you may not use your own device or take this assessment at a different location without prior approval.

---

# Exam Format and Review Priorities

- D2L; multiple choice, multi-select, true/false, and short written response
- Applied coding questions combine several topics

---

# Inheritance: Concepts to Study

- What a superclass and subclass are
- The purpose and benefits of inheritance: shared behavior, reuse, and maintainability
- The “is-a” relationship
- What a subclass inherits, and what it can add or customize
- Superclass private fields remain part of the object's state; subclasses use accessible methods to work with them
- The `extends` and `super` keywords
- Java classes have one direct superclass
- Understand superclass constructor chaining
- Use `super(arguments)` to initialize superclass state; if omitted, Java attempts an implicit `super()`

---

# Overriding and Overloading

- **Overriding:** a subclass replaces inherited method behavior using a matching method signature.
- **Overloading:** methods share a name but have different parameter lists.
- Know how to tell the two apart from a short code example.
- Know when `super` refers to superclass construction or behavior.
- `super.method(...)` calls superclass behavior; it does not select the subclass override.

---

# Review: Inheritance

### Which statements are true? Select all that apply.

- A subclass can override an inherited method.
- A Java class can extend multiple classes.
- Inheritance can reduce duplicated code.

<div class="fragment">

**Answers:** A subclass can override an inherited method; inheritance can reduce duplicated code.

</div>

<div class="fragment">

A Java class has one direct superclass.

</div>

---

# Review: Method Behavior

### Two methods have the same name but different parameter lists. Is this overriding or overloading?

<div class="fragment">

**Overloading.**

</div>

<div class="fragment">

Overriding requires a subclass method to match an inherited method's signature and provide different behavior.

</div>

---

# `Object` and `toString()`: Concepts to Study

- `Object` is the root superclass of Java classes.
- A class with no declared superclass implicitly extends `Object`.
- Trace indirect inheritance: `Object` → superclass → subclass; `String` also extends `Object`.
- Every object has a `toString()` method.
- Know why the default `toString()` result may not be meaningful to a user.
- The default result looks like `ClassName@hexHash`, rather than a description of the fields.
- Know the purpose of overriding `toString()` to describe an object's data.
- Printing an object can call its `toString()` method automatically.
- A subclass can build on superclass behavior without directly accessing private superclass fields.

---

# Writing `toString()`: Study Pattern

- Use `@Override` and the signature `public String toString()`.
- Return a string describing relevant fields; do not just print them.
- In a subclass, combine `super.toString()` with the subclass's own fields.

```java
@Override
public String toString() {
    return super.toString() + ", detail=" + detail;
}
```

This subclass pattern assumes the superclass already provides a useful `toString()`.

---

# Review: `Object` and `toString()`

### True or false: A class with no `extends` clause ultimately inherits from `Object`.

<div class="fragment">

**True.**

</div>

<div class="fragment">

### Why override `toString()`?
</div>

<div class="fragment">

To provide a useful text description of an object instead of relying on the default representation.

</div>

---

# Polymorphism: Concepts to Study

- What polymorphism means in object-oriented programming
- A superclass reference can refer to an object of a subclass
- The declared reference type controls which methods are available to call
- An overridden method's behavior depends on the object's actual type
- How polymorphism supports reusable and maintainable code
- Recognize valid assignments such as `Base item = new Child(...);` and `Object item = new Child(...);`
- Check local variable names too: redeclaring a name in the same scope prevents compilation

---

# Review: Polymorphism

### A superclass reference refers to a subclass object. Which implementation of an overridden method runs?

```java
class Animal {
    public String speak() { return "Animal sound"; }
}
class Cat extends Animal {
    @Override
    public String speak() { return "Meow"; }
}

// In main:
Animal pet = new Cat();
System.out.println(pet.speak()); // What is printed?
```

<div class="fragment">

**`Meow`** — the object's actual class is `Cat`, so `Cat.speak()` runs.

</div>

<div class="fragment">

The reference type still determines which methods can be called in the first place.

</div>

---

# `ArrayList` and Generics: Concepts to Study

The exam provides an `ArrayList` reference. Review how to:

- Declare a list with a generic type
- Append with `add(value)`; insert with `add(index, value)`; access with `get(index)`
- Replace with `set(index, value)`; insertion shifts items, replacement does not
- Use `size()` for the item count; indexes start at zero
- Use wrapper types such as `Integer`; autoboxing converts primitive values when adding them
- Store subclass objects in a list declared for their superclass
- `ArrayList<Object>` can hold different object types because they all share `Object`
- `isEmpty()` checks whether the list has no items

---

# Reading and Displaying a List

- Use `size()` and `get(i)` for a list, versus `length` and `[i]` for an array.
- Printing the list directly displays its contents using the collection's `toString()`, rather than `Object`'s default.
- Each element's `toString()` determines its text representation.

---

# Review: `ArrayList`

### Which list operation replaces an item at an existing index?

<div class="fragment">

**`set(... , ...)`**

</div>

<div class="fragment">

### What should a loop use as its stopping limit when visiting every list item?

</div>

<div class="fragment">

The list's current size; valid indexes range from zero to one less than the size.

```java
for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}
```

</div>

---

# Applying the Concepts

Be prepared to:

- Identify which statements or lines of code are valid
- Define a subclass with its own fields and behavior
- Initialize inherited data through constructor chaining
- Override `toString()` to describe an object
- Create a superclass-typed `ArrayList` containing superclass and subclass objects
- Display objects and use shared methods to calculate a value across the list
- Initialize an accumulator before a loop; add each object's getter result inside the loop
- Trace which methods actually run: a constructor that assigns a field does not automatically call its setter

Focus on how these ideas fit together; use the provided reference material for `ArrayList` syntax.

---

# Review: Putting It Together

### What makes a superclass-typed list polymorphic?

<div class="fragment">

It can hold objects of the superclass and its subclasses.

</div>

<div class="fragment">

### When displaying objects from that list, what controls each object's `toString()` behavior?

</div>

<div class="fragment">

The actual class of each object, if the class overrides `toString()`.

</div>

---

# Final Study Checklist

- Explain inheritance and its benefits.
- Distinguish constructor chaining, overriding, and overloading.
- Explain the role of `Object` and `toString()`.
- Describe polymorphism and identify reference type versus object type.
- Use `ArrayList` operations, indexes, and generic types.
- Explain how inheritance and polymorphism support working with a group of related objects.
- Practice short code-reading and written-response questions on each topic.
