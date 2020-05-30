n,m = map(int,input().split())
h = list(map(int,input().split()))
j = []
for i in range(m):
  j.append(list(map(int,input().split())))

num_ok = []
num_false = []
for i in range(m):
  if h[j[i][0] -1] > h[j[i][1] - 1]:
    num_ok.append(j[i][0])
  else:
    num_false.append(j[i][0])
for i in range(m):
  if h[j[i][1] - 1] > h[j[i][0] - 1]:
    num_ok.append(j[i][1])
  else:
    print(j[i][1])
    num_false.append(j[i][1])

set_num_ok = set(num_ok)
set_num_false = set(num_false)
count = 0

for i in range(1,n+1):
  if i not in set_num_ok and i not in set_num_false:
    count+=1
  else:
    continue
for num in set_num_ok:
  if num in set_num_false:
    continue
  else:
    count+=1
print(count)