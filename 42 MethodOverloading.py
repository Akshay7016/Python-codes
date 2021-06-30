# Method overloading bydefault doesnt support in python we perform in different way

class Overload:

    def __init__(self):
        self.m1=98
        self.m2=48

    #MEthod overloading
    def add(self,a=None, b=None ,c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a

        return s

obj = Overload()

print(obj.add(10,23))
print(obj.add(15,13,75))
print(obj.add(10))

# 33
# 103
# 10