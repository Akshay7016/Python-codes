#print the first no. which is divisible of 5
nums=[11,24,30,14,38]

for i in nums:
    if(i%5==0):
        print(i)
        break
else:
    print("Not found")
