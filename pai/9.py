n = int(input())
s_box = []
for i in range(n):
  s_box.append(list(map(str,input().split())))
var1 = 0
var2 = 0

for s in s_box:
  if s[0] == 'SET' and s[1] == '1':
    var1 = s[2]
  elif s[0] == 'SET' and s[1] == '2':
    var2 = s[2]
  elif s[0] == 'ADD':
    var2 = int(var1) + int(s[1])
  else:
    var2 = int(var1) - int(s[1])
print(f"{var1} {var2}")



