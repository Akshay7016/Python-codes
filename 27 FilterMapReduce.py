from functools import reduce

# FInd out even and odd numbers


lst = [2,5,9,7,6,4,10,8]
# Filter()
evens = list(filter(lambda n:n%2==0,lst))
    # list is used because filter function gives sequence
    # filter(functionorNone, iterable) it takes two args and it filters values
    # we can use specific function but lambda is better
print(evens)

# Map() = To changes filtered values
doubles = list(map(lambda m:m+2,evens))
    # map(func, *iterables)
print(doubles)


# Reduce() = To reduce the value in single value eg.Average,sum
sum = reduce(lambda a,b:a+b,doubles)
    # reduce(function, sequence: Iterable[_S], initial: _T)
    # adds all values of doubles 
print(sum)


# [2, 6, 4, 10, 8]   = evens
# [4, 8, 6, 12, 10]  = doubles
# 40                 = sum


