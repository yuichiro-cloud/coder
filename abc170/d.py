n = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
count = 0

for i in range(n):
  for i2 in range(i+1,n):
    if a[i]%a[i2] == 0:
      count-=1
      break
  count+=1
if a[-1]%a[-2]==0:
  count-=1
print(count)
