import numpy as np

l1 = np.arange(1,101)
l2 = np.square(l1)

print((sum(l1))**2 - sum(l2))
