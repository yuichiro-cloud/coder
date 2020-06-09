n,x = map(int,input().split())
taxi = []

for i in range(n):
  taxi.append(list(map(int,input().split())))

price = []

for i in range(n):
  if x < taxi[i][0]:
    price.append(taxi[i][1])
  else:
    price.append(taxi[i][1] + taxi[i][3]*(int(((x - taxi[i][0])//taxi[i][2]))+1))
print(f"{min(price)} {max(price)}")