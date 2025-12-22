# Python Functions — Basics & Types

## What is a Function?
    A function is a **block of reusable code**
    It performs a specific task
    Helps reduce code repetition

---
    def function_name():
        pass
---

## Function Syntax
    def function_name(parameters):
        # function body
        return value

## Types of Functions

### 1. Built-in Functions

    Functions already provided by Python

        Examples:
            print("Hello")
            len([1, 2, 3])
            type(10)
            range(5)

### 2. User-Defined Functions

    Functions created by the programmer

    def greet():
        print("Hello World")

#### Calling the function:

    greet()

## Function with Parameters

    def add(a, b):
        return a + b

    add(2, 3)

### Default Parameters

    Parameters that have default values

    def greet(name="User"):
        print("Hello", name)

    greet()
    greet("Man")

## The print() Function (In Detail)

### Syntax

    print(*objects, sep=' ', end='\n')

### sep Parameter

    Used to separate multiple values
    Default value is space " "

    print(1, 2, 3)
    print(1, 2, 3, sep=",")
    print(1, 2, 3, sep="-")

### end Parameter

    Used to decide what prints at the end
    Default value is new line (\n)

    print("Hello", end=" ")
    print("World")

    print("A", end="-")
    print("B")

### Return Statement
    Sends value back from function


    def square(x):
        return x * x

    result = square(4)

## Key Points to Remember

    * Functions make code reusable

    * Built-in vs User-defined

    * Default parameters prevent errors

    * print() uses sep and end for formatting
