from array import *
#Empty array
arr = array('i',[])   #i for type and [] for empty array   

n=int(input("Enter the length of array: "))

for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)

print(arr)


#Searching
#Manual method

a=int(input("Enter a no. to be searched"))
k=0  #Counter
for j in arr:
    if(j==a):
        print("Index is: ",k)
        break

    k+=1

# By Inbuilt Method
b=int(input("Enter a no. to be searched"))
print(arr.index(b))