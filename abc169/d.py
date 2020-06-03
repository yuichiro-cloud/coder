n = int(input())
p = []
n2 = n
# for i in range(2,int(n2**0.5//1 + 1)):
for i in range(2,n):
  index = 0
  while n2%i == 0:
    index+=1
    n2 = n2//i
  if index != 0:
    p.append(index)
  else:
    continue
count = 0
t = 1

if n == 1:
  print(0)
elif not p:
  print(1)
else:
  for i in range(len(p)):
    while p[i] - t >= 0:
      p[i]-=t
      count+=1
      t+=1
    t = 1
  print(count)


  



# n = int(input())

# number = 2

# p_box = []
# p = 0
# while n !=1:
#   if n%number == 0:
#     while n%number == 0:
#       n = n/number
#       p+=1
#     p_box.append(p)
#     p = 0
#     number+=1
#   else:
#     number+=1
# count = 0
# t = 1
# for i in range(len(p_box)):
#   while p_box[i] >0:
#     p_box[i]-=t
#     t+=1
#     count+=1
# print(count)






