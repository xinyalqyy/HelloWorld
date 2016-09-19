
filename = raw_input('Please input a filename:')
target = open(filename,'w')

line1 = raw_input('Line 1:')
line2 = raw_input('Line 2:')
line3 = raw_input('Line 3:')

# strings = [line1, line2, line3]
target.write('%s\\n %s\\n %s\\n' % (line1, line2, line3))
target.close()

print open(filename).read()
