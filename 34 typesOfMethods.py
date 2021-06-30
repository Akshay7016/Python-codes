#1. Instance methods => USe with instance variable
#2. Class methods => Use with class variable , def using @classmethod
#3. Static methods => Nothing to do with class and instance variable. Any activity
     #eg.factorial of no. bcz it does not need class and instance variable =>dont use self and cls

class student:

    school="Telusko"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):    # Instance method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):  #Getters =>Instance method
        return self.m1

    def set_m1(self,value):  #Setters => Instance method
        self.m1=value

    @classmethod   #Decorator
    def nameOfSchool(cls):   #Class method => use "cls"
        return cls.school

    @staticmethod
    def msg():    # static method
        print("Hey these is static method")

def info():   # Function
    print("Hiiiiiiiiiiii")


s1=student(15,68,65)
s2=student(42,18,68)

s1.set_m1(50)
print(s1.m1)

print(s1.avg())

#class methods
print(s1.nameOfSchool())  # using object
print(student.nameOfSchool()) # using classname

#static methods
student.msg()
s1.msg()

info()


#  50
# 61.0
# Telusko
# Telusko
# Hey these is static method
# Hey these is static method
# Hiiiiiiiiiiii       