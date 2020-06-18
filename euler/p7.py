count = 1
num = 2
l = []
while count < 10001:
  num+=1
  for i in range(2,int((num)**0.5)//1 + 1):
    l.append(num%i)
  if 0 not in l:
    count+=1
  l = []
print(num)