## PROBLEM 1
# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])

# 'o'
print(s[-1])

# 'djan'
print(s[:4])

# 'jan'
print(s[1:4])

# 'go'
print(s[-2:])

# Bonus: Use indexing to reverse the string
print(s[::-1])

# Given this nested list:
l = [3,7,[1,4,'hello']]

# Reassign "hello" to be "goodbye"
l[2][2] = 'goodbye'

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep, hello']}]}

indexing1 = d1['simple_key']
print(indexing1)

indexing2 = d2['k1']['k2']
print(indexing2)

indexing3 = d3['k1'][0]['nest_key'][0]
print(indexing3)

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,2,2,2,2,3,3,3,3]
uniqueList = set(mylist)
print(uniqueList)

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
print("Hello my dog's name is {name} and he is {age} years old.".format(name=name, age=age))