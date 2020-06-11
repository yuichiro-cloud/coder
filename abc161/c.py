n,k = map(int,input().split())

ans1 = n%k
ans2 = k - n%k

if ans1 > ans2:
  print(ans2)
else:
  print(ans1)



