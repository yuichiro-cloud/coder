# (n,m) = list(map(int,input().split()))

# sc = []
# # c = []
# for i in range(m):
#   (sc1) = list(map(int,input().split()))
#   sc.append(sc1)
# print(sc)
# sc_box = []
# # print(s_box)
# for i in range(m):
#   if sc[i][0] == 1 and sc[i][1] == 0:
#     print('-1')
#     exit
#   elif bool([s for s in sc_box if s.startswith(sc[i][0])]) and [s for s in sc_box if s.startswith(sc[i][0])] != sc[i]:
#     print('-1')
#     exit
#   else:
#     next
#   sc_box.append(sc[i])

#   print(sc_box)


#sc[i][0]でscのなかのi番目のsを表せる

N,M = map(int,input().split())
o = {}
if N==1 and M==0:
  print(0)
else:
  for i in range(M):
    print(o)
    s,c = map(int,input().split())
    if o.get(s,-1)==-1:
        o[s]=c
    elif o.get(s,-1)!=-1 and o[s]!=c:
        print(-1)
        break
  else:
    m = [1]+[0]*(N-1)
    for k in o.keys():
        m[k-1]=o[k]
    if N!=1 and m[0]==0:
      print(-1)
    else:
      print(''.join([str(a) for a in m]))
