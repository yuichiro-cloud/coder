q = int(input())
n = []
for i in range(q):
  n.append(int(input()))

index = 1
s = []
for i in n:
  while index < i:
    if i%index == 0:
      s.append(index)
    index+=1
  if sum(s) == i:
    print('perfect')
  elif i - sum(s) == 1 or i - sum(s) == -1:
    print('nearly')
  else:
    print('neither')
  s = []
  index = 1