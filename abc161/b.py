n,m = map(int,input().split())


a = list(map(int,input().split()))

a_sum = sum(a)
judge = a_sum/(4*m)

count = 0
for i2 in [i for i  in a if i >= judge]:
  count+=1

if count >= m:
  print('Yes')
else:
  print('No')





