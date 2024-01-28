# word=list(map(str,input("Enter words ").split()))
# for i in range(len(word)-1):
#     for j in range(i+1,len(word)):
#         # if list(set[word[i]] & set[word[j]]):
#         #     pass
#         # else:
#         #     ans=len(word[i])*len(word[j])
#         set1=set(word[i])
#         set2=set(word[j])
#         if len(set1.intersection(set2))>0:
#             ans=0
#             pass
#         else:
#             ans=len(word[i])*len(word[j])

# print(ans)

# word=eval(input())
# ans=-1
# for i in word:
#     for j in word :
#         st=" ".join(set(i).intersection(j))
#         if len(st)==0:
#             ans=max(ans,len(st))
# print(ans)
word = input()
ans = -1  # Initialize ans to a negative value
for i in word:
    for j in word:
        st = " ".join(set(i).intersection(j))
        if len(st) > 0:
            ans = max(ans, len(st))

print(ans)
