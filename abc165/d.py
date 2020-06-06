a,b,n = map(int,input().split())
ans = 0

for x in range(n+1):
  if a*x//b - a*(x//b) > ans:
    ans = a*x//b - a*(x//b)
print(ans)


