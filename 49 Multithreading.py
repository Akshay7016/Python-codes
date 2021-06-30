# By default "main" thread is called
# sleep is used bcz system executes it fast so for viewing execution we use sleep()



from threading import *
from time import sleep

class Hello(Thread):   # Hello is subclass of Thread
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


t1=Hello()
t2=Hi()

t1.start()   # start() is used for multithreading and in background run() method is called 
sleep(0.2)
t2.start()


t1.join()  # after thread t1 completion "main" thread excuted
t2.join()  # after thread t2 completion "main" thread excuted

print("Bye")  # this statement is printed by "main" thread
 


# Hello
# hi
# Hello
# hi
# Hello
# hi
# Hello
# hi
# Hello
# hi
# Bye