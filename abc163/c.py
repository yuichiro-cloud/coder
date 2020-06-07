import time
n = int(input())
a = list(map(int,input().split()))
t1 = time.time()

for i in range(1,n+1):
  print(a.count(i))
# count = ''
# for i in range(1,n+1):
#   # print(a.count(i))
#   count+=(str(a.count(i))+'\n')
# print(count)
# print([0]*n)
# l = [0]*n

# for i in a:
#   l[i-1] +=1
# for i in l:
#   print(i)
t2 = time.time()
print(f"経過時間:{t2-t1}")


# 50
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
# 0.0006172657012939453 for 2回
# 0.0003349781036376953 文字列一括出力
# 0.0006849765777587891 初めのやり方