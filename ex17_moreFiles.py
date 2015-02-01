# from system import argument variable module to pass variable parameters
from sys import argv
from os.path import exists

# Pass 3 var parameters to argv module
script, from_file, to_file = argv

# Call .format method and pass vars "from_file and to_file" to print to console
print "Copying from {} to {}.." .format(from_file, to_file)

# Assign var "in_file" to the value of function "open()" and pass from_file parameter
# Assigne var "indata" to value of method .read(); .read() called without parameters
in_file = open(from_file)
indata = in_file.read()

print "The input file is {} bytes long." .format(len(indata))

print "Does the output file exist? {}" .format(exists(to_file))
print "Ready, hit RETURN to continue, CTRL-C to abort."

# Call function raw_input() and pass client input as value
# prompt = ">"
raw_input()

out_file = open(to_file, 'w')
# Call .write() method and pass "indata" as var parameter
out_file.write(indata)

print "Done."

out_file.close()
in_file.close()