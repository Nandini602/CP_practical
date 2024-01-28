
def remove(num , k): 
    stack = [] 
    for i in num: 
        while stack and k>0 and stack[-1]: 
            stack.pop() 
            k -=1  

    stack.append(i) 

    if k>0:
        stack = stack[ : -k] 

    return ".join(stack).lstrip('0')or'0' 

num,k = map(int,input().split()) 
res = remove(num,k)
print(res)