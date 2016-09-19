# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print 'arg1: %r , arg2: %r' % (arg1, arg2)
# *argv is pointless, we can just do this
def print_two_again(arg1, arg2):
    print 'arg1 : %r, arg2: %r' % (arg1, arg2)
# this just takes one argument
def print_one(arg1):
    print 'arg1: %r' % arg1
# this takes no argument
def print_none():
    print "I got nothin'."

# use functions above
print_two('wang','ran')
print_two_again('wang','ran')
print_one('Only')
print_none()
