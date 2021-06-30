class A:
    def feature1(self):
        print("Feature 1 working....")

    def feature2(self):
        print("Feature 2 working....")

# class B inherites the feature of A
class B(A):
    def feature3(self):
        print("Feature 3 working....")

    def feature4(self):
        print("Feature 4 working....")

#class c inherits features of A and B so features of A and B are accessible from C
class C(B):
    def feature5(self):
        print("Feature 5 working....")

a1=A()
a1.feature1()
print("**********************************************************************")
b1=B()
b1.feature1()
b1.feature3()
print("**********************************************************************")
c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
print("**********************************************************************")

# Feature 1 working....
# **********************************************************************
# Feature 1 working....
# Feature 3 working....
# **********************************************************************
# Feature 1 working....
# Feature 2 working....
# Feature 3 working....
# Feature 4 working....
# Feature 5 working....
# **********************************************************************