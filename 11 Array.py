from array import *

arr = array('i',[2,3,4,5,6])

newArray = array(arr.typecode, (a for a in arr))    #copy of array
#typecode is used to get the type of array
#We use loop to access the elements of array

for i in arr:
    print(i)

print("***************************************")
for i in range(len(arr)):    #range(5)
    print(arr[i])

print("***************************************")
for j in newArray:
    print(j)


print("***************************************")
#Copy of array with values as square
newArray1 = array(arr.typecode, (a*a for a in arr))
for k in newArray1:
    print(k)