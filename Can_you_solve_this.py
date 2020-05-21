(n,m,c) = list(map(int,input().split()))
b = list(map(int,input().split()))
a = []
for i in range(n):
  a.append(list(map(int,input().split())))

ans = 0
count = 0
for i in range(n):
  for index in range(m):
    ans += a[i][index]*b[index]
  if ans + c > 0:
    count += 1
  else:
    next
  ans = 0
print(count)
