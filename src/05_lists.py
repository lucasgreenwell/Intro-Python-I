# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
# append is python's push method
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
#the extend method will spread the argument list into the main list
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
#the remove method finds an element with the argument value and removes it
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
#the insert method takes first an index and then a value to inject at the given index
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
#len is a builtin method that measures any data collection
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
#you can use lambda expressions the same as in Java or the same as an arrow function in JS
#map is a builtin function that takes a callback followed by an iterable collection and returns a map
# printing a map only returns a memory location so you must typecast it as a list to print it's values
print(list(map( lambda ele : ele * 1000, x)))
