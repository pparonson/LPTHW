x = 'There are %d types of people.' % 10 # str embedded within a str
binary = 'binary'
do_not = "don't"
y = 'Those who know %s and those who %s.' % (binary, do_not)

print x
print y

print 'I said: %r.' % x # Use the %r for debugging
print "I also said: '%s'" % y # I’ll use a single-quote inside a string that has double-quotes

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation % hilarious

w = 'This is the left side of...'
e = 'a string with a right side.'

print w + e

