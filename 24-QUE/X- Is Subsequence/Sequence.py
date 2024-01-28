def isSubsequence(s,t):
    n=len(s)
    m=len(t)
    i=0
    j=0
    while i<n and j<m:
        if s[i]!=t[j]:
            j=j+1
        else:
            i=i+1
            j=j+1
    if i==n:
        return True
    return False

        
s=input()
t=input()
print(isSubsequence(s,t))