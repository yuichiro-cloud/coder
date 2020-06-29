n,b,r = map(int,input().split())

x = n//(b+r)
x1 = n%(b+r)

if b >= x1:
  b_count = x1
else:
  b_count = b

print(x*b + b_count)