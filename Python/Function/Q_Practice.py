# Q1. WAP to make a function which calculate the average of 3 values.

def avg(a,b,c):
    average = ((a+b+c)/3)
    return average

print(avg(10,100,1000))



# Q2. WAF to print the elements of a list in a single line.(list is the parameter)

accounts = ["1million","17million","138million","57billion"]

def print_list(list):
    for el in list:
        print(el, end=" ")

print_list(accounts)



# Q3. WAF to print the length of a list. (list is the paramenter)

accounts = ["1million","17million","138million","57billion"]

def print_len(list):
    print(len(list))   

print_len(accounts)



# Q4. WAF to find the factorial of n. (n is the parameter)

n = int(input("Enter a number: "))

def fact(n):
    a=1
    for i in range(1,n+1):
        a*=i
    print(a)

fact(n)



# Q5. WAF to convert USD to INR

amt = int(input("Enter the USD: "))

def convt(amt):
    a = amt*90
    print(a)

convt(amt)



# Q6. WAF to return "Even" for an even input and "odd" for an odd input.(homework Q)

num = int(input("Enter a number: "))

def num_check(num):
    if( num%2 == 0):
       print("'EVEN'")
    else:
       print("'ODD'")
        
num_check(num)









