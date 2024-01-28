def permute(arr):
    n = len(arr)
    result = [arr[:]]
    while True:
        i = n - 2
        # Find the first element that is less than the element to its right
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        if i < 0:
            break  # No more permutations
        j = n - 1
        # Find the first element that is greater than the pivot
        while arr[j] <= arr[i]:
            j -= 1
        # Swap the pivot and the greater element
        arr[i], arr[j] = arr[j], arr[i]
        # Reverse the suffix
        arr[i+1:] = arr[i+1:][::-1]
        # Add the new permutation to the result
        result.append(arr[:])
    return result


a = int(input("Enter the size of the array: "))
arr = []
for i in range(a):
    num = int(input("Enter element {}: ".format(i)))
    arr.append(num)
permutations = permute(arr)
print(permutations)