def fact(n):
    if(n==0):
        return 1

    return n*fact(n-1)



# x= int(input("Enter a no: "))
x=5
result= fact(x)
print(result)