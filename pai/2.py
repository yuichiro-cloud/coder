a,b,c = map(int,input().split())
n = int(input())
time = []
for i in range(n):
  time.append(input().split())
minute_time = []
for i in range(n):
  minute_time.append(int(time[i][0])*60+int(time[i][1]))
arrive = []
for i in range(n):
  arrive.append(minute_time[i]+b+c)
ok_arrive = [i for i in arrive if i<=539]
ans = max(ok_arrive) - a - b -c
fin_ans = f"0{ans//60}:{str(ans%60).zfill(2)}"
print(fin_ans)
