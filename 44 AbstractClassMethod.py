# In python Abstract claases and methods does not support bydefault
# The method which has declaration only not definition is called as abstract method
# the class in which abstract mrthods are present are called as abstract classes
# we cant create object of abstract class

#abc = abstract base class

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("Its running in Laptop")

class Desktop(Computer):
    def process(self):
        print("Its running in Desktop")


class Programmer:
    def work(self,other):
        print("Solving problems")
        other.process()
        other.process


lap = Laptop()
lap.process()

des=Desktop()
des.process()


pro=Programmer()
pro.work(lap)
pro.work(des)


# Its running in Laptop
# Its running in Desktop
# Solving problems
# Its running in Laptop
# Solving problems
# Its running in Desktop