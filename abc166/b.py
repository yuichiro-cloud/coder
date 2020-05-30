n,k = map(int,input().split())

a = []
d = []
for i in range(k):
  d.append(input())
  a+=(map(int,input().split()))
set_a = set(a)
count = 0
for i in range(1,n+1):
  if i in set_a:
    continue
  else:
    count+=1
print(count)