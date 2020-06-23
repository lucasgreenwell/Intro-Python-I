"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# this saves it as a weird data type, a textEncoding
foo_text_file = open("foo.txt", 'r')
# Print all the contents of the file, then close the file
print(foo_text_file.read())
# Note: pay close attention to your current directory when trying to open "foo.txt"



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing.
bar_text_file = open("bar.txt", "w+")
# Write three lines of arbitrary content to that file,
bar_text_file.write("/n /n /n look i made a text file")
bar_text_file.close()
bar_text_file = open("bar.txt", "r")
print(bar_text_file.read())
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE