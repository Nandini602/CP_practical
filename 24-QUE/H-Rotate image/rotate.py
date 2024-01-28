
l= input()
y = l.split(',')
arr=[]

for ele in y:
    elements = ele.split()
    arr.append([e for e in elements])

row = len(arr)
n = len(arr[0])

for i in range(0,n):

    for j in range(0,i):
        temp1 = arr[i][j]
        arr[i][j]=arr[j][i]
        arr[j][i]=temp1


for i in range(0,row):
    start =0
    end =n-1
    while(start<end):
        temp = arr[i][start]
        arr[i][start]=arr[i][end]
        arr[i][end]=temp
        start = start+1
        end = end-1


print(arr)


