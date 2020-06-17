s = list(input())

length_s = len(s)
print(length_s)
s_first = s[:length_s//2]
s_last = s[length_s//2 + 1:]

# print(s[:length_s//2])
# print(s[length_s//2 + 1:])
rev_last = s_last.reverse()
if s_first == s_last:
  print('Yes')
else:
  print('No')
