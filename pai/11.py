n,m = map(int,input().split())

a = []
for i in range(n):
  a.append(list(map(int,input().split())))

goukaku_a = []

for i in range(n):
  if a[i][0] - a[i][1]*5 < 0:
    goukaku_a.append(0)
  else:
    goukaku_a.append(a[i][0] - a[i][1]*5)
number = 1
for i in goukaku_a:
  if i >= m:
    print(number)
  number+=1