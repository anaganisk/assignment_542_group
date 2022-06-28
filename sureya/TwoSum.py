nums = [2,3,3,7]
target = 6
result = []
print(len(nums))
for i in range (len(nums)):
    j = i + 1
    while j<(len(nums)):
        if nums[i]+nums[j] == target :
            result = result + [i,j]
            print(result)
        j = j+1