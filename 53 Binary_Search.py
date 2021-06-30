# Elements should be in sorted
# If value in greater than mid then shift lower bound to mid
# If value is lesser than mid then shift upper bound to mid
# mid = (upper + lower) // 2

pos=-1

def search(list,n):

    lower=0
    upper=len(list)-1

    while lower <= upper:

        mid = (lower + upper) // 2

        if(list[mid]==n):
            globals()['pos']=mid
            return True
        else:
            if(list[mid] < n):
                lower = mid+1
            else:
                upper = mid-1

    return False



list = [10,20,35,48,68,75,98]   # list needs to be sorted
n=70
if search(list,n):
    print("Found at: ",pos+1)
else:
    print("Not Found!!!!!")