n,m = map(int,input().split())
l = []
for i in range(n):
  l.append(int(input()))

kinds = list(range(1,m+1))
count=1
for i in range(n):
  if l[i] in kinds:
    kinds.remove(l[i])
  if not kinds:
    continue
  count+=1
if kinds:
  print('unlucky')
else:
  print(count)
