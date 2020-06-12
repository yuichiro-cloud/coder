k,n = map(int,input().split())
a = list(map(int,input().split()))

count = []

for i in range(n):
  if (a[i-1]-a[i])<0:
    count.append(a[i-1]-a[i]+20)
  else:
    count.append(a[i-1]-a[i])
print(min(count))