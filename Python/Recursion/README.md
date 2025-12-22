# 🔁 Recursion in Python

## 📌 What is Recursion?

### Recursion is when a function calls itself to solve a problem by breaking it into smaller sub-problems.
    
    > Simple idea:

    Big problem → smaller version of same problem → repeat → stop



## 🤔 Why do we use Recursion?

### Use recursion when:

        * A problem naturally breaks into similar subproblems

        * Code becomes cleaner & shorter

        * Problems involve:

        * Factorial

        * Fibonacci

        * Tree / Graph traversal

        * Divide & conquer logic



## ⚠️ But be real:

    Recursion uses more memory

    Too much recursion = stack overflow

    So: use it smartly, not blindly



## 🧱 Two Important Parts of Recursion

### Every recursive function must have:

    * 1️⃣ Base Case

    👉 Condition where recursion stops

    * 2️⃣ Recursive Case

        👉 Function calls itself with a smaller input

        Without base case = ❌ infinite recursion



## 🧩 Syntax of Recursive Function (General Form)

    def function_name(parameters):
        if base_condition:
            return result
        else:
            return function_name(smaller_input)



## 🧠 Example: Simple Recursion (Countdown)

    def countdown(n):
        if n == 0:          # base case
            return
        print(n)
        countdown(n - 1)    # recursive call


### How it works:

        Calls itself with n-1

        Stops when n == 0



## 📚 What is Call Stack? (VERY IMPORTANT)

### Call Stack = Memory stack

    Python keeps track of function calls using a stack (LIFO – Last In, First Out).

    Each function call:

    Gets its own space in memory

    Waits until the function it called finishes




## 🧠 Call Stack Example (Normal Function)

    def a():
        b()

    def b():
        c()

    def c():
        print("Done")


### Stack flow:

        c() → finishes
        b() → finishes
        a() → finishes



## 🔥 Call Stack in Recursion (Factorial)

### 📌 Factorial Formula

    n! = n × (n-1)!


---

### 🧮 Recursive Factorial Code

    def factorial(n):
        if n == 1:          # base case
            return 1
        return n * factorial(n - 1)




## 🧠 Call Stack Trace: factorial(5)

### Step-by-step Calls

    factorial(5)
    = 5 * factorial(4)

    factorial(4)
    = 4 * factorial(3)

    factorial(3)
    = 3 * factorial(2)

    factorial(2)
    = 2 * factorial(1)

    factorial(1)
    = 1   ← base case reached




## 📥 Stack Filling Phase (Going Down)

    factorial(5)
    factorial(4)
    factorial(3)
    factorial(2)
    factorial(1)

### Each call waits for the next one.


---

## 📤 Stack Unwinding Phase (Returning Back)

    factorial(1) → returns 1
    factorial(2) → 2 * 1 = 2
    factorial(3) → 3 * 2 = 6
    factorial(4) → 4 * 6 = 24
    factorial(5) → 5 * 24 = 120

### 🎯 Final Answer = 120


---

## ⚠️ Important Notes (Exam + Interview)

    Every recursive call uses stack memory

    Deep recursion → RecursionError

    Python default recursion limit ≈ 1000



---

## 🔄 Recursion vs Loop (Quick Truth)

    Feature	    Recursion	         Loop

    Code	    Cleaner	             Faster
    Memory	    High	             Low
    Stack	    Uses call_stack      No call stack
    Risk	    Stack overflow	     Safer


### 👉 Use loop when possible
### 👉 Use recursion when logic is naturally recursive


---

## ✅ When to Use Recursion (Rule of Thumb)

    Use recursion only if:

    Problem repeats itself

    Smaller version of same problem exists

    Clear base case is present



---