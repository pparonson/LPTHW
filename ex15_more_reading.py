# import argv module to hold arguments to pass to the python script
from sys import argv

script, filename = argv

# Assign var txt to "open() method and pass the "filename" as parameter
# to open the desired file
txt = open(filename)

print "Here\'s your file {0}" .format(filename)

# Call .read() method with no parameters
print txt.read()
print txt.close()

print "Type the filename again: "

# Assign var "file_again" to method raw_input() a
file_again = raw_input('>>> ')

txt_again = open(file_again)

print txt_again.read()
print txt_again.close()