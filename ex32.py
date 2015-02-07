
# var assigned to list
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

print(the_count)
print(fruits)
print(change)

"""
For loop statement iterates over a sequence of objects
This first kind of for loop goes through a list:
Iterates through passed var "the_count"
Cascades var number to var count to list; pre-defined for-loopfunction iterates
through the list.
"""

for index in the_count:
	print "This is count {}" .format(index)

# for-loop iterates through passed var fruits
for index in fruits:
	print "A fruit of type: {}" .format(index)

# also we can go through mixed lists too
# notice we have to use %r or {} since we have int and str
for index in change: 
	# print "I got {}" .format(change)
	print "I got {}" .format(index)
	# print "I got %r" % (index)
	# print "I got %r" % (change)

# We can also build lists, first assign var to empty list
# A list is an example of a python class
"""
When we use a var 'index' and assign a value to it, say integer 5, you can 
think of it as creating an object (ie instance) "index" of class (ie type) int.
"""
elements = []

# Then use the range function to do 0 to 5 counts.
for index in range(0,7):
	# print "Adding %d to the list." % index
	print "Adding {} to the list" .format(index)
	# Call .append method on elements var for list, and pass index parameter
	elements.append(index)
for index in elements:
	print "Element was: {}" .format(index)

print
elements.append('pparonson')
print("Adding {} to the list.") .format(index)
print("My list is now {}") .format(elements)

