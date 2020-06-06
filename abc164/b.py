a,b,c,d = map(int,input().split())

a2 = a
c2 = c
while True:
  c2-=b
  if c2 <= 0:
    print('Yes')
    exit()
  a2-=d
  if a2 <= 0:
    print('No')
    exit()