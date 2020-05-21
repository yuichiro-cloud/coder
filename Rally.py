n = int(input())
# x = input().split(' ')
x = list(map(int,input().split()))

p = 0
ans = []
while p <= x[n-1]:
  e = 0
  for i in range(n):
    e += (x[i]-p)**2
  ans.append(e)
  p+=1
print(min(ans))