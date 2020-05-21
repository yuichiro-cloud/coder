a = list(map(int,input().split()))
a += list(map(int,input().split()))
a += list(map(int,input().split()))
n = int(input())
b = []
for i in range(n):
  b.append(int(input()))
index = 0
for i in a:
  if i in b:
    a[index] = 0
  else:
    next
  index += 1

if (a[0]is a[1]is a[2]is 0)or(a[3]is a[4]is a[5]is 0)or (a[6]is a[7]is a[8]is 0)or(a[0]is a[3]is a[6]is 0)or(a[1]is a[4]is a[7]is 0)or(a[2]is a[5]is a[8]is 0)or(a[0]is a[4]is a[8]is 0)or(a[2]is a[4]is a[6]is 0):
  print('Yes')
else:
  print('No')

# ビンゴになる条件をifの条件にした。
# bに入っているaの値には0を代入
