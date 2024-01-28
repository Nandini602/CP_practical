class PrefixCount:
    
    def count_prefixes(words, s):
        count = 0
        for word in words:
            if s.startswith(word):
                count += 1
        return count

# Example usage
words = ["a", "b", "c", "ab", "bc", "abc"]
s = "abc"
result = PrefixCount.count_prefixes(words, s)
print( result)
