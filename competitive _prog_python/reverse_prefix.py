def reverse_prefix(word, ch):
    if ch not in word:
        return word

    ch_index = word.index(ch)
    reversed_segment = word[:ch_index + 1][::-1]
    return reversed_segment + word[ch_index + 1:]
word = "abcdefd"
ch = "d"
result = reverse_prefix(word, ch)
print(result)
