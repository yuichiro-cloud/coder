k,n = map(int,input().split())
a = list(map(int,input().split()))

count = []

for i in range(n):
  if a[i]-a[i-1]<0:
    count.append(20+(a[i]-a[i-1]))
  else:
    count.append(20-(a[i]-a[i-1]))
print(min(count))
