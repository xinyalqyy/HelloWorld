print '%s %s' % ('one','two')
print '{} {}'.format('one','two')
print '{} {}'.format(1,2)

print '{0!s} {1!r}'.format('one','two')
# change order
print '{1} {0}'.format(1,2)

# %r print no matter what it is
my_gender = 'girl'
my_age = 29
print 'I am a %s' % my_gender
print 'I am a %r' % my_gender
print 'I am %d year old.' %my_age
print 'I am %r year old.' %my_age

# padding and aligning strings
names = ['Lily','Andy','Rebecca']
# align right
for name in names:
    print('%10s' % name)
    print('{:>10}'.format(name))
#align left
for name in names:
    print('%-10s' % name)
    print('{:10}'.format(name))
#align center
for name in names:
    print('{:&^10}'.format(name))

# use underscore for padding
print '{:_<20}'.format('congratulations')

# truncating long strings
# The number behind a . in the fomat specifies the precision of the output.
print '%.5s' % 'Morning'
print '{:.5}'.format('Morning')

# combine truncating and padding
print '%10.6s' % 'love you'
print '{:@>10.6}'.format('love you')
