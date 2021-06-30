# Everything in python is object
# self is the object which you are passing
# self points to object

class Computer:
    def config(self):
        print('i5,1tb,16gb')

# a='xyz'
# print(type(a))  => <class 'str'>

# b=85
# print(type(b))  => <class 'int'>

com1= Computer()
com2= Computer()
#print(type(com1))  => <class '__main__.Computer'>

# 1st Method to call methods
Computer.config(com1)
Computer.config(com2) # Here we are passing com2 object as self

# 2nd Method to call methods
com1.config()
com2.config()

# Here com1 is the object which is given as self to config()

# OUTPUT
# i5,1tb,16gb
# i5,1tb,16gb
# i5,1tb,16gb
# i5,1tb,16gb