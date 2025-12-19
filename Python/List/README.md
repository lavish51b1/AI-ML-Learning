# Python Lists — Basics & Methods

## What is a List?
* A list is an ordered, mutable collection
* Lists can store multiple data types

        my_list = [1, 2, 3, "apple", 4.5]


## Length of a List

    length = len(my_list)


## Accessing Elements (Indexing)

* Positive indexing

* Negative indexing

        my_list[0]
        my_list[2]
        my_list[-1]
        my_list[-2]


## List Slicing

Extracting a part of the list

    my_list[0:3]
    my_list[2:]
    my_list[:4]
    my_list[-4:-1]


## List Methods

* Append (add at end)

        my_list.append(10)

* Insert (add at specific index)

        my_list.insert(2, "new")

* Remove (remove by value)

        my_list.remove("apple")

* Pop (remove by index)

        my_list.pop()
        my_list.pop(1)

* Sort (ascending order)

        my_list.sort()

* Reverse the List

        my_list.reverse()


## Extra Useful Methods

* Clear the list

        my_list.clear()

* Count elements


        my_list.count(2)

* Find index of element


        my_list.index(3)

