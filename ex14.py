
from sys import argv

script, user_name = argv
promt = '>>>'

print "Hello %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(promt)

print "Where do you live %s?" % user_name
lives = raw_input(promt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(promt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer)
