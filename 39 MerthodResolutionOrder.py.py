class A:
    def __init__(self):
        print("In A init")
    
    def feature1(self):
        print("Feature 1=>A working....")

    def feature2(self):
        print("Feature 2 working....")


class B:
    def __init__(self):
        print("In B init")
    

    def feature1(self):
        print("Feature 1=>B working....")

    def feature4(self):
        print("Feature 4 working....")

# IF we create object of C then it will call init method of class c first
# If we call init method by super(). then it will call init of leftmost class 
# class A and B has same methods name then by by calling object of C it will call leftmost
 # class method

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")
    
    # We can call method of parent class by super() method
    def feat(self):
        super().feature4()
    


c1=C()

c1.feature1()
c1.feat()

# In A init
# In C init
# Feature 1=>A working....
# Feature 4 working....