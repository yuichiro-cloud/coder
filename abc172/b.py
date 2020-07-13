s = list(input())
t = list(input())

dif_count = 0
for i in range(len(s)):
  if s[i] != t[i]:
    dif_count+=1
print(dif_count)

