# Assign "formatter" var to "%r %r %r %r"
formatter = "%r %r %r %r"

# print value of formatter var with hard values passed into parameter
print "This will print hard values.", formatter % (1, 2, 3, 4)
print "This will pass variables.", formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing", 
"That you could type up right.", 
"But it didn\'t sing.", 
"So I said goodnight."
)

# \r - Carriage return
# \n - linefeed
# \\ - Backslash

# input() versus raw_input() - input() will attempt to conversion; 
# input() is recommended to avoid

# Example  - y = raw_input("Name? ")
# Also see "pydoc raw_input"

# module that accept arguments to pass variables
# the variable holds the arguments you pass to your python script
from sys import argv
# "Unpacks" argv so that, rather than holding all the arguments
# it gets assigned to multiple variables you can work with
script, user_name = argv

prompt = '>'

print "Hi {1}, I\'m the {0} script." .format (user_name, script)


