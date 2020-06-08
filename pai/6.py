n,m = map(int,input().split())
m_box = []
for i in range(m):
  m_box.append(int(input()))

point = 0
cash = n

for i in range(m):
  if point < m_box[i]:
    cash-=m_box[i]
    point += m_box[i]//10
    print(f"{cash} {point}")
  else:
    point-=m_box[i]
    print(f"{cash} {point}")