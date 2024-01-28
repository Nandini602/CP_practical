
arr = list(map(str,input().split()))
k = int(input())
current =0
dict={}
flag =0
for i in arr:
    if i in dict:
        dict[i] +=1
    else:
        dict[i]=1
for i in arr:
    if dict[i]>1:
        continue 
    current = current+1
    if(current==k):
        flag=1
        print(i)
        break

if flag==0:
    print('" " ')



