""" Q1. Store following word meanings ina python dictionary: 
table: "a piece of furniture", "list of facts & figures"
cat: "a small animal"
"""
House = {
    "table" : ("a piece of furniture", "list of facts & figures"),
    "cat" : "a small animal",
}
print(House)


"""
Q2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
"python","java","C++","python","javascript","java","python","C++","C"
"""

subject = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(subject))



# Q3. WAP to enter markws of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.


score = {}

sub1 = int(input("Enter marks: "))
sub2 = int(input("Enter marks again: "))
sub3 = int(input("Enter marks once more: "))

score["maths"] = sub1
score["chem"] = sub2
score["evs"] = sub3

print(score)



# Q4. Figure out a way to store 9 & 9.0 as seperate values in the set.

values = {
    ("float",9.0),
    ("int",9)
}
print(values)









