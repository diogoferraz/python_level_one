# Basics
# strings are immutable

string = 'abcdefg'

# Indexing
print(string[0])  # a

# Slicing
print(string[0:3])  # abc
print(string[4:])  # efg
print(string[:2])  # ab
print(string[::2])  # aceg
print(string[::-1])  # gfedcba
print(string[2:5]) # cde - define starting point and ending point however it is up to not including

# Basic Methods
upper = string.upper()
lower = string.lower()

print(upper)  # ABCDEFG
print(lower)  # abcdefg

mystring = 'Hello World'
split = mystring.split()
splitO = mystring.split('o')

#Print Formating
print_formating = "Isenrt anorther string here: {x}; another here: {y}".format(x="INSERT ME!",y= "cat")

print(print_formating)