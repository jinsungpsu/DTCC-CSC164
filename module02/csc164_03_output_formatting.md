

# Output formatting
- print
- regular output
- println
- output followed by printing a \n (new line)
- printf
- formatted output

---

# Formatting Decimal Numbers
- // declaring double
- double a = 3.14159265359;
- // Printing Double Value with
- // different Formatting
- System.out.printf("%f\n", a);
- System.out.printf("%5.3f\n", a);
- System.out.printf("%5.2f\n", a);
- 3.141593
- 3.142
- 3.14
- https://www.geeksforgeeks.org/formatted-output-in-java/
- Code:
- Output:

---

# Format specifiers
- %s: String
- %d: Decimal integer
- %f: Floating-point number
- %c: Character
- %b: Boolean (true/false)
- %n: Newline character

---

# Numeric
- %x: Hexadecimal integer (lowercase)
- %X: Hexadecimal integer (uppercase)
- %o: Octal integer
- %e: Exponential floating-point number (lowercase 'e')
- %E: Exponential floating-point number (uppercase 'E')
- %g: General format for floating-point (chooses between %f or %e)
- %G: General format for floating-point (chooses between %f or %E)

---

# Width and Precision
- %5d: Integer with minimum width of 5
- %.2f: Floating-point with 2 decimal places
- %10.2f: Floating-point with minimum width of 10 and 2 decimal places
- %-10s: Left-aligned string with minimum width of 10

---

# Example
- Can be used to simplify output:
- System.out.printf(“Hi my name is %s”, name);
- instead of System.out.printf(“Hi my name is “ + name);
- Multiple variables
- System.out.printf(“Hi my name is %s %s”, firstName, lastName);
- System.out.printf(“Hi my name is %s %s and my age is %d and my grade is %.2f”, firstName, lastName, age, grade);

---