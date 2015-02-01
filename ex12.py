print "How old are you?",
age = raw_input("How old are you? ")
print "How tall are you?",
height = raw_input("How tall are you? ")
print "How much do you weigh?",
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
print "So, you're {0} old, {1} tall, and {2} heavy." .format (
    age, height, weight)