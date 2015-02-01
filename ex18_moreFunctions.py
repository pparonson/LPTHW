# Define function and pass *args parameter
# *args - similar to argv parameter, but for functions rather than modules
def print_two (*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Alternatively,
def print_two_alternate (arg1, arg2):
	print "{}:, {}:" .format(arg1, arg2)

# Define function and pass 1 arg var
def print_one(arg1):
	print "arg1: %r" % (arg1)

# Call the functions:
print_two("Preston", "Ashley")
print_two_alternate("Preston", "Ashley")
print_one("Preston")
