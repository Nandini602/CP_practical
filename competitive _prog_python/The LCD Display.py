print("Enter dash and no")
dash,no = map(int,input().split())
ans = []
no = str(no)
def s1(n,no,ans):
    s1str=''
    for i in no:
        if i in '1':
            s1str = s1str + ' ' + ' '
        elif i in '02356789':
            s1str = s1str + ' ' + '-'*n + ' ' + ' '
        elif i in '4':
            s1str = s1str + ' ' + ' '*n + ' ' + ' '
    ans.append(s1str)
def s2(n,no,ans):
    for i in range(n):
        s2str=''
        for i in no:
            if i in '0489':
                s2str = s2str + '|' + ' '*(n) + '|' + ' '
            elif i in '1':
                s2str = s2str + '|' + ' '
            elif i in '237':
                s2str = s2str + ' '*(n+1) + '|' + ' '
            elif i in '56':
                s2str = s2str + '|' + ' '*(n) + ' ' + ' '
        ans.append(s2str)
def s3(n,no,ans):
    s3str=''
    for i in no:
        if i in '1':
            s3str = s3str + ' ' + ' '
        elif i in '2345689':
            s3str = s3str + ' ' + '-'*n + ' ' + ' '
        elif i in '07':
            s3str = s3str + ' '*(n+1) + ' ' + ' '
    ans.append(s3str)
def s4(n,no,ans):
    for i in range(n):
        s4str=''
        for i in no:
            if i in '068':
                s4str = s4str + '|' + ' '*(n) + '|' + ' '
            elif i in '1':
                s4str = s4str + '|' + ' '
            elif i in '34579':
                s4str = s4str + ' '*(n+1)+ '|'  + ' '
            elif i in '2':
                s4str = s4str + '|' + ' '*(n) + ' ' + ' '
        ans.append(s4str)
def s5(n,no,ans):
    s5str = ''
    for i in no:
        if i in '1':
            s5str = s5str + ' ' + ' '
        elif i in '0235689':
            s5str = s5str + ' ' + '-' * n + ' ' + ' '
        elif i in '47':
            s5str = s5str + ' ' + ' ' * n + ' ' + ' '
    ans.append(s5str)
s1(dash,no,ans)
s2(dash,no,ans)
s3(dash,no,ans)
s4(dash,no,ans)
s5(dash,no,ans)
for i in ans:
    print(i)
#2 12345
 # __     __  __        __   __ __   __   __
# |  | |    |   | |  | |    |     | |  | |  |
# |  | |    |   | |  | |    |     | |  | |  |
#         __  __   __   __   __      __   __
# |  | | |      |    |    | |  |  | |  |    |
# |  | | |      |    |    | |  |  | |  |    |
#  --      __  __        __  __      __   __