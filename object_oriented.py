# every thing in python is an object !
# class is a blueprint for creating objects
# object is an instance of a class

# class definition
class Sample():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Dog():
    
    # class object attribute
    species = 'mammal'

    # constructor
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    
    # methods
    def bark(self):
        print("Woof! My name is {}".format(self.name))

    def set_breed(self, new_breed):
        self.breed = new_breed

mydog = Dog(breed='Lab', name='Sammy', spots=False)
otherdog = Dog(breed='Huskie', name='Huskie', spots=True)
print(type(mydog))
print('the breed is', mydog.breed)
print('the breed is', otherdog.breed)
mydog.bark()
otherdog.bark()

# Inheritance
class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Cat(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("Cat created")

    def who_am_i(self):
        print("I am a cat")

    def meow(self):
        print("Meow")

mycat = Cat()
mycat.who_am_i()
mycat.eat()
mycat.meow()

# Special Methods
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # string representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}"

    # length of the object
    def __len__(self):
        return self.pages

    # delete the object
    def __del__(self):
        print("A book object has been deleted")

my_book = Book('Python Rocks', 'Jose', 200)
print(my_book)
print(len(my_book))
del my_book