n = int(input())

s = 2
x = {}

p_box = []
while n != 1:
  if n%s == 0:
    p = 0
    p_box.append(s)
    while n%s == 0:
      p+=1
      x[str(s)] = p
      n = n/s
  else:
    s+=1
count = 0
for i in range(len(x)):
  if str(p_box[i]) not in x:
    continue
  else:
    t = 1
    while x[str(p_box[i])] - t > 0:
      count+=1
      t+=1  
print(count)




