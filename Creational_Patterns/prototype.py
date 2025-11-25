# Copies existing objects to create new ones.

import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
    

class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Black"
        self.options = "Ex"

    def __str__(self):
        return f"{self.name} | {self.color} | {self.options}"
    

c = Car()
print(c)

prototype = Prototype()
prototype.register_object('skylark', c)

c1 = prototype.clone('skylark', color = "Red")
print(c1)