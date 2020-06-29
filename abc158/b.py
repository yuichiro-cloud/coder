n,b,r = map(int,input().split())

s_b = ['b']*b
s_r = ['r']*r
l = []
for i in range(1000):
  l+=(s_b + s_r)

print(l[0:n].count('b'))