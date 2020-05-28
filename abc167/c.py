import itertools
n,m,x = map(int,input().split())

l = ['0']*n + ['1']*n

ca = []
for i in range(n):
  ca.append(list(map(int,input().split()))) 
p = itertools.permutations(l,n)
box = []
for v in p:
  box.append(''.join(v))

box = set(box)

cost = []
arg = []
for b in box:
  arg1 = []
  cost1 = []
  while min(arg1)<=x or not arg1:
    for i in range(n):
      if b[i] == '0':
        continue
      else:
        cost1+=ca[i][0]
        arg1.append(ca[i][i+1])
  arg.append(arg1)
  cost.append(cost1)
  arg1 = []
  cost1 = []

print(arg)
print(cost)


