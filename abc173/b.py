n = int(input())
s = []
for i in range(n):
  s.append(input())

judge = {'AC':0,'WA':0, 'TLE':0, 'RE':0}

for s1 in s:
  if s1 == 'AC':
    judge['AC']+=1
  elif s1 == 'WA':
    judge['WA']+=1
  elif s1 == 'TLE':
    judge['TLE']+=1
  else:
    judge['RE']+=1
print("AC x "f"{judge['AC']}")
print("WA x "f"{judge['WA']}")
print("TLE x "f"{judge['TLE']}")
print("RE x "f"{judge['RE']}")
