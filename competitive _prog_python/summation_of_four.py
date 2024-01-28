def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_four_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
            if len(primes) == 4:
                return primes
    return []

# Read input
while True:
    try:
        n = int(input())
        primes = find_four_primes(n)
        if primes:
            print(' '.join(str(p) for p in primes))
        else:
            print("Impossible.")
    except EOFError:
        break

