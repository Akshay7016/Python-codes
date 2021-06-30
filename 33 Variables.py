#1.Class Variable => If changes it will change for all objects
#2.Instance Variable

class Car:

    wheels=4  # Class variable(Static variable)

    def __init__(self):
        self.com="BMW"    #Instance variable
        self.mil=10

c1=Car()
c2=Car()

Car.wheels=8  # wheels is a class variable so we need class name to change it

print(c1.com,c1.mil,Car.wheels)
print(c2.com,c2.mil,c2.wheels)

# BMW 10 8
# BMW 10 8