# copy image to myphoto.txt file

f= open("akshay.jpg",'rb')  # rb= read binary because image are in binary format

f1 = open("myphoto.jpg",'wb') # wb = write binary
for i in f:
    f1.write(i)