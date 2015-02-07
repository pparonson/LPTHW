"""
While-loops: 
1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
2. Review yoiur while-loop statements and make sure to  write false boolean into
the statement.
3. When in doubt, print out your test var at the top and bottom of the while-
loop to see what it is doing. 
"""

# Define function "whileLoopPractice"
def whileLoopFunction():

	# Assign var index to 0 
	index = 0
# Assign var numbers to list []
	numbers = []
	# While-loop statement
	while index < 6:
		print("At the top of the while-loop index is {}") .format(index)
		numbers.append(index)

# Increment the index
		index = index + 1
		print("Numbers now {}") .format(numbers)
		print("At the bottom of the while-loop index is {}") .format(index)

	print("The numbers: ") 

	# For-loop: 
	for index in numbers:
		print(index)

# Call whileLoopFunction
whileLoopFunction()

