x,n = map(int,input().split())
p = list(map(int,input().split()))
ans = []
i = 1
if x not in p:
  print(x)
else:
  while len(ans)==0:
    if x+i not in p and x-i not in p:
      ans.append(x+i)
      ans.append(x-i)
    elif x+i not in p:
      ans.append(x+i)
    elif x-i not in p:
      ans.append(x-i)
    else:
      i+=1
  print(min(ans))
