from numpy import *

arr = array([1,2,3],int)
print(arr.dtype)
print(arr)
# int32
# [1 2 3]

arr1=array([1,2,3,4],float)
print(arr1.dtype)
print(arr1)
# float64
# [1. 2. 3. 4.]

print("**************************************")
#linespace()

arr2=linspace(1,15,18)  # here 18 is parts in which range divides
print(arr2)
# [ 1.          1.82352941  2.64705882  3.47058824  4.29411765  5.11764706
#   5.94117647  6.76470588  7.58823529  8.41176471  9.23529412 10.05882353
#  10.88235294 11.70588235 12.52941176 13.35294118 14.17647059 15.        ]

print("**************************************")
#arange()
arr3= arange(1,15,2)
print(arr3)
# [ 1  3  5  7  9 11 13]

print("**************************************")
#logspace()
arr4 = logspace(1,40,5)
print(arr4)
# [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30
#  1.00000000e+40]
print("%.2f"%arr4[0])
#10.00

print("**************************************")
#zeros()
arr5 = zeros(5)     # By default float values
print(arr5)
# [0. 0. 0. 0. 0.]=float
arr6=zeros(5,int)
print(arr6)
# [0 0 0 0 0]=int

print("**************************************")
arr7= ones(5)
print(arr7)
# [1. 1. 1. 1. 1.]