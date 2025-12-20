# Q1. Print number 1 to 100.

i = 1
while i<=100:
    print(i)
    i+=1


# Q2. Print the multiplication table of a number n.

n = int(input("Enter a number: "))
i=1
while i<=10:
    print(n*i)
    i+=1


# Q3. Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]

square = [1,4,9,16,25,36,49,64,81,100]
i=0
while i<=len(square)-1:
    print(square[i])
    i+=1


# Q4. Search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]

square = (1,4,9,16,25,36,49,64,81,100)
print(square)

x = int(input("Enter a no. from the above tuple: "))

i=0
while i<=len(square)-1:
    if(x == square[i]):
        print("number is present at index: ",i)
        break
    i+=1
else:
    print("not found")
    

# Q5. Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100] using for loop

squr = [1,4,9,16,25,36,49,64,81,100]
for value in squr:
    print(value)


# Q6. Search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100] using for loop.

x = int(input("Enter a number: "))
i=0
sqr = (1,4,9,16,25,36,49,64,81,100)
for value in sqr:
    if(x == sqr[i]):
        print("Found at index",i)
        break
    i+=1
else:
    print("not found")


# Q7. Print numbers from 1 to 100.

for i in range(0,101):
    print(i)


# Q8. Print numbers from 100 to 1.

for i in range(0,101):
    print(100-i)


# Q9. Print the multiplication table of a number n.

n = int(input("Enter a numer: "))
for i in range(1,11):
    print(i*n)


# Q10. WAP to find the sum of first n numbers.(using while)

n = int(input("Enter a number: "))

i=0
a=0
while i<=n:
    a+=i
    i+=1
print(a)


# Q11. WAP to find the factorial of first n numbers.(using for)

n = int(input("Enter a number: "))
a=1
for i in range(1,n+1):
    a*=i
    i+=1
print(a)



































































































































































































