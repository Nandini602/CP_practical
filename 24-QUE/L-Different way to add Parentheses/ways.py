
def diffWay(exp):
    if exp.isdigit():
        return [int(exp)]

    ans = []
    for i in range(0,len(exp)):
        if exp[i] in '+-*':
            left = diffWay(exp[:i])
            right = diffWay(exp[i+1:])
            for a in left:
                for b in right:
                    if exp[i] == '+':
                        ans.append(a + b)
                    elif exp[i] == '-':
                        ans.append(a - b)
                    elif exp[i] == '*':
                        ans.append(a * b)

    return ans
exp = input()
result = diffWay(exp)
print( result)
