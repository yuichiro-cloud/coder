m,n,k = map(int,input().split())

k_box = []
for i in range(k):
  k_box.append(int(input()))
remain = n
l = [0]*m
# print(l)
for i in range(k):
  for index in range(m):
    if l[index] != 0:
      l[index]-=1
      l[k_box[i]-1]+=1
  if remain != 0:
    remain-=1
    l[k_box[i]-1]+=1

for i in [i for i, x in enumerate(l) if x == max(l)]:
  print(i+1)