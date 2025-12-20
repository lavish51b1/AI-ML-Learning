# 🔁 Loops in Python

Loops are used when you want to *repeat a block of code* again and again until a condition is met.  
Python mainly uses *two types of loops*:

- while loop  
- for loop  

---

## 🔄 While Loop

### 📌 What is a while loop?
A while loop keeps running **as long as the condition is True**.

---

### 🧠 Syntax

```python
while condition:
    statement 1
    statement 2

⚠ Important spacing rule (Indentation)

Code inside the loop must be indented (usually 4 spaces)

If indentation is wrong → ❌ error



---

✅ Example

i = 1

while i <= 5:
    print(i)
    i = i + 1

🟢 Output:

1
2
3
4
5


---

🛑 break Statement

break is used to stop the loop immediately, even if the condition is still true.

i = 1

while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

🟢 Output:

1
2


---

⏭ continue Statement

continue skips the current iteration and jumps to the next one.

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

🟢 Output:

1
2
4
5


---

🔂 For Loop

📌 What is a for loop?

A for loop is used to iterate over a sequence like:

list

string

range



---

🧠 Syntax

for variable in sequence:
    statements


---

✅ Example

for i in range(1, 6):
    print(i)

🟢 Output:

1
2
3
4
5


---

🔢 range() Function

range() is used to generate a sequence of numbers.

🧠 Syntax

range(start, stop, step)

start → starting number (default = 0)

stop → ending number (not included)

step → jump (default = 1)



---

✅ Examples

range(5)        # 0 to 4
range(1, 6)     # 1 to 5
range(1, 10, 2) # 1, 3, 5, 7, 9


---

💤 pass Statement

📌 What is pass?

pass is a null statement.
It does nothing but avoids an error when a statement is required.


---

✅ Example

for i in range(5):
    pass

🧠 Useful when:

you are writing code later

loop body is empty for now



---

⚡ Quick Summary

while → runs until condition becomes false

for → runs over a sequence

break → stops loop

continue → skips one iteration

range() → generates numbers

pass → does nothing, avoids error



---