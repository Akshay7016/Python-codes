# two classes have same methods thats overrides
# If subclass doesnt have method then it will call superclass method

class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self): # these show() overrides earlier show() method
        print("In B show")

b1=B()
b1.show()

# In B show