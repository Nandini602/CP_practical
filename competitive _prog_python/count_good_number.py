def countGoodNumbers(n: int) -> int:
    mod = 10**9 + 7

    # Recursive helper function
    def countGoodNumbersHelper(length: int, isEven: bool) -> int:
        # Base case: when the length becomes 0
        if length == 0:
            return 1

        # For even indices, count the number of good digit strings with even digits
        if isEven:
            return (5 * countGoodNumbersHelper(length - 1, False)) % mod

        # For odd indices, count the number of good digit strings with prime odd digits
        else:
            return (4 * countGoodNumbersHelper(length - 1, True)) % mod

    return countGoodNumbersHelper(n, True)

n = 1
result = countGoodNumbers(n)
print(result)
