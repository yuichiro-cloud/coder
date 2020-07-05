n = int(input())
pay = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

for p in pay:
  if (p - n) < 1000 and (p - n) >= 0:
    print(p-n)
    exit()

  
    

