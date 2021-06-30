def sort(nums):

    for i in range(len(nums)-1,0,-1):   # for iteration
        for j in range(i):              # for go till last value
             if nums[j] > nums[j+1]:
                 temp = nums[j]
                 nums[j] = nums[j+1]
                 nums[j+1] = temp





nums=[2,7,9,5,6,4]
sort(nums)

print(nums)