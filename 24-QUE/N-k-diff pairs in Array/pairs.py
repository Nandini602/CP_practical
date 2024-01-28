

l = list(map(int,input().split()))
k = int(input())
count =0
length = len(l)
dict = {}
p=0
q=1
while(p<length and q<length):
    diff = l[p]-l[q]
    if(abs(diff)==k):
        if(l[p]>l[q]):
            x=l[p]
            y=l[q]
        else:
            x=l[q]
            y=l[p]
        dict[x]=y
    if q==length-1:
        p=p+1
        q=p+1
    else:
        q=q+1
print(len(dict))