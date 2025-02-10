"""
One to many relations
Problem:
    > Subject needs to be monitored
    > Observers to be notified when there is a change in the subject
Solution:
    > Subject - An abstract class with following operations
        > Attach
        > Detach
        > Notify
    > Concrete subject classes inheriting from the abstract Subject class
    Singleton is related to the observer design pattern

Example:
    Keeping track of the Core temperatures of reactors at a Nuclear power plant.
    When there is a change in the Core temp, the registered observers must be notified
"""

class Subject(object):  # Represents what is being 'observed'

    def __init__(self):
        self._observers = []    # This represents all the observers
                                # Note that this is a one-to-many relationship

    def attach(self, observer):
        # if the observer is not already present in the
        # observers list then append it to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if observer != modifier:    # Don't notify the observer who is actually modifying the values
                observer.update(self)   # Alert the observers


class Core(Subject):    # Inherits from the subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name   # set the name of the Core
        self._temp = 0  # Initialize the temperature of the core

    @property   # Getter that gets the temperature of the Core
    def temp(self):
        return self._temp
    
    @property
    def name(self):
        return self._name
    
    @temp.setter    # Setter that sets the temperature of the Core
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the Core temperature
        self.notify()


class TempViewer:   # The observer class

    def update(self, subject):
        """Alert method that gets invoked when 
        the temperature value changes
        """
        print(f"Temperature viewer: {subject.name} has Temperature {subject.temp}")


# Lets create our subjects
c1 = Core("Core_1")
c2 = Core("Core_2")

# Lets create our observers
v1 = TempViewer()
v2 = TempViewer()

# Lets attach observers to the first core
c1.attach(v1)
c1.attach(v2)

# Lets change the temperature of the first core
c1.temp = 100
c1.temp = 200
