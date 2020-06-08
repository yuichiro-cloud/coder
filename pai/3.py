p1,p2,p3,k = map(int,input().split())

k_box = []
index2 = 40
index3 = 30
index5 = 25
for i in range(index2):
  for i2 in range(index3):
    for i3 in range(index5):
      k_box.append(p1**(i)*p2**(i2)*p3**(i3))
k_box.sort()
print(k_box[k-1])



