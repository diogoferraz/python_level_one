# Given a list of ints, return True if the sequence of number 1,2,3 appears in the list somewhere.

# for example:
# array_check([1, 1, 2, 3, 1]) -> True
# array_check([1, 1, 2, 4, 1]) -> False
# array_check([1, 1, 2, 1, 2, 3]) -> True

def array_check(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

print(array_check([1, 1, 2, 3, 1]))
print(array_check([1, 1, 2, 4, 1]))

# Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".

# For example:
# string_bits('Hello') -> 'Hlo'
# string_bits('Hi') -> 'H'
# string_bits('Heeololeo') -> 'Hello'

def string_bits(str):
  result = ''
  for i in range(len(str)):
    if i%2 == 0:
      result = result + str[i]
  return result

# result = str[::2]



print(string_bits('Hello'))

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
# Note: s.lower() returns the lowercase version of a string.

# Examples:
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

def end_other(a, b):
  a = a.lower()
  b = b.lower()

  return a[-(len(b)):] == b or a == b[-(len(a)):]

# return a.endswith(b) or b.endswith(a)

print(end_other('Hiabc', 'abc'))

# Given a string, return a string where for every character in the original there are two chars

# Examples:
# double_char('The') -> 'TThhee'
# double_char('AAbb') -> 'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'

def double_char(str):
  result = ''
  for char in str:
    result += char*2
  return result

print(double_char('The'))

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):" that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum(). Again, you will have two functions for this problem!

# Examples:
# no_teen_sum(1, 2, 3) -> 6
# no_teen_sum(2, 13, 1) -> 3
# no_teen_sum(2, 1, 14) -> 3

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
    return 0
  return n

print(no_teen_sum(1, 2, 3))

# Return the number of even integers in the given array

#Examples:

# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0

def count_evens(nums):
  count = 0

  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

print(count_evens([2, 1, 2, 3, 4]))