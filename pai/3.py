import math
p1,p2,p3,k = map(int,input().split())

k_box = []
tem = []
num = 1
while len(k_box) <k:
  index2 = int(math.log(num,2)//1)
  index3 = int(math.log(num,3)//1)
  index5 = int(math.log(num,5))
  if num in tem:
    k_box.append(num)
  else:
    for i in range(index2+1):
      for i2 in range(index3+1):
        for i3 in range(index5+1):
          tem.append((p1**i)*(p2**i2)*(p3**i3))
    if num in tem:
      k_box.append(num)
    set(tem)
  num+=1
print(k_box[k-1])



