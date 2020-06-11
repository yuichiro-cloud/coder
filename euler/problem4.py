import numpy as np
l = []
for i in range(100,1000):
  for i2 in range(100,1000):
    l.append(i*i2)

np_l = np.array(l)
np_l_1 = np.array(np_l[np_l<100000])
np_l_2 = np.array(np_l[np_l>=100000])
np_l_2_r = np.array(np_l_2[(np_l_2//10**5 == np_l_2%10) & ((np_l_2//10**4)%10 == (np_l_2//10)%10)&((np_l_2//10**3)%10 == ((np_l_2//10**2)%10))])
np_l_1_r = np.array(np_l_1[(np_l_1//10**4 == np_l_1%10**4) & ((np_l_1//10**3)%10 == (np_l_1//10)%10**3)])

if np_l_2_r.size != 0:
  print(max(np_l_2_r))
else:
  print(max(np_l_1_r))
