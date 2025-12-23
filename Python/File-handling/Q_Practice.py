# Q1. Create anew file "Practice.txt" using python. Add the following data in it.

"""
Hi Everyone
We are learning File I/O
using python
I like programming in python.
"""

f= open("practice.txt","x")
f.write("Hi everyone\nWe are learning File I/O\nusing python\nI like programming in python.")
f.close()


# Q2. WAF that replace all occurrence of "python" with "java" in above file.

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("python","java")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)



# Q3. Search if the word "learning" exits in the file or not.

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.find("learning")
if (new_data != -1):
    print("Exists")
else:
    print("Not exists")



# Q4. WAF to find in which line of the file does the word "learning" occur first. Print -1if word not found.

def find_line():
    word = "learning"
    data = True
    line_no =1

    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

        print(-1)

find_line()



# Q5. From a file containing numbers separated by comma, print the count of even numbers.

count = 0

with open("practice.txt", "r") as f:
    data = f.read()

     # Method-1

     #nums = data.split(",")
     #for val in nums:
     #    if int(val) % 2 == 0:
     #        count += 1
     # print(count)



    # Method-2

    num = ""
    for ch in data:
        if ch == ",":
            if int(num) % 2 == 0:
                count += 1
            num = ""
        else:
            num += ch

    # check last number
    if int(num) % 2 == 0:
        count += 1

print(count)




























