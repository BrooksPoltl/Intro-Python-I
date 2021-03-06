"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
def foo(x):
    test = open(x)
    print(test.read())
    test.close()
    

foo('foo.txt')
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def bar(x):
    test = open(x, 'w')
    test.write('this is a test \nis it working \nplz reply')
    test.close()

bar('bar.txt')