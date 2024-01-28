def restoreIpAddresses(s):
    def backtrack(s, start, parts, current, result):
        if start == len(s) and parts == 4:  # Found a valid IP address
            result.append('.'.join(current))
            return
        
        if parts == 4 or start == len(s):  # Invalid IP address
            return
        
        for i in range(1, 4):  # Try different lengths for the current part
            if start + i > len(s):
                break
            
            segment = s[start:start+i]
            
            # Check if the segment is a valid integer
            if int(segment) > 255 or (segment[0] == '0' and len(segment) > 1):
                break
            
            current.append(segment)
            backtrack(s, start+i, parts+1, current, result)
            current.pop()
    
    result = []
    backtrack(s, 0, 0, [], result)
    return result
s = "25525511135"
print(restoreIpAddresses(s))