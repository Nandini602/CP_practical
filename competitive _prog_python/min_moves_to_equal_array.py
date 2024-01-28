# nums=list(map(int,input("Enter the nums").split()))
# ans=sorted(nums)
# max=ans[-1]
# sol=1
# for i in range(len(nums)):
#     a=0
#     for i in range(len(nums) - 1):
#         a+= max - ans[i]
#     max=ans[len(nums)-(i)]
#     if sol<a:
#         ans1=sol
#     else:
#         ans1=a

# print(ans1)


def minMoves2(nums):
    nums.sort()
    left = 0
    right = len(nums) - 1
    moves = 0

    while left <= right:
        moves += abs(nums[right] - nums[left])
        left += 1
        right -= 1

    return moves


nums=[1,10,2,9]
minMoves2(nums)
print(minMoves2(nums))

