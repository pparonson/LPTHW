print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "So, you're {0} years old, {1} inches tall, and {2} pounds heavy." .format (
    age, height, weight)