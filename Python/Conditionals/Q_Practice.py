# Q1. WAP to gradee students based on marks; marks>=90,grade ="A" ;90>marks>=80,grade = "B" ;80>marks>=70,grade = "C" ; 70>marks,  grade = "D".

marks = float(input("Enter your marks: "))

if(marks>=90):
    print("Grade A")
elif(90>marks>=80):
    print("Grade B")
elif(80>marks>=70):
    print("Grade C")
else:
    print("Grade D")


# Q2. WAP to check if a number entered by the user is odd or even.

num = int(input("Enter a number: "))

if(num%2 == 0):
    print("Even")
else:
    print("Odd")


# Q3. WAP to find greatest of 3 numbers entered by user.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if(num1 >= num2 and num1 >= num2):
    num = num1
elif(num2 >= num1 and num2 >= num3):
    num = num2
else:
    num = num3

print("The greatest among these three is:",num)


# Q4. WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter a number: "))

if(num % 7 == 0):
    print("Entered number is multiple of 7")
else:
    print("Not a multiple of 7")































