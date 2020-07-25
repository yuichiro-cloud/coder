import re
n = list(map(str,input().split()))
print(f'nです{n}')

l2 = []
l22 = []
for i in range(len(n)):
  if n[i] == '(':
    l22  = []
  elif n [i] == ')':
    l2.append(l22)
    l22 = []
  elif (n[i] == '+' or n[i] == '-' or n[i] == '*' or n[i] == '/') and (l22 == []):
    l2.append(n[i]) 
  else:
    l22.append(n[i])
print(l2)

l3 = 0
ans_l = []
print(len(l2))
sisoku = ''
for i in range(len(l2)):
  num = 0
  for i2 in range(len(l2[i])):
    if len(l2[i]) == 1 and (l2[i][i2] == '+' or l2[i][i2] == '-' or l2[i][i2] == '*' or l2[i][i2] == '/'):
      # ans_l.append(l2[i])
      num = l2[i]
    
    if l2[i][i2] != '+' and l2[i][i2] != '-' and l2[i][i2] != '*' and l2[i][i2] != '/':
      if sisoku != '':
        if sisoku == '+':
          print('plus')
          print(f'l3のあたい{l3}')
          print(f'intのあたい{int(l2[i][i2])}')
          num = l3 + int(l2[i][i2])
          print(num)
        else:
          num = l3 - int(l2[i][i2])
        sisoku = ''
      else:
        # print('sisoku入ってない')
        l3 = int(l2[i][i2])
        print(f'l3初期化{l3}')
    else:
      sisoku = l2[i][i2]
  ans_l.append(num)
print(ans_l)

ans = ''
sisoku = ''
for elem_ans in ans_l:
  if elem_ans == '+' or elem_ans == '-' or elem_ans == '*' or elem_ans == '/':
    sisoku = elem_ans
  else:
    if sisoku ==  '':
      ans = elem_ans
    else:
      if sisoku == '+':
        ans+= elem_ans
      elif sisoku == '-':
        ans -= elem_ans
      elif sisoku == '*':
        ans *= elem_ans
      else:
        asn /= elem_ans
    sisoku = ''
print(ans)



