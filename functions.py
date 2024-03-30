def my_func(param1=''):
  """
  Docstring: Information about the function
  """
  print("my first python function! {}".format(param1))

my_func()

def hello():
  return "hello"

print(hello())

def addNum(num1, num2):
  if(type(num1) == type(num2) == type(10)):
    return num1 + num2
  else:
    return 'Sorry, I need integers!'

result = addNum(2,3)
print(result)

# Filter
my_list = [1,2,3,4,5,6,7,8]

def even_bool(num):
  return num%2 == 0

# Lambda expression
evens2 = filter(lambda num: num%2 == 0, my_list)
print(list(evens2))

evens = filter(even_bool, my_list)
print(list(evens))

print('x' in [1,2,3, 'x'])