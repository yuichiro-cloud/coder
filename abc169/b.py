import numpy as np
n = int(input())

a = list(map(int,input().split()))
np_a = np.array(a)
ans = np.prod(np_a)
if ans > 10**18:
  print('-1')
else:
  print(int(ans))