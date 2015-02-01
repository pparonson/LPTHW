# Import argv module / library from system
from sys import argv

# Allows passage of input file into the argv module
script, input_file = argv

# Define the function and pass the file into the function
def print_all(file):
    print file.read() # Call the .read method 
# Call the .seek method and pass file argument into the function parameter. (0): means your reference point is the beginning of the file.
def rewind(file):
    file.seek(0) 
    
def print_a_line(line_count, file): # pass arguments (line_count and file) into the function
    print line_count, file.readline() # call the .readline method
    
current_file = open(input_file)
    
print "First let\'s print the whole file:\n"

# Call print_all function
print_all(current_file)

print "Now let's rewind, kind of like a tape:\n"

# Call rewind function and pass current_file into the function
rewind(current_file)

print "Let's print three lines:\n"

# Call print_a_line function and pass current_line and current_file arguments into the function
current_line = 1
print_a_line(current_line, current_file) 

# Call current_line function and assign advance current_line function 1 line command, then call print_a_line function and pass current_line and current_file arguments
current_line = current_line + 1
print_a_line(current_line, current_file)

# Call current_line function and assign advance current_line function 1 line command, then call print_a_line function and pass current_line and current_file arguments
current_line = current_line + 1
print_a_line(current_line, current_file)
    
