
count = 0
n = int(input())
for i in range(1, n + 1):
    s = input()
    if len(s) == 7:
        count = i
        break
 #   print(i, s, len(s), count)
print(count if count > 0 else 'НЕТ')