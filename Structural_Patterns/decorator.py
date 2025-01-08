from functools import wraps


def make_blink(function):
    """Defines the decorator"""
    
    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"
    
    return decorator


# Apply the decorator here
@make_blink
def hello_world():
    """Original Function"""
    return "Hello, World!"

print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)


""" Function Decorators
The most common type of decorator, which takes a function as input and 
returns a new function.
"""
def simple_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper 

@simple_decorator
def greet():
    print("Hello, World!")

greet()


""" Method Decorators 
Used to decorate methods within a class. They often handle special cases, 
such as the self argument for instance methods.
"""
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()


""" Class Decorators
Class decorators are used to modify or enhance the behavior of a class. 
Like function decorators, class decorators are applied to the class definition. 
They work by taking the class as an argument and returning a modified version of the class.
"""
def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass

print(Person.class_name)
