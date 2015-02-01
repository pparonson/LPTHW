# Import argv function from system; Import "exists" from os.path (Returns True if file exists)
from sys import argv
from os.path import exists

# argv called into function
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file); indata = in_file.read()

# pass str to len() function to return length
print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

out_file = open(to_file, 'w'); out_file.write(indata)

print "Alright, all done."

out_file.close(); in_file.close()
