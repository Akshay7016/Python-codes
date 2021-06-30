from numpy import *

arr = array([
     [1,2,3,4,5,6],
     [5,6,7,8,9,10]

]
)

print(arr)
print(arr.ndim)   #2
print(arr.shape)  #(2,6)
print(arr.size)   #12

arr2 = arr.flatten()   #multi to one dimensional
print(arr2)
# [ 1  2  3  4  5  6  5  6  7  8  9 10]

arr3 = arr2.reshape(3,4)   # one dimesional to multidimensional
print(arr3)
# [[ 1  2  3  4]
#  [ 5  6  5  6]
#  [ 7  8  9 10]]

arr4 = arr2.reshape(2,2,3)   #2=two arrys  2=inside 2 array new 2 array  3=each two array contains 3 elements
print(arr4)
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 5  6  7]
#   [ 8  9 10]]]