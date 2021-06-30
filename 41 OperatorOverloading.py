# Polymorphism => Operator Overloading
# Operator overloading takes palce when we perform operation on object of class
#  +  => __add__()
#  -  => __Sub__()
#  *  => __mul__()
#     => __str__()

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):  # Method Overloading , self=s1 and other=s2
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3=Student(m1,m2)
        return s3

    def __gt__(self,other):   #gt=greater than  , ge=greater than or equal
        r1=self.m1 + self.m2
        r2=other.m1+other.m2

        if r1 > r2:
            return True
        else:
            return False

    # def __str__(self):
    #     return self.m1,self.m2   => gives tuple as output

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1=Student(65,47)
s2=Student(54,89)

s3 = s1 + s2   # => Student.__add__(s1,s2)
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a=9
print(a.__str__())   # __str__() prints the value

print(s1.__str__()) 
# Here it prints address but we need value so we use operator overloading
# by overloading it prints value

print(s1)


# 119
# 136
# s2 wins
# 9
# 65 47
# 65 47