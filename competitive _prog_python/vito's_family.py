for t in range(int(input("enter testcase "))):
    x = list(map(int, input().split()))
    avg = sum(x)/len(x)
    minn = float('inf')
    print(avg)
    mini = -1
    for i in range(len(x)):
        if abs(x[i]-avg) < minn:
            minn = abs(x[i]-avg)
            mini = i
    print(x[mini])
    