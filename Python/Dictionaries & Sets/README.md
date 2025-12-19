---

# 📘 Python Dictionary & Sets – Complete Basics

---

## 🔹 Dictionary in Python

### 📌 What is a Dictionary?
A *dictionary* is a collection of *key–value pairs*.  
- Keys are *unique*
- Values can be anything
- It is *mutable* (changeable)

Think of it like a real dictionary:
> word → meaning

---

### 🧾 Dictionary Syntax
```python
student = {
    "name": "Man",
    "age": 18,
    "course": "CS"
}


---

🔍 Accessing Values

print(student["name"])

Using get() (safe method):

print(student.get("age"))


---

✏ Changing Values

student["age"] = 19


---

➕ Adding New Key–Value Pairs

student["college"] = "UPES"


---

📏 Length of Dictionary

len(student)


---

🔁 Dictionary Methods

🔹 keys()

Returns all keys

student.keys()

🔹 values()

Returns all values

student.values()

🔹 items()

Returns key–value pairs

student.items()

🔹 update()

Updates or adds values

student.update({"age": 20, "city": "Dehradun"})


---

🪜 Nested Dictionary

Dictionary inside another dictionary

students = {
    "student1": {
        "name": "Man",
        "age": 18
    },
    "student2": {
        "name": "Aman",
        "age": 19
    }
}

Access nested values:

print(students["student1"]["name"])


---

🔹 Set in Python

📌 What is a Set?

A set is an unordered collection of unique elements.

⚠ No duplicates
⚠ No indexing
✅ Mutable
❌ Elements must be immutable


---

🧾 Set Syntax

numbers = {1, 2, 3, 4}

Empty set:

s = set()

(Not {} — that creates a dictionary)


---

➕ add()

Adds an element

numbers.add(5)


---

➖ remove()

Removes an element (error if not present)

numbers.remove(2)


---

❌ discard()

Removes element (no error if missing)

numbers.discard(10)


---

🧹 clear()

Removes all elements

numbers.clear()


---

🎯 pop()

Removes a random element

numbers.pop()


---

🔗 Union

Combines two sets

a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)


---

✂ Intersection

Common elements

a.intersection(b)


---

🔁 Mutable vs Immutable (Important)

✅ Set itself is mutable

numbers.add(10)

❌ Elements inside a set must be immutable

Allowed:

{1, 2, "hello", (1, 2)}

Not allowed:

{1, 2, [3, 4]}  # ❌ list is mutable


---

🔐 Hashable Values

Set elements must be hashable
Means:

Value cannot change

Has a fixed hash value


✅ Hashable:

int

float

string

tuple


❌ Not Hashable:

list

set

dictionary



---

✅ Quick Comparison

Feature	Dictionary	Set

Stores	Key–Value	Values only
Duplicate	Keys ❌	❌
Mutable	✅	✅
Indexed	❌	❌



---
