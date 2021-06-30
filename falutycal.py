

a= int(input("Enter a first operand"))
b=int(input("Enter a second operand"))
opr = input()

if(opr == "*"):
    if (a==45 and b==3):
        print("Multiplication is: 555")
    else:
        print(a * b)

elif(opr=="+"):
    if (a==56 and b==9):
        print("Addition is: 77")
    else:
        print(a + b)

else:
    if(a==56 and opr=="/" and b==6):
        print("Division is: 4")
    else:
        print(a/b)

