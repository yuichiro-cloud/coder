def cal_digit(n):
  n2 = 26
  n2_l = [26]
  digit = 1
  while n/sum(n2_l)>=26:
    n2*=26
    n2_l.append(n2)
    digit+=1
  return n2_l
n = int(input())
alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

l = []

n_l = cal_digit(n)
print(n_l)
digit = len(n_l)
if n>sum(n_l):
  digit+=1

x = n
dif = n - n_l[-1]
for i in range(digit):

  if i == 0:
    l.append(alpa[dif%26 - 1])
  elif dif != 0:
    l.append(alpa[dif%26 - 1])
  else:
    l.append('a')
  print(l)
  dif = dif//26
  print(dif)
l.reverse()

ans = ''.join(l)
print(ans)




