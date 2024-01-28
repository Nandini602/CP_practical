

def ispangram(s):
    alphabets ="abcdefghijklmnopqrstuvwxyz" 
    for i in alphabets: 
        if i not in s: 
            return False 
        
    return True 
s = input() 
print(ispangram(s))