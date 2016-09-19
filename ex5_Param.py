from datetime import datetime

print '{:{align}{length}}'.format('test', align='^', length='10')

# prametrized precision
print '%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182)
print '{:.{prec}} = {:.{prec}}'.format('Gibberish', 2.7182, prec=3)

# the precision for floating point numbers limits the number of positions after
# the decimal point.
print '{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
# get the same result above
print '{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3')

# the components of a data-time can be set separately
dt = datetime(2001, 2, 3, 4, 5)
print '{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')
