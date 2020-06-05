a,b,n = map(int,input().split())
ans = []

for x in range(n+1):
  ans.append(a*x//b - a*(x//b))
print(max(ans))
