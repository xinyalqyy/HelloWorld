
from sys import argv

# unpack the arguments
script, filename = argv

# open a file
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# remember to close the file when finished
txt.close()

print "Type the file name again:"
file_again = raw_input('>')

txt_again = open(file_again)
print txt_again.read()

# remember to close the file when finished
txt_again.close()
