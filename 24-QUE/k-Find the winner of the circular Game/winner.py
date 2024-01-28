
n,k = map(int,input().split()) 
arr = list(range(1,n+1)) 
start =0; 
while(len(arr)>1): 
    rem = (start + k ) -1 
    if rem<len(arr): 
        del arr[rem] 
        start = rem 
    else: 
        m = rem % len(arr) 
        del arr[m] 
        start = m 

print(arr[0])