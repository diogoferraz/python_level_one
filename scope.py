# Scope
# scope levels LEGB

x = 25

def my_func():
    x = 50
    return x

print(x) # 25

print(my_func()) # 50

my_func()

print(x) # 25

# Local
lambda x: x**2

# Enclosing function locals
name = 'This is a global name'
def greet():
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

greet()

# Global
print(name)

def func(): 
    global name # danger, avoid global. 
    name = '1000'
func()
print(name) # This is a global name

# Built-in
len = 23 # don't do this because len is a reserved keyword
print(len) # 23

# Variables are stored in a namespace, and the scope determines the visibility of that variable name to other parts of your code.