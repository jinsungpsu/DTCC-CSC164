# Debugging I

Break points, Step Over

---

# Have you ever done this?

- There’s a better way!!

![debugging-example](images/debugging-example.png)

---

# Breakpoints

![breakpoints](images/breakpoints.png)

---

# Debug Mode

![debug-mode](images/debug-mode.png)

---

# Breakpoints

- Program stop BEFORE the instruction at the breakpoint is executed
- You can add/remove breakpoints while in debug mode
- If you make any changes to the source code, you must recompile/restart debug mode

---

# Variable values

- Displayed inline in the source code
- Displayed in the “Threads & Variables” section on the bottom
- Console output is in a separate tab

![threads-and-variables](images/threads-and-variables.png)

---

# Debug Mode Controls

![debug-controls](images/debug-controls.png)

- Step over
- Executes current instruction and stops before executing the next instruction

---

# Debug Mode Controls

![debug-controls](images/debug-controls.png)

- Re-run
- Re-compile and start debug process again

---

# Debug Mode Controls

![debug-controls](images/debug-controls.png)

- Resume
- Continue program until it encounters next breakpoint

---

# Debugging II

Step In/Out, Stack Frames

---

# Methods

- Stepping in and out in debug mode has everything to do with the call stack
- The call stack organizes each method running in the program

---

# The Call Stack

[Diagram explaining the call stack and function calls]

![call-stack-diagram](images/call-stack-diagram.png)

---

# Example

![debugging-example-1](images/debugging-example-1.png)

![debugging-example-2](images/debugging-example-2.png)

---

# Stack Frames

![stack-frame-1](images/stack-frame-1.png)

![stack-frame-2](images/stack-frame-2.png)

![stack-frame-3](images/stack-frame-3.png)

---

# Debug Mode Controls

![debug-controls](images/debug-controls.png)

- Step into
- Will go into any methods in the next instruction
- If there are multiple methods, debugger will prompt and ask which method to go into
- Behaves the same as step over if there are no methods

---

# Debug Mode Controls

![debug-controls](images/debug-controls.png)

- Step out
- Will finish running current method and step out of current method
