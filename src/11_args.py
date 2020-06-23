# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

def f1(number1, number2):
    return number1 + number2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

#you can pass down a list this way of unspecified length in the function definition. idk where this would be useful but it's neat
def f2 (*tupleOfNumbers):
    sum = 0
    for number in tupleOfNumbers:
        if isinstance(number, int):
            sum = sum + number
        elif isinstance(number, tuple) or isinstance(number, list):
            for number_tuple in number:
                sum = sum + number_tuple
    return sum

#
print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
# i created a conditional fork that checks the type of the input and either adds it or adds all of it's components
print(f2(a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
# if the function is called with a second argument then the value of 1 is overwritten
def f3(number, number2 = 1):
    return number + number2

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4 (**kwargs):
    #dictionary.items returns a list filled with tuples of key,value pairs from the original dictionary
    listOfKeyValuePairs = kwargs.items()
    for keyValuePair in listOfKeyValuePairs:
        print(f"{keyValuePair[0]}: {keyValuePair[1]}")

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
# f4(city="Berkeley", population=121240, founded="March 23, 1868")
#
# d = {
#     "monster": "goblin",
#     "hp": 3
# }

# How do you have to modify the f4 call below to make this work?
# f4(d)
