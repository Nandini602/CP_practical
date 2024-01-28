def kthDistinctString(arr, k):
    distinct_count = 0

    for string in arr:
        if arr.count(string) == 1:
            distinct_count += 1
            if distinct_count == k:
                return string
    
    return ""  # kth distinct string not found

# Test the function
arr = ["d", "b", "c", "b", "c", "a"]
k = 2
result = kthDistinctString(arr, k)
print(result)  # Output: "a"
