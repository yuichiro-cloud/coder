n,k = map(int,input().split())
p = list(map(int,input().split()))

p.sort()
price = 0
for i in range(k):
  price+=p[i]
print(price)