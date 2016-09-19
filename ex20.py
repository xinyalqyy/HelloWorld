from sys import argv

script, input_file = argv

# print the whole info from the file
def print_all(f):
    print f.read()

# reset the position where start reading
def rewind(f):
    f.seek(0)

# print a line
def print_a_line(line_count, f):
    print line_count, f.readline()
# print all lines with line number before it
def print_lines(lines_count, f):
    for i in range(lines_count):
        print_a_line(i+1, f)

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print"rewind again!"
rewind(current_file)

print "Let's print specific lines we want: "
print_lines(2,current_file)

# never forget to close the file
current_file.close()
