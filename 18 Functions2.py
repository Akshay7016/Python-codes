def update(x):
    print(id(x))

    x=8
    print(id(x))
    print("x ",x)

a=10
print(id(a))
update(a)
print("a ",a)

# 1915541824
# 1915541824
# 1915541792
# x  8
# a  10

print("*****************************************************************")

def update(lst):
    print(id(lst))

    lst[1]=25
    print(id(lst))
    print("x ",lst)

lst=[10,20,30]
print(id(lst))
update(lst)
print("lst ",lst)

# 9586128
# 9586128
# 9586128
# x  [10, 25, 30]
# lst  [10, 25, 30]