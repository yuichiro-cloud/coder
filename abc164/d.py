s = input()
len_s = len(s)
count = 0
for i in range(len_s + 1):
  for index in range(i + 1):
    if i != index and int(s[index:i])%2019 == 0:
      count+=1
print(count)

