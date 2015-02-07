# Define function "whileLoopPractice"
def whileLoopFunction():

	# Assign var index to 0 
	index = 0
# Assign var numbers to list []
	numbers = []
	# While-loop statement
	user_input = int(raw_input("Please enter a number >"))
	
	while index < user_input:
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

