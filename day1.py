# B - Power Socket
def sum(A, B):
  n = 0
  while True:
    if n >= (B-1)/(A-1):
      return n
    else:
      n += 1

num = input().split(' ')
A = int(num[0])  #2<=A<=20
B = int(num[1])    #1<=B<=20

n = sum(A,B)
print(n)
# A, B = map(int, input().split())
# print((A+B-3)//(A-1))


