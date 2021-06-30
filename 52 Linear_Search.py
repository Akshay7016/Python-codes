pos=-1

def search(list,n):

    i=0

    while (i<len(list)):
        if(list[i]==n):
            globals() ['pos'] = i
            return True

        i=i+1

    return False




list=[3,5,9,7,6,4]
n=int(input("Enter value to be searched: "))

if search(list,n):
    print("Found at: ",pos+1)
else:
    print("Not Found!!!!")

# Enter value to be searched: 6
# Found at:  5