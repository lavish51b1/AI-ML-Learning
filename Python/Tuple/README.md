# Python Tuples — Basics & Methods

## What is a Tuple?

* A tuple is a built-in data type in Python

* It stores an ordered sequence of values

* Tuples are immutable (cannot be changed after creation)


        tup = (1, 2, 3)


---

## Creating Tuples

* Normal Tuple

        tup = (10, 20, 30)

* Tuple Without Parentheses (Packing)

        tup = 1, 2, 3

* Single Value Tuple (Comma is Mandatory)

        tup = (5)

        ❌ This is NOT a tuple

        tup = (5,)

        This ia a tuple


---

## What is Allowed in Tuples?

* Numbers

* Strings

* Boolean values

* Mixed data types

* Nested tuples


        tup = (1, "apple", True, (2, 3))


---

## What is NOT Allowed in Tuples?

* Modifying elements

* Adding or removing items


* Not allowed
        tup[0] = 100


---

* Accessing Tuple Elements (Indexing)

        tup = (10, 20, 30, 40)
        tup[0]
        tup[2]
        tup[-1]


---

* Tuple Slicing

        tup[0:2]
        tup[1:]
        tup[:3]
        tup[-3:-1]


---

## Tuple Methods

* index() — Find Position of Element

        tup.index(20)

* count() — Count Occurrences

        tup.count(10)


---

### Key Points to Remember

* Tuples are immutable

* Faster than lists

* Safe for fixed data

* Comma makes the tuple, not parentheses
