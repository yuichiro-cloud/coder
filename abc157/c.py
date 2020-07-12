n,m = map(int,input().split())
sc = []
for i in range(m):
  sc.append(list(map(int,input().split())))

sc1 = []
sc2 = []
sc3 = []
for i in sc:
  if i[0]==1:
    sc1.append(i[1])
  elif i[0]==2:
    sc2.append(i[1])
  else:
    sc3.append(i[1])

if len(set(sc1)) > 1 or len(set(sc2)) > 1 or len(set(sc3)) > 1:
  print('-1')
  exit()
elif 0 in list((set(sc1))):
  print('-1')
  exit()


c1 = list(set(sc1))
c2 = list(set(sc2))
c3 = list(set(sc3))

if c1:
  c1_ans = c1[0]
else:
  c1_ans = 1
if c2:
  c2_ans = c2[0]
else:
  c2_ans = 0
if c3:
  c3_ans = c3[0]
else:
  c3_ans = 0

print(100*c1_ans + 100*c2_ans + c3_ans)
