nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
red,white,blue=0,0,0
for i in nums:
    if i==0:
        red+=1
    elif i==1:
        white+=1
    else:
        blue+=1
print("0 "*red+"1 "*white+"2 "*blue)