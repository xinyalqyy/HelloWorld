
# it is aslo possible to format numbers
print '%d' % 42
print '{:d}'.format(42)

# format floats
print '%f' % 3.141592653589793
print '{:f}'.format(3.141592653589793)

# padding numbers
# align right
print '%10d' % 42
print '{:10d}'.format(42)

#align left
print '%-10d' % 42
print '{:<10d}'.format(42)

# align center
print '{:^10.2f}'.format(3.141592653589793)

# For floating points the padding value represents the length of the complete output
print '%10.2f' % 3.141592653589793
print '{:10.2f}'.format(3.141592653589793)

# sign numbers
# use a space character to indicate that negative numbers should be prefixed with
# a minus symbol and a leading space for positive ones.
print '% d' % 42
print '{: d}'.format(42)

print '% d' % -42
print '{: d}'.format(-42)

# control the position of the sign symbol relative to the padding.
print '{: =6d}'.format(+352)
print '{: 6d}'.format(+352)
print '{: =6d}'.format(+352)
print '{:=6d}'.format(-352)
print '{:6d}'.format(-352)
print '{:=6d}'.format(-352)

# named placeholders
dic = {'first':'Hodor','last':'Hodor!'}
print '%(first)s %(last)s' % dic
print '{first} {last}'.format(**dic)
