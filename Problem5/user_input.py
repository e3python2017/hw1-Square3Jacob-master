# Problem 5: User Input
#
# In this exercise, we will ask the user for his/her first and last name and date of birth and print them out formatted.
# Recall that you can get input from the user using the command raw_input("text").
#
# Note: There are two functions to get user input. The first, raw_input, turns whatever the user inputs into a string
# automatically. The second, input, preserves type. So, if the user inputs an int or a float, you will get an int or
# a float (rather than a string). Be careful though- you still want to use raw_input if you want a string back, or
# otherwise the user will have to put quotes around their answer. Use raw_input here - it's good for string processing,
# like this problem. input will come in handy when using user input to compute math.
#
# Example Output:
#
# Enter your first name: Chuck
# Enter your last name: Norris
# Enter your date of birth:
# Month? March
# Day? 10
# Year? 1940
# Chuck Norris was born on March 10, 1940.
#
# To print a string and a number in one line, you just need to separate the arguments with a comma (this works for
# any two types within a print statement). The comma adds a space between the two arguments. For example, the
# lines:
#
# mo = 'October'
# day = '20'
# year = '1977'
# print mo, day, year
#
# will have the output:
#
# October 20 1977

# 1. Ask for the first name and store it in a variable
a = "What is your name?"
print a
# 2. Ask for the last name and store it in a variable
b = "Whats ur last name?"
print b
# 3. Print "Enter your date of birth:"
c = "Enter your date of birth"
print c
# 4. Ask for the Month and store it in a variable
d = "Name a month"
print d
# 5. Ask for the day and store it in a variable
e = "Name a day"
print e
# 6. Ask for the year and store it in a variable
f = "Name a year"
print f
# 7. Print the name with the date of birth as shown above.
g = "Nov 19 2002"
print g
