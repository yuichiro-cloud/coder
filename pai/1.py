leet = list(input())
print(len(leet))
for i in range(len(leet)):
  if leet[i] ==  'A':
    leet[i] = '4'
  elif leet[i] == 'E':
    leet[i] = '3'
  elif leet[i] == 'G':
    leet[i] = '6'
  elif leet[i] == 'I':
    leet[i] = '1'
  elif leet[i] == 'O':
    leet[i] = '0'
  elif leet[i] == 'S':
    leet[i] = '5'
  elif leet[i] == 'Z':
    print('z')
    leet[i] = '2'
  else:
    continue
print(''.join(leet))
