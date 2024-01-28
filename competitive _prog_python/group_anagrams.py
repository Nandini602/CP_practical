def group_anagrams(words):
    anagrams = {}
 
    for word in words:
        word_sort=" ".join(sorted(word))
        if word_sort in anagrams:
            anagrams[word_sort].append(word)
        else:
            anagrams[word_sort] = [word]
 
    # Return the groups of anagrams as a list of lists
    return list(anagrams.values())
 
# Example usage
words = ["eat","tea","tan","ate","nat","bat"]
print("The original list : {}".format(words))
print("The grouped Anagrams : {}".format(group_anagrams(words)))