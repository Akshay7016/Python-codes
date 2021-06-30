
f = open("Mydata.txt",'r')

#print(f.readline(),end="#")   #  read one line
#print(f.readline())
#print(f.read())       # read all lines and pointer starts from existing


f1 = open("abc.txt",'a')  # if open in write mode then data get lost 
 #if file is not present then it automatically created

#f1.write("My Laptop ")
#f1.write("is very good")

# copy contents of file mydata into abc
for data in f:
    f1.write(data)