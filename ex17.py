
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print 'Coping from %s to %s' % (from_file, to_file)
#
# infile = open(from_file)
# indata = infile.read()
#
# print 'The input file is %d bytes long' % len(indata)
#
# print 'Does the output file exist? %r' % exists(to_file)
# print 'Ready, hit RETURN to continue, CTRL-C to abort.'
# raw_input()
#
# outfile = open(to_file, 'w')
# outfile.write(indata)
#
# print 'Alright, all done.'
#
# outfile.close()
# infile.close()

open(to_file,'w').write(open(from_file).read())
