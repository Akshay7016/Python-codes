def fib(n):

    a=0
    b=1

    if n==1:
        print(a)
    elif(n<=0):
        print("Wrong Input!!!!")
    else:
        print(a)
        print(b)
        for i in range (2,n):
            c=a+b
            a=b
            b=c
            print(c)

# x=int(input("Enter a number: "))
x=5
fib(x)