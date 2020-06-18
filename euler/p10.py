count = 0
l = []
for i in range(2,200000):
  for i2 in range(2,int((i**0.5)//1 + 1)):
    l.append(i%i2)
  if 0 not in l:
    count+=i
  l = []

print(count)
  
