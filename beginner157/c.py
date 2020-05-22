n,m = list(map(int,input().split()))

sc = []
for i in range(m):
  sc.append(int(input().replace(' ','')))

sc1 = []
sc2 = []
sc3 = []


if m==0:
  print(0)
else:

  for i in range(m):
    if (int(str(sc[i])[-2]) == 1 and (not sc1 or sc[i] in sc1)) and int(str(sc[i])[-1]) == 0:
      sc1.append(sc[i])
    elif int(str(sc[i])[-2]) == 2 and sc[i] not in sc2:
      sc2.append(sc[i])
    elif int(str(sc[i])[-2]) == 3 and not sc3 or sc[i] in sc3:
      sc3.append(sc[i])
    else:
      print(-1)

# if not sc1:
#   sc1 = range(10)
# else:
#   next
print(sc1)
  


