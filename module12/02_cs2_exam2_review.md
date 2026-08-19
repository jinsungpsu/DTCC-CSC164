# CSC164 Exam 2 Review

---

# Exam Instructions/Policies

This assessment is closed resource (no notes, powerpoint, textbook, internet, etc.). If you open another internet browser or tab, it will be considered cheating. You may not leave the testing area for any reason. If you have any extenuating circumstances that may require any exceptions, please let the instructor/proctor know as soon as you can.

This assessment MUST be completed using D2L on a lab computer during the scheduled time and location; you may not use your own device or take this assessment at a different location without prior approval.

---

# Format

- Entirely in D2L
- Multi-select
- Multiple choice
- True/false
- Matching
- Written Response (short answer)

---

# OOP Concepts

- What is OOP?
- What is encapsulation? Abstraction?
- Classes vs Objects
- What is the difference between the two?
- Reference types/classes vs primitive types
- As simple as a name that starts with a upper or lower case letter!
- For example - int is a primitive, String and Integer are classes/reference types
- Naming conventions

---

# Objects and Access

- Dot notation to access object instance data/methods
- Private data and using setters and getters
- why?
- syntax of each
- this keyword

---

# Constructors

- Syntax
- return type
- default constructors
- Overloaded constructors
- Overloaded methods

---

# Static vs Instance Variables and Methods

- What is each - definition

---

# Visibility Modifiers

- Public, private
- protected and default visibility not emphasized
- we’re not using packages in this course

---

# Reference Variables

- reference variable
- null value
- Can only be assigned to reference variables
- special meaning - NOWHERE/NOTHING, NOT a memory address
- Deep copy
- When dealing with reference variables, = doesn't do the same thing as with primitive types

---

# Java Classes

- String
- Scanner

---

# Array of Objects

- array of objects (more accurately - array of reference variables)

---

# Practice

Write a program that…

- Defines a BankAccount class with a name and balance.
- Create a program that prompts the user whether they want to open up a bank account and whether they want to make a deposit into that account.
- A bank account cannot be created without a name, and the default balance value is 0.
- Try to do this without using resources!!!

---

# ChatGPT review possible prompt

- give me a practice problem about creating classes, using constructors, setters, getters, and arrays of objects. difficulty level should be for a beginner with oop

---

# Problem: Create a Class for a Library System

You are tasked with creating a basic library system to manage books. In this system, you'll need to represent a book and be able to store multiple books in the library.

## Requirements

### Create a class Book

- Properties:
  - title (String)
  - author (String)
  - yearPublished (int)
  - isAvailable (boolean)
- Constructor initializes all properties.
- Create getter and setter methods for all properties.

---

# Create a class Library

- The class should have an array of Book objects (fixed size, e.g., 5).
- Methods:
  - addBook(Book book)
  - listBooks()
  - findBookByTitle(String title)
- Create a main class or method to test functionality:
  - Create a Library object.
  - Create Book objects and add them.
  - List all books.
  - Search for a book by title.

---

# Example Output

Library contains the following books:

1. Title: "Harry Potter", Author: "J.K. Rowling", Year: 1997, Available: true
2. Title: "The Hobbit", Author: "J.R.R. Tolkien", Year: 1937, Available: false

Searching for "Harry Potter":

Found book: Title: "Harry Potter", Author: "J.K. Rowling", Year: 1997, Available: true

Searching for "Moby Dick":

Book not found.
