import math

def findGCD(nums):
    # Find the smallest and largest numbers in the array
    smallest = min(nums)
    largest = max(nums)

    # Calculate the GCD using the Euclidean algorithm
    gcd = math.gcd(smallest, largest)

    return gcd

# Example usage
nums = [2, 5, 6, 9, 10]
result = findGCD(nums)
print(result)  # Output: 2
