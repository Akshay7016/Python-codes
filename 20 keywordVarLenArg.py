def person(name, **data):  # ** for multiple arguments with keyword
    print(name)
    #print(data) = it also works

    for i,j in data.items():
        print(i,j)

person('akshay',age=32,city='mumbai',mob=7040607016)

# akshay
# age 32
# city mumbai
# mob 7040607016