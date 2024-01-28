
word = input()
ch = input() 
if ch in word: 
    i = word.index(ch) 
    word = word[i: -1] + word[i+1: ] 
print(word)