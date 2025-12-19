# Python Strings — Basics & Operations

## Creating a String

s = "hello"
s2 = 'world'

Concatenation

result = s + " " + s2

## Length of a String

length = len(s)

## Indexing (Positive)

s = "python"
char = s[0]
char2 = s[3]

## Indexing (Negative)

last_char = s[-1]
second_last = s[-2]

## Slicing

part = s[0:3]
part2 = s[2:]
part3 = s[:4]

## Slicing with Negative Index

part = s[-4:-1]

## String Functions

* Convert to Uppercase

        s.upper()

* Convert to Lowercase

        s.lower()

* Capitalize First Letter

        s.capitalize()

* Swap Case

        s.swapcase()

* Replace a Substring

        s.replace("py", "my")

* Find a Substring

        s.find("th")

* Count Occurrences

        s.count("o")
