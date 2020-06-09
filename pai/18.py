# import itertools
# n = int(input())

# ab = []
# c = []

# for i in range(n-1):
#   x = list(map(int,input().split()))
#   ab.append(sorted(x[0:2]))
#   c.append([x[2]])
# print(ab)

# number = range(1,n+1)
# ptn = list(itertools.combinations(number,2))
# #list_ptnに街の組み合わせをlistに変換して保存
# list_ptn = []
# # def pt_find(pt_num_f,pt_num_l):
# #   count = []
# #   pt_num_f2 = pt_num_f
# #   while pt[pt != list_ptn[i][0]] not in count:
# #     # for pt_num_f in [i2 for i2 in ab if pt_num_f in i2]:
# #     for pt_num_f2 in [i2 for i2 in ab if pt_num_f2 in i2]:
# #     #list_ptnの最初の文字が含まれているものの中のその文字以外
# #       pt[pt != list_ptn[i][0]]
# #       count.append()
# #     # print(list_ptn[i][0])

# # def ptns():
# #   for pt_num_f2 in [i2 for i2 in ab if pt_num_f2 in i2]:


# for i in range(len(ptn)):
#   list_ptn.append(list(ptn[i]))
#list_ptnのそれぞれに対して[1,2]だったら2が含まれているものをabから探していく。目的の値になるまで繰り返す。
# for のなかのifでlist_ptn[i]がabにあるかどうか判断。
# for i in range(len(list_ptn)):
#   list_ptn[i][0]
#   pt_find(list_ptn[i][0],list_ptn[i][1])
  # pt_find()
  # if list_ptn[i] in ab:
  #   print('OK')
  # else:

    # # print([i2 for i2 in ab if list_ptn[i][0] in i2])
    # for pt in [i2 for i2 in ab if list_ptn[i][0] in i2]:
    #   #list_ptnの最初の文字が含まれているものの中のその文字以外
    #   pt[pt != list_ptn[i][0]]
    #   # print(list_ptn[i][0])




import itertools
n = int(input())

ab = []
c = []

for i in range(n-1):
  x = list(map(int,input().split()))
  ab.append(sorted(x[0:2]))
  c.append([x[2]])
# print(ab)

number = range(1,n+1)
ptn = list(itertools.combinations(number,2))
list_ptn = []
#list_ptnに街の組み合わせをlistに変換して保存
for i in range(len(ptn)):
  list_ptn.append(list(ptn[i]))
for i in range(len(list_ptn)):
  list_ptn[i]
  find_dis(list_ptn[i][0],list_ptn[i][1])

def find_dis(first_num,last_num):
  find_num = first_num
  for i in find_ptns(find_num):
    find_num = i[i != find_num]
    find_ptns(find_num)
def find_ptns(number):
  [i2 for i2 in ab if number in i2]





