N = int(input())
H = input().split(' ')
# print(N)
counter = []
for i in range(1,N):
  # i = 0
  
  while i < N - 1:
    print('aaaa')
    if H[i]>=H[i+1]:
      print('if')
      i+=1
    else:
      counter.append('aa')
      # print('break')
      # break

print(counter)
