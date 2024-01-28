ip = input()
s=''
for i in ip:
    if i =='.':
        s = s+'[.]'
    else:
        s = s+i
print(s)