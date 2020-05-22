n,m = map(int,input().split())

if m==0:
  print(0)
  exit()

s = []
c = []
for i in range(m):
  sc = input().replace(' ','')
  s.append(int(sc[-2]))
  c.append(int(sc[-1]))

s1 = []
s2 = []
s3 = []
c1 = []
c2 = []
c3 = []
for i in range(m):
  if s[i] == 1 and not s1:
    s1.append(s[i])
    c1.append(c[i])
  elif s[i] == 1 and s1 and c[i] == c1[0]:
    next
  elif s[i] == 1 and s1 and c[i] != c1[0]:
    print(-1)
    exit()
  elif s[i] == 2 and not s2:
    s2.append(s[i])
    c2.append(c[i])
  elif s[i] == 2 and s2 and c[i] == c2[0]:
    next
  elif s[i] == 2 and s2 and c[i] != c2[0]:
    print(-1)
    exit()
  elif s[i] == 3 and not s3:
    s3.append(s[i])
    c3.append(c[i])
  elif s[i] == 3 and s3 and c[i] == c3[0]:
    next
  elif s[i] == 3 and s3 and c[i] != c3[0]:
    print(-1)
    exit()
ans = 0
if c1[0]==0:
  print(-1)
  exit()
elif not c1:
  next
else:
  ans+=c1[0]*100

if not c2:
  next
else:
  ans+=c2[0]*10

if not c3:
  next
else:
  ans+=c3[0]

print(ans)

  






