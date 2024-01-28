def isSubsequence(s, t):
    i = 0  # Pointer for string s
    j = 0  # Pointer for string t
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1  # Advance pointer for s
        j += 1  # Always advance pointer for t
        
    # If we reached the end of s, it is a subsequence
    return i == len(s)
s1 = "abc"
t1 = "ahbgdc"
print(isSubsequence(s1, t1))  