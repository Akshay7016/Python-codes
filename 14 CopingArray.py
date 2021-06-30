from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([3,5,7,9,6])
arr3=arr1+arr2
print(arr3)
# [ 4  7 10 13 11]
arr5 = concatenate([arr1,arr2])
print("Arr5: ",arr5)

arr4=array([1,5,9,6,7])
print(sin(arr4))
print(cos(arr4))
print(log(arr4))
print(sqrt(arr4))
print(min(arr4))
print(max(arr4))
print(sum(arr4))

print("***************************************************************")
#copy array

arr6 = array([5,8,6,9])
arr7 = arr6 # aliasing  = Same address

arr8 = arr6.view()   #Shallow copy - means dependent on each other as value changes

arr9 = arr6.copy()   #Deep copy - means not dependent on each other as cant cant changes value

print(arr6)
print(arr7)
print(arr8)
print(arr9)

print(id(arr6))
print(id(arr7))
print(id(arr8))
print(id(arr9))

# [5 8 6 9]
# [5 8 6 9]
# [5 8 6 9]
# [5 8 6 9]
# 21302792
# 21302792
# 196079432
# 196079392

