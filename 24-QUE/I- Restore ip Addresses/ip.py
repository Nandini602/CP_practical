
ip = input() 
res = " " 
for i in ip:
    if i =='.': 
        res += '[.]' 
    else: 
        res += i 

print(res)