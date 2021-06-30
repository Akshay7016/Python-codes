class Names:

    def __init__(self):
        self.name="akshay"
        self.age=20

    def update(self):
        self.age=36

    def compare(self,other): # self=c1 and other=c2
        if self.age==other.age:
            return True
        else:
            return False


c1 = Names()
c2 = Names()

c1.name = "Amey"  # Explicit changing
c1.age =  25

c1.update()

if c1.compare(c2):   # if we use c1==c2 then it compares addresses
    print("Age is Same")
else:
    print("Age is different")


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)


# Age is different
# Amey
# 36
# akshay
# 20