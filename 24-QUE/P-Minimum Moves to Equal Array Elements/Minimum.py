
nums = list(map(int,input().split())) 
nums.sort() 
mid = nums[len(nums)//2] 
res =0
for i in nums: 
    res += abs(mid-i) 
print(res)