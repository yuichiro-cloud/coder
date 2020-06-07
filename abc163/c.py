n = int(input())
a = list(map(int,input().split()))
count = ''
for i in range(1,n+1):
  # print(a.count(i))
  count+=(str(a.count(i))+'\n')
print(count)