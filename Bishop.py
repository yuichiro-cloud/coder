(h,w) = list(map(int,input().split()))

if h==1 or w==1:
  print(1)
elif w%2==0:
  print(int((w//2)*h))
else:
  print((h-(h//2))*(int((w//2)+(w%2)))+(h//2)*(int((w//2))))


# if では横が2の倍数の時、横幅割る2かける高さ
# elifでは高さが１の時
# elseでは横幅が奇数、高さが奇数の時。
# 奇数の高さはブロックがw//2足す1 偶数の高さはw//2
# wが１の場合はhの値によらず斜め移動できない。




