i=int(input("i= "))
j=int(input("j= "))

max_n=1

for n in range(i,j+1):
    c=1
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        c+=1
    max_n=max(max_n,c)
print(i,j,max_n)
