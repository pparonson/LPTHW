# This exercise demonstrates that the variable in the function are NOT connected to the variable in the script!

# Define the function and name the parameters.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Method 1. 
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that\'s enough for a party!"
    print "Get a blanket.\n"
    
    # print "You have {0}" .format(cheese_count)
    # print "You have {1}" .format(boxes_of_crackers)
    # print "Man that\'s enough for a party!"
    
# Method 1. Call the function with the values directly.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Method 2. Set variables to the values, and then call the function.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Method 3. Combination of variable and math.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# In a way, the arguments to a function are kind of like our assignment character (=) when we make a variable. In fact, if you can use (=) to name something, you can usually pass it to a function as an argument.

def height_and_weight(height, weight):
    print "I am {} inches tall and I weigh {} lbs." .format(height, weight)
    print "That is the perfect size for a point guard!\n"
    
# Method 1 to call the function "height_and_weight". 
print "I can call the function with the values directly:"
height_and_weight(71, 177)

# Method 2. Setting the variables.
print "I can also call the function using variables set to the values."
actual_height = 71
actual_weight = 177

height_and_weight(actual_height, actual_weight)





    
    