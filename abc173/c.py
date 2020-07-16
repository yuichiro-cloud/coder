h,w,k = map(int,input().split())

c = []
black = 0
for i in range(h):
  c_input = list(input())
  black+=c_input.count('#')
  c.append(c_input)
print(black)