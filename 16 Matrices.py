from numpy import *

m = matrix('1,2,3;4,5,6;7,8,9')
print(m)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(diagonal(m))
#[1 5 9]

print(m.min())  #1

#multiplication
m1=matrix('2,6,8;4,8,3;1,7,3')
m2=m*m1
print(m2)
# [[ 13  43  23]
#  [ 34 106  65]
#  [ 55 169 107]]