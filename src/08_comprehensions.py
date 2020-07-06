"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
# array = [1, 2, 3, 4, 5]
# this is what a list comprehension looks like. It's a bit weird, kinda like a lambda expression but only for lists. Like a weird map syntax?
# resultVariable = [singleElementInTheList for singleElementInTheList in listOfELements (optional additional conditions)]
y = [count for count in range(6)][1:]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [count ** 3 for count in range(10) ]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
# input is pretty cool, helpful for scripts. Link up to a React form?


x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [number for number in x]

print(y)