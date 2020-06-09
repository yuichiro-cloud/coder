import math
n,m = map(int,input().split())

a = []


a.append(list(map(int,input().split())))
q = int(input())

l = []

for i in range(q):
  l.append(list(map(int,input().split())))

for i in range(q):
  if sum(a[0][l[i][0]-1:l[i][1]])/(l[i][1]-l[i][0]+1) < m:
    dif = m - sum(a[0][l[i][0]-1:l[i][1]])/(l[i][1]-l[i][0]+1)
    dif = math.ceil(dif)
    for p in range(l[i][0],l[i][1]+1):
      a[0][p-1] += dif
ans = ''
for i in range(n):
  if i != n-1:
    ans+=f"{str(a[0][i])} "
  else:
    ans+=f"{str(a[0][i])}"
print(ans)

