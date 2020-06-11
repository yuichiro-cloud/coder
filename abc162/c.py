import math
import time
from functools import reduce
k = int(input())
t1 = time.time()

l = 0
for i in range(1,k+1):
  for i2 in range(1,k+1):
    for i3 in range(1,k+1):
      # l+=reduce(math.gcd,[i,i2,i3])
      l+=i3
print(l)
t2 = time.time()
print(t2 - t1)