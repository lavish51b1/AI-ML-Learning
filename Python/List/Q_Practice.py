# Q1. WAP to ask the user to enter names of their 3 favourite movies & store them in a list.
"""
print("Enter Your favorite movies")
a = input("First: ")
b = input("Second: ")
c = input("Third: ")

list = [a,b,c]
print(list)



# Q2. WAP to check if a list contains a palindrome of elements.

listt = [1,2,3,2,1]
list2 = listt.copy()
list2.reverse()

if(listt == list2):
    print("List is Palindrome")
    print(listt)
else:
    print("List is not Palindrome")
"""


# Q3. Store the values C,D,A,A,B,B,A in a list & sort them from "A" to "D"

values = ["C","D","A","A","B","B","A"]
values.sort()
print(values)














