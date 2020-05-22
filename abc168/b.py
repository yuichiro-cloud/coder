k = int(input())
s = input()
s_length = len(s)
if s_length <= k:
  print(s)
else:
  print(s[0:k]+('...'))
