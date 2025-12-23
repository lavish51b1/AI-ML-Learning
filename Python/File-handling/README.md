# 📁 File Handling (I/O) in Python

## 📌 What is File Handling?

### File handling allows a program to:

    Read data from a file
    Write data into a file
    Store data permanently (unlike variables)

## 📂 Types of Files in Python

### 1️⃣ Text Files

    • Store data as readable characters  
    • Examples: `.txt`, `.csv`, `.py`

### 2️⃣ Binary Files

    • Store data in binary format (0s and 1s)  
    • Used for images, videos, audio, PDFs  
    • Examples: `.jpg`, `.mp3`, `.mp4`, `.exe`

## 🧠 Basic File Handling Flow

    1. Open a file  
    2. Perform operation (read / write / append)  
    3. Close the file

## 🔓 Opening a File

    🔹 Syntax
        file_object = open("filename", "mode")

    🔹 Example
        f = open("data.txt", "r")


## ⚙️ File Modes (VERY IMPORTANT)

### 📌 Common File Modes

    r → Read mode
        • Reads existing file  
        • Error if file does not exist  
        • Default mode

    w → Write mode
        • Creates new file if not exists  
        • Overwrites existing file ❗

    a → Append mode
        • Adds data at end of file  
        • File pointer at last position

    x → Exclusive creation
        • Creates file  
        • Error if file already exists

    b → Binary mode
        • Used with other modes  
        • Example: `rb`, `wb`

    t → Text mode
        • Default mode  
        • No need to mention explicitly


## 🧠 Default Stuffs (Must Remember)

    • Default mode → `r`
    • Default file type → Text
    • File pointer starts at beginning (except append)
    • Files must be closed after use

## c📖 Reading a File

### read() Method
Reads entire file content.

    Syntax
        file.read()

    Example
        f = open("data.txt", "r")
        content = f.read()
        print(content)
        f.close()

    Things to Remember

        • Reads whole file at once  
        • Not memory-efficient for large files
---
### read(n) → Read specific characters

    f.read(5)    # reads first 5 characters
---
### readline() Method

Reads one line at a time.

    Example

        f = open("data.txt", "r")
        line = f.readline()
        print(line)
        f.close()

    Things to Remember

        • Includes newline `\n`  
        • Good for line-by-line processing
---
### readlines() Method
    Reads all lines and returns a list.
    lines = f.readlines()
---
## ✍️ Writing to a File

### Writing Using write()

    Syntax
        file.write("text")

    Example
        f = open("data.txt", "w")
        f.write("Hello World")
        f.close()

## ⚠️ Overwriting Explained (IMPORTANT)

    If file already exists and mode is w: • Old data is completely deleted
    • New data replaces it

    f = open("data.txt", "w")
    f.write("New Data")

### 👉 Old content = 💀 gone

## Appending to a File (a)

    Example
        f = open("data.txt", "a")
        f.write("\nMore data added")
        f.close()

    Things to Remember
        • Data is added at the end  
        • Existing content remains safe

---
### 🔁 Writing Multiple Lines

    lines = ["Line 1\n", "Line 2\n"]
    f.writelines(lines)

## 🔒 Closing a File

### Why Closing is Important?
    • Frees system resources  
    • Ensures data is saved properly
---
    f.close()
---

## ✅ Best Practice: with Statement (HIGHLY RECOMMENDED)

    Syntax
        with open("data.txt", "r") as f:
            content = f.read()

    Why use it?
        • Auto-closes file  
        • Cleaner and safer code
---
## 🗑️ Deleting a File

### Using os Module

    Syntax
        import os
        os.remove("filename")

    Example
        import os
        os.remove("data.txt")

## ⚠️ Things to Remember Before Deleting

    • File must exist  
    • Otherwise → FileNotFoundError  
    • Always check before deleting

        if os.path.exists("data.txt"):
        os.remove("data.txt")

## 🚨 Common Errors & Fixes

    FileNotFoundError

        • File doesn’t exist  
        • Wrong path or name

    PermissionError

        • No permission to access file

## 🧠 Real-World Tips

    • Use `with` statement always  
    • Avoid `w` mode unless overwriting is intended  
    • Use append for logs  
    • Read large files line-by-line

## 🔚 Summary (Quick Recall)

    • Files store data permanently  
    • Modes control file behavior  
    • `r` is default  
    • `w` overwrites  
    • `a` appends  
    • Close files or use `with`  
    • Use `os.remove()` to delete files
