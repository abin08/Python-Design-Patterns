class Borg:
    """The Borg design pattern"""

    _shared_data = {} # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data # Make an Attribute Dictionary


class Singleton(Borg):
    """The Singleton Class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data) # Returns the attribute dictionary for printing
    

# Let's create a singleton object and our first acronym
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)

# Let's create another Singleton object and see
# if it refers to the same attribute dictionary
# by adding another acronym
y = Singleton(SNMP = "Simple Network Management Protocol") 
# The Attribute Dictionary will retain the previous acronym 
# and will add this new acronym to it
print(y)