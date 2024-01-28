words = list(map(str,input().split()))

n = len(words)
result =0
for i in range(0,n):
    s1 = words[i]
    len1 = len(words[i])
    arr =[]
    for c in s1:
        if c not in arr:
            arr.append(c)
    for j in range(i+1,n):
        s2 = words[j]
        len2= len(words[j])
        flag =0
        for k in range(len(s2)):
            if(s2[k] in arr):
                flag =1
                break
        if(flag==0):
            result = max(result,len1*len2)
print(result)

