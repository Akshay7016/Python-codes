# count no. of even and odd nos

def check(lst):
    even=0
    odd=0
    for i in lst:
        if(i%2==0):
            even+=1
        
        else:
            odd+=1

    return even,odd


lst=[10,25,3,6,94,45,6,89,65,23]
even,odd = check(lst)

print("Even: {} and Odd: {}".format(even,odd))
#Even: 4 and Odd: 6


#count the names which has length greater than 5 
def checkNames(names):
    count=0
    for i in names:
        if len(i)>5:
            count+=1

    return count

names=['akshay','Ram','Amey','Kunal','Rushikesh']
count = checkNames(names)
print(count)