# argv method to import file into script, this method would usually be better because it is not executed during runtime.
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
print txt.close()

# raw input method to import file into script
print "Type the filename again:"
file_again = raw_input('>')

txt_again = open(file_again)

print txt_again.read()
print txt_again.close()