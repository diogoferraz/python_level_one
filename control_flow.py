# Comparison Operators
# Equality
1 == 1
1 != 0

# Logical Operators
# AND
(1 > 2) and (2 < 3)

# OR
(1 >2) or (2 < 3)

# Multiple logical operators
(1 == 2) and (2 == 3) or (4 == 4)

if 1 < 2:
  print('Yep!')
  if 2 < 3:
    print('Second Yep!')

if 1 < 2:
  print('First Block')
elif 3 == 3:
  print('Elif Block')
else:
  print('Second Block')

# Loops
# For Loops

bucket = [1,2,3,4,5,6]
for grapes in bucket:
  # code here
  print(grapes)

dictionary = {'k1':1, 'k2':2, 'k3':3}
for key in dictionary:
  print(key)
  print(dictionary[key])

for values in dictionary.values:
  print(values)

for keys in dictionary.keys:
  print(values)

# Tuple unpacking
tuples = [(1,2), (3,4), (5,6)]

for tup1, tup2 in tuples:
  print(tup1)
  print(tup2)

# While Loops
i = 1
while i < 5:
  print(f'i is: {i}')
  i = i + 1

# Range
list = [1,2,3,4,5]
theRange = range(0,5)

print(theRange)

for item in range(10):
  print(item)

# List Comprehension
x = [1,2,3,4]

out = []
for num in x:
  out.append(num**2)

print(out)

listcomprehension = [num**2 for num in x]
print(listcomprehension)