a,b,c,k = map(int,input().split())

ans = 0
if a >= k:
  ans = k
  print(ans)
elif a + b >= k:
  ans = a
  print(ans)
else :
  ans = a + (-1)*(k - a - b)
  print(ans)

# min(a,k)