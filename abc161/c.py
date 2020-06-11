n,k = map(int,input().split())

ans1 = n%abs(n-k)
ans2 = abs(n-k)%k

if ans1 > ans2:
  print(ans2)
else:
  print(ans1)



