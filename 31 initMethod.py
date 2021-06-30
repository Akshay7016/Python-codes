class Computer:

    # To declare attributes we use __init__ method and it is automatically called
    def __init__(self,processor,ram):  # self is referring to object
        self.processor=processor
        self.ram=ram
        

    def config(self):
        print("Processor is: ",self.processor,"RAM is: ", self.ram)
        # We use self. because each attribute is referring to object



com1=Computer("i5",16) # Here 3 arguments self is refer to onject itself
com2=Computer("AMD-7",8)

com1.config()
com2.config()

# Processor is:  i5 RAM is:  16
# Processor is:  AMD-7 RAM is:  8