
def group_Anagram(str): 
    d = {} 
    for i in str: 
        s =" ".join(sorted(i)) 
        if s in d: 
            d[s].append(i) 
        else: 
            d[s] =[i] 
    
    return d.values() 


str = list(map(str,input().split(" ")))
print(group_Anagram(str)) 