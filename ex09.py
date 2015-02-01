# Here's some new strange stuff, remember to type it exactly.

day = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # "\n" = "new line"

print "Here are the days: {0}" .format (day) # "\n" did NOT work with ".format" method

print "Here are the days: ", day
print "Here are the months: ", months

print """""" # behaves like a "#"
