arr = list(map(str, input().split()))
s = input()
count = 0

for i in arr:
    if s[:len(i)] == i:
        count += 1

print(count)
