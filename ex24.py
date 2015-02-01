print "Let\'s practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = '''
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
'''

print "____________________"
print poem
print "____________________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five 

# define function "secret_formula" and pass arg var "started"
# Return statement: example
def maxNumber(x, y):
    if x > y:
        return x
    elif x == y:
        return "The numbers are equal!"
    else:
        return y
        
a = 50
b = 50
# pass var assigned to value
print "The larger number is: ", maxNumber(a, b)
# pass value
print maxNumber(50, 25)

def secret_formula(started):
    # assign var jelly_beans to var "started" * 500
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # return values for assigned var
    return jelly_beans, jars, crates

# assign var start_point to value 10000    
start_point = 10000
# assign var "beans, jars, crates" to function "secret_formula", and pass var "start_point" to the function
# Remember, inside the function the var is "local" and temporary. Then, the returned value is assigned to a new "global" var 
beans, jars, crates = secret_formula(start_point)

# print "With a starting point of %d" % (start_point)
print "With a starting point of {}" .format(start_point)
# call var "beans_jars_crates" assigned to function and pass var arg "start_point"
# print "We\'d have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# Note: "beans" is a new var 
print "We\'d have {} beans, {} jars, and {} crates." .format(beans, jars, crates)

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % (secret_formula(start_point))
# print "We'd have {} beans, {} jars, and {} crates." .format(secret_formula(start_point))



