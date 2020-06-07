import numpy as np
s = input()
len_s = len(s)
counter = []
for i in range(len_s + 1):
  for index in range(i + 1):
    if i != index:
      counter.append(int(s[index:i]))
np_counter = np.array(counter)
np_2019 = np_counter % 2019
print(np.count_nonzero(np_2019 == 0))

# s = input()
# len_s = len(s)
# count = 0
# for i in range(len_s + 1):
#   for index in range(i + 1):
#     if i != index and int(s[index:i])%2019 == 0:
#       count+=1
# print(count)
