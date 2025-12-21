# Q1. Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter a number: "))

def sum(a):
    if(a==0):
        return 0
    return sum(a-1) +a

print(sum(n))



# Q2. Write a recursive function to print all elements in a list. Hint: use list & index as parameters.

value = [1,2,3,4,5,6,7,8,9,10]

def ele(list,i=0):
    if(i == len(value)):
        return
    print(value[i])
    ele(list,i+1)

ele(value)







