"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("the value of x: %s, y: %s, z: %s " % (x, round(y, 2), z))

# Use the 'format' string method to print the same thing
# you can chain this method on any string and it will replace the empty bracs with the value in the dictionary you provide
print("the value of {}, {}, {}".format(x, round(y, 2), z))

# Finally, print the same thing using an f-string
# you can also use an f string which is like atemplate literal with an f at the front
# apparently this is a Python >= v3.0 only feature, needed to upgrade from v2.7.2
print(f"the value of x: {x}, y: {round(y, 2)}, z: {z}.")
