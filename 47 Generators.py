# program to print square of top ten values using generator

# Generator gives Iterator
# yield is a keyword which converts your function as generator 
# yield is same as return but return terminate the loop but yield will not terminate loop

def topten():

    n=1

    while(n<=10):
        square = n*n
        yield square   #yield converts into generator
        n+=1


values = topten()

for i in values:
    print(i)


# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100