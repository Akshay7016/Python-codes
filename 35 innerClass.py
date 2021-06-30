# We create object of inner class in outer class
class Student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()  #object of inner class

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
                self.brand='HP'
                self.pro = 'i5'
                self.ram=16

        def show(self):
            print(self.brand, self.pro, self.ram)


s1=Student("AKshay",20)
s2=Student("Ram",58)

s1.show()
s2.show()

# lap1 = s1.lap  # object of inner class
# lap2 = s2.lap
# lap3 = Student.Laptop()
# lap3.show()


#OUTPUT
# AKshay 20
# HP i5 16
# Ram 58
# HP i5 16

