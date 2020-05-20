# N = int(input())
# H = input().split(' ')
# # print(N)
# counter = []
# for i in range(1,N):
#   # i = 0
  
#   while i < N - 1:
#     print('aaaa')
#     if H[i]>=H[i+1]:
#       print('if')
#       i+=1
#     else:
#       counter.append('aa')
#       # print('break')
#       # break

# print(counter)





n=int(input())
h=list(map(int,input().split()))
print(h)
count=0
ans=0
for i in range(n-1):
  if h[i]>=h[i+1]:
    count+=1
  else:
    ans=max(ans,count) #ansとcountの大きい方でansを再度宣言
    print(ans)
    count=0
print(max(count,ans))

