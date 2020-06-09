n = int(input())

f = []
for i in range(n):
  f.append(int(input()))

f1 = 1
count = 0
for i in f:
  count+= int(((i - f1)**2)**0.5)//1
  f1 = i
print(count)