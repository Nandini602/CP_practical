
def permutation(nums):
    if len(nums) ==0:
        return[] 
    if len(nums) ==1: 
        return[nums] 
    res =[] 

    for i in range(len(nums)): 
        x = nums[i] 
        rem = nums[ :i] + nums[i+1:]
        for y in permutation(rem): 
            res.append([x] +y) 
    return res 


nums = list(map(int,input().split())) 
print(permutation(nums))

