a=10  #Global variable
print(id(a))

def something():
    # global a = global variable used in function but value of global var changes to 23
    a=23
     
    x = globals()['a'] #globals() returns all global variables & same address as of global var
    print(id(x))

    print("in function: ",a)   #local  var = we can use global var in function also


something()
print("Outside ",a)


# 1915541824
# 1915541824
# in function:  23
# Outside  10