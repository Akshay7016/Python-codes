# Iterator iterates one element at a time
# it gives one value at a time but not repeat that value
# iter() will give object of iterator
# next() gives next object

nums=[5,6,9,8]

it = iter(nums)
print(it.__next__())  # => 5
print(it.__next__())  # => 6

print(next(it))

for i in nums:
    print(i)


# 5
# 6
# 9
# 5
# 6 
# 9
# 8