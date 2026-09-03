# Java Data Types and Operations

---

<div style="font-size:0.6em;">

# Java Data Types

| Type | Used For | Example |
|--------|----------|---------|
| `byte` | Small integers | `127` |
| `short` | Medium integers | `32000` |
| `int` | Regular integers | `100` |
| `long` | Large integers | `123456789L` |
| `float` | Decimal numbers | `19.99F` |
| `double` | Precise decimal numbers | `3.14159` |
| `char` | One character | `'A'` |
| `boolean` | True/False values | `true` |
| `String` | Text | `"Hello"` |

<!-- footer -->

https*//*ww.w3schools.com/java/java_data_ty*es.asp
</div>

---
<div style="font-size:0.6em;">

# Java Primitive Type Ranges

| Type | Minimum Value | Maximum Value |
|--------|--------|--------|
| `byte` | -128 | 127 |
| `short` | -32,768 | 32,767 |
| `int` | -2,147,483,648 | 2,147,483,647 |
| `long` | -9,223,372,036,854,775,808 | 9,223,372,036,854,775,807 |
| `float` | ±1.4 × 10^-45 | ±3.4 × 10^38 |
| `double` | ±4.9 × 10^-324 | ±1.8 × 10^308 |
| `char` | 0 (`'\u0000'`) | 65,535 (`'\uffff'`) |
| `boolean` | `false` | `true` |

</div>
---

# String

- Slightly different from the primitive data types.
- `String` is actually a class.
- We'll discuss classes in more detail later.

---

# Defining Variables

- Same as C++

```java
int age = 20;
double gpa = 3.5;
char grade = 'A';
String name = "Alex";
```

---

# Numeric Operators
- Addition (`+`)
- Subtraction (`-`) 
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)

---

# Augmented Operators

- Each numeric operator has a corresponding shorthand assignment operator.

```java
+=
-=
*=
/=
%=
```

Example:

```java
count += 1;
total *= 2;
```

---

# Literals vs Variables

- A literal is a value written directly into source code.
- A variable stores a value in memory RAM.

Examples of literals:

```java
1
1.5
'A'
"hello"
```

Example using variables:

```java
int x = 1; 
// in this case, 
// 1 is a literal, 
// x is a variable
```

---

# Numeric Literals

* Numeric literals can include suff*xes to specify their type.

```java
1.23L   // long
1.23F   // float
1.23D   // double
```


## Scientific Notation

```java
1e3
```

Equivalent to:

```text
1 × 10^3 or 1000
```

---

<div style="font-size:0.7em;">

# Java Operator Precedence


| Precedence | Operators | Description |
|------------|------------|-------------|
| Highest | `()` `[]` `.` | Parentheses, array access, member access |
| 2 | `++` `--` `+` `-` `!` | Unary operators |
| 3 | `*` `/` `%` | Multiplication, Division, Modulus |
| 4 | `+` `-` | Addition, Subtraction |
| 5 | `<` `<=` `>` `>=` | Relational operators |
| 6 | `==` `!=` | Equality operators |
| 7 | `&&` | Logical AND |
| 8 | `||` | Logical OR |
| 9 | `=` `+=` `-=` `*=` `/=` `%=` | Assignment operators |


<!-- footer -->
https://www.programiz.com/java-programming/operator-precedence

</div>

---

# Operator Precedence

### Example

```java
int result = 2 + 3 * 4;
```

Evaluates as:

```java
int result = 2 + 12;
int result = 14;
```

Because `*` has higher precedence than `+`.

---

# Remember PEMDAS

1. Parentheses `()`
2. Multiplication, Division, Modulus `* / %`
3. Addition, Subtraction `+ -`
4. Comparisons `< > <= >=`
5. Equality `== !=`
6. Logical AND `&&`
7. Logical OR `||`
8. Assignment `=`

### Example

```java
boolean answer =
    (5 + 2 > 3) && (10 % 2 == 0);
```

- `5 + 2` evaluated first
- `10 % 2` evaluated next
- Comparisons evaluated
- `&&` evaluated last

---

# Modulus review
- Simply the remainder part of division
- Uses of %
    - even, odd
    - “wrapping around”
        - something that happens every n-th time in a loop

---

# Increment / Decrement
- preincrement/predecrement
    - ++var, --var
    - Change the value and use the new value in the statement
- postincrement/postdecrement
    - var++, var--
    - Use the value and use the old value in the statement

---

# Java Numeric Type Promotion & Demotion

<!-- column -->
### Promotion ↑ 
- Automatic Promotion

<!-- column -->
double

⬆

float

⬆

long

⬆

int

⬆

short

⬆

byte

---
# Java Numeric Type Promotion & Demotion

<!-- column -->
### Demotion ↓ 
- Explicit Demotion

<!-- column -->
double

⬇ cast

float

⬇ cast

long

⬇ cast

int

⬇ cast

short

⬇ cast

byte

---
# Java Numeric Type Promotion & Demotion Examples
```java
byte b = 100;
int n = b;          // promotion

double d = 3.14;
int x = (int)d;     // demotion
```
---

# Type casting

```java
int smallNum = 5;

System.out.print(smallNum / 2); 
// will print 2

System.out.print((double)smallNum / 2); 
// will print 2.5
```
---

# Analogy

- Overflow *can* occur when converting from a bigger type to a smaller type - so it must be done explicitly.

<!-- column -->

```java
double bigNumber = 1234.5678;

int smallNumber = (int) bigNumber; 
// this works

int smallNumber = bigNumber; 
// this is an error
```

<!-- column -->

![Overflow illustration pouring large amount of water from a 5 gallon bucket into small 8 oz cup and water overflowing](images/overflow.png)

---

# String concatenation for output
```java
int students = 5;
System.out.print("The number of students is " + students);
```
- What’s actually happening?
- The students variable is being converted to a string, then “added” to the rest of the string

---

# Print examples of conversion
```java
System.out.print(1 + 1);
// this outputs 2
System.out.print("The sum is " + 1 + 1);
// the output is The sum is 11
// because the 1’s are being treated as strings
System.out.print("The sum is " + (1+1));
// the output is The sum is 2
// because the (1+1) makes the operator precedence
// add the 1+1 as integers first,
// THEN gets converted to a string
// before being added to the "The sum is " string
```
---
