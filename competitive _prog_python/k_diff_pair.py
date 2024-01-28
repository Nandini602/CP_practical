def findPairs(nums, k):
    pairs = set()
    seen = set()

    for num in nums:
        if num - k in seen:
            pairs.add((num - k, num))
        if num + k in seen:
            pairs.add((num, num + k))
        seen.add(num)

    return len(pairs)

nums = [3, 1, 4, 1, 5]
k = 2
print(findPairs(nums, k))
