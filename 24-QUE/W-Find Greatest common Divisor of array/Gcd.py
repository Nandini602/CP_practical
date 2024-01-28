
def Gcd(l,s): 
    while(s):
        l,s  = s,l % s

    return abs(l)
    
nums = list(map(int, input("Enter elements: ").split())) 
print(arr)  
nums.sort()
s  = arr[0]
l = arr[-1 : : ] [0] 

print("smallest elements", s) 
print("largest element",l)

print("Gcd of elements is ", Gcd(s,l))