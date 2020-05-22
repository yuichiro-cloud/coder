import math
a,b,h,m = map(int,input().split())


if 30*h == 6*m:
  print(0)
elif 30*h > 6*m:
  rad = 30*h - 6*m
else:
  rad = 6*m - 30*h

if rad == 180:
  print(a+b)
elif rad > 180:
  rad = 360 - rad
else:
  next
# rad = ((math.pi)*rad)/180
# rad = 90
# print(rad)
# print(math.cos(math.radians(rad)))
# print(math.cos1.5708) 
rad = math.radians(rad)
# print(rad)
# print(math.cos(rad))

c = (a**2 + b**2 -2*a*b*(math.cos(math.radians(rad))))**(1/2)
if c < 0:
  c = -c
else:
  next
print(c)

