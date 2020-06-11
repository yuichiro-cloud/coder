n = 600851475143
n1 = n
number = 2
l = []
while n1 !=1:
  if n1%number == 0:
    l.append(number)
    while n1%number == 0:
      n1 = n1/number
  number+=1
print(max(l))