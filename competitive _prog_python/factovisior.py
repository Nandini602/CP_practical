import math

def divides_factorial(n, m):
    factorial = math.factorial(n)
    if factorial % m == 0:
        return f"{m} divides {n}!"
    else:
        return f"{m} does not divide {n}!"

n,m=list(map(int,input("Enter n and m:- ").split()))
print(divides_factorial(n,m))
