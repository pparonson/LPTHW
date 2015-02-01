# An "import" adds features to your script from the python set; note feature = modules; this is how you unpack the argv vector
from sys import argv 

# The argv is the "argument variable", a standard name in programming. This variable "holds" the argumnents you pass to your python script; this argv is "set" to 4 var
script, first, second, third = argv 

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

first = raw_input("What is your name?")
second = raw_input("What is your age?")
third = raw_input("What is your height?")

# when I use argv in the code I should provide argument in the prompt before I start executing the program, whereas in raw_input I can actually provide the input at the runtime, that is, if I want to collect dynamic entry like "What is the current time?", then raw_input would be good, but if my code just requires me to enter the date for the day, I may provide through argv itself.

# raw input is like a pause button for the program, it will wait till the input is provided and argv just got the requirement input upfront in the command prompt itself and gets the work done. 


