# n=int(input("Enter the number of array input"))
# li=[]
# li = list(map(int,input().split()))


# ans= []
# ans2 = set()
# for i in range(n-2):
#     for j in range(i,n-1):
#         for k in range(j,n):
#             if li[i]+li[j]+li[k]==0:
#                 ans2.add(tuple(sorted(li[i],li[j],li[k])))
                
# print(ans2)
                # print("Triplet is :",li[i],li[j],li[k])


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, n-1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result
    
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))




