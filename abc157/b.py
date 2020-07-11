a = []

for i in range(3):
  a.append(list(map(int,input().split())))
n = int(input())
b = []
for i in range(n):
  b.append(int(input()))

for b1 in b:
  for a1 in a:
    if b1 in a1:
      a1[a1.index(b1)] = 0
aa = [[a[0][0],a[1][0],a[2][0]],[a[0][1],a[1][1],a[2][1]],[a[0][2],a[1][2],a[2][2]]]

if a[0].count(0) == 3 or a[1].count(0) == 3 or a[2].count(0) == 3 or aa[0].count(0) == 3 or aa[1].count(0) == 3 or aa[2].count(0) == 3 or a[0][0] == a[1][1] == a[2][2] == 0 or a[0][2] == a[1][1] == a[2][0] == 0:
  print('Yes')
else:
  print('No')