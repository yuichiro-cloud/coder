import math
n = int(input())
x = math.ceil(n/1.08)
if math.floor(x*1.08) == n: #1.08で割って元に戻した値を切り捨てした値が同じになる時
  print(x)
else:
  print(':(')
