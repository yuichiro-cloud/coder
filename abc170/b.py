x,y = map(int,input().split())

if 4*x >= y and 2*x <= y and y%2==0:
  print('Yes')
else:
  print('No')