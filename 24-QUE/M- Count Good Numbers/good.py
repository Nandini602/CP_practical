
n = int(input()) 
rem  = n%2 
n -= rem 
res = pow(20,n//2, 10**9 +7) 
if rem ==1:
    res +=5 
print(res% (10**9+7))