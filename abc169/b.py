n = int(input())
a = list(map(int,input().split()))

seki = 1
if 0 in a:
  print(0)
else:

  for i in range(n):
    seki*=a[i]
    if seki > 10**18:
      break
  if seki > 10**18:
    print('-1')
  else:
    print(seki)