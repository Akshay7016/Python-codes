#Formal parameter = func definition
#Actual parameter = func calling
    #1.Positional
    #2. Default
    #3. Variable length
    #4. Keyword

#positional
def person(name, age):
    print(name)
    print(age)
person('ram',25)   #positional
person(age=28,name='akshay')   #keyword

#Default
def person(name, age=20):
    print(name)
    print(age)

person('akshay') #if we pass age here then it override existing

#variable length
def sum(a,*b):  #a takes 1st agrument and b takes tuple
    #print(a) = 2
    #print(b) = (3, 6, 8, 9)

    c=a
    for i in b:
        c=c+i   #Tuple cant add in int

    print(c)

sum(2,3,6,8,9)   #a=2 and b=(3,6,8,9)

#output: 28

print("************************************************")
def add(*b):

    c=0
    for i in b:
        c=c+i

    print(c)

add(2,3,6,8,9)   
#output: 28