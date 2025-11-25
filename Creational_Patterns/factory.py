# Lets subclasses decide which class to instantiate for a single object.

class Dog:
    """A simple Dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"
    

class Cat:
    """A simple Cat class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"
    

def get_pet(pet="Dog"):
    """The Factory method"""
    pets = dict(dog = Dog("Hope"), cat = Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
