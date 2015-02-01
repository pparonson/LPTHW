#COMMANDS
# close - Closes the file. Like File --> Save in the editor
# read - Reads the contents of the file. You can assign the result to a var
# readline - Reads just one line of a text file
# truncate - Empties the file. Watch out if you care about the file
# write('stuff') - Writes "stuff" to the file

# Imports the argv method
from sys import argv

# Assigns the var to the argv.
script, filename = argv

# Pass filname into command.
print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# 
raw_input('?')

# Opens the specified file and passes the ability to write to the file.
print "Opening the file..."
target = open(filename, 'w')

# Erases the specified file.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# Assigns raw_input to each var
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Writes the var to the file.
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write (line1, '\n', line2, '\n', line3, '\n') # Cannot provide 6 argv to 1 func ?

print "And finally, we close it."

# Closes the file.
target.close()