people = 30
cars = 40
buses = 15

# True results True
if cars > people:
	print "We should take the cars."
# False results False
elif cars < people:
	print "We should not take the cars."
else:
	print "We can\'t decide"

# False results False
if buses > cars:
	print "That\'s too many buses."
# True results True
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can\'t decide."

# True results True
if people > buses:
	print "Alright, let\'s just take the buses."
else:
	print "Fine, let\'s stay home then."

# True and True results True
if cars > people and buses < cars:
	print "We should definitely take the buses."

