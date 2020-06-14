import time
n = int(input())
a = list(map(int,input().split()))
t1 = time.time()
a.sort(reverse=True)
t2 = time.time()
count = 0

for i in range(n):
  for i2 in range(1,n-i):
    if a[i]%a[-i2] == 0:
      count-=1
      break
  count+=1
if a[-1]%a[-2]==0:
  count-=1
print(count)
t3 = time.time()

print(t2-t1)
print(t3-t1)