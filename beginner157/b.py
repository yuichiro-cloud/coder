a = list(map(int,input().split()))
a+=list(map(int,input().split()))
a+=list(map(int,input().split()))
n = int(input())
b = []
for i in range(n):
  b.append(int(input()))

for i in range(9):
  if a[i] in b:
    a[i] = 'x'
  else:
    next
if a[0]is a[1]is a[2] is 'x' or a[3]is a[4]is a[5]is 'x' or a[6]is a[7]is a[8]is 'x' or a[0]is a[3]is a[6]is 'x' or a[1]is a[4]is a[7]is 'x' or a[2]is a[5]is a[8]is 'x' or a[0]is a[4]is a[8]is 'x' or a[2]is a[4]is a[6]is 'x':
  print('Yes')
else:
  print('No')

