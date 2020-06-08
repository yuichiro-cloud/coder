h,w = map(int,input().split())
a = []
a.append(list(map(int,input().split())))
a.append(list(map(int,input().split())))

l = []

for index in range(h):
  l.append([0]*w)

l[0][0] = a[0][0]
l[0][1] = a[0][1]
l[1][0] = a[1][0]
l[1][1] = a[1][1]
print(l)

h_diff = a[1][0] - a[0][0]
w_diff = a[0][1] - a[0][0]




