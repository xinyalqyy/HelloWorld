
from sys import argv

# unpacking the argument variable
script, first, second, third = argv

# print the arguments above
print 'The script is called:', script
print 'Your first variable is:', first
print 'Your second variable is:', second
print 'Your third variable is:',third

ans1 = raw_input('Do you like your job?')
ans2 = raw_input('Are you happy?')
ans3 = raw_input('Try somthing different!,OK?')

if ans1=='yes':
    print 'Yes,I like it very much!'
else:
    print 'I am not sure about that,maybe not!'

if ans2=='yes':
    print "Yes, I'm very happy"
else:
    print "I'm afraid not!"

if ans3=='Ok':
    print "Ok,I'll try it,wish me good luck!"
else:
    print "Nothing will change,I give it up!"
