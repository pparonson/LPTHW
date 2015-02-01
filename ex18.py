# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    #print "[1], [2]" .format arg1, arg2
    
def print_two_again(arg1, arg2):
    print  "arg1: %r, arg2: %r" % (arg1, arg2)

# Format method (See abop p. 86)    
def print_two_final(arg1, arg2):
    print "{0}, {1}" .format(arg1, arg2)
    
def print_one(arg1):
    print "arg1 %r" % (arg1)
    
def print_none():
    print "I got nothin\'"
    
print_two('Preston', 'Aronson')
print_two_again('Preston', 'Aronson')
print_two_final('Preston', 'Aronson')
print_one('First!')
print_none()