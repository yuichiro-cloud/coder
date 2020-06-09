n,m = map(int,input().split())

a = []

for i in range(m):
  a.append(list(map(int,input().split())))

l = [0]*n

ans = 0
for i in a:
  if i[1]+i[0] -1 < n:
    if 1 not in l[i[1]-1:i[0]+i[1]-1]:
      num = -1
      for p in range(i[0]):
        l[i[1]+num] = 1
        num+=1
        ans+=1
  else:
    if 1 not in l[i[1]-1:] and 1 not in l[:i[0] - (n - i[1]+1)]:
      for p in range(n - i[1]+1):
        l[i[1]-1] = 1
        ans+=1
      for p2 in range(i[0] - (n - i[1]+1)):
        l[p2-1] = 1
        ans+=1
print(ans)