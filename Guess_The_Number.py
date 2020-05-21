(n,m) = list(map(int,input().split()))

sc = []
# c = []
for i in range(m):
  (sc1) = list(map(int,input().split()))
  sc.append(sc1)
print(sc)
sc_box = []
# print(s_box)
for i in range(m):
  if sc[i][0] == 1 and sc[i][1] == 0:
    print('-1')
    exit
  elif bool([s for s in sc_box if s.startswith(sc[i][0])]) and [s for s in sc_box if s.startswith(sc[i][0])] != sc[i]:
    print('-1')
    exit
  else:
    next
  sc_box.append(sc[i])

  print(sc_box)


#sc[i][0]でscのなかのi番目のsを表せる