import fractions
# a = list(map(int, input().split()))
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ans = a[0]
for i in range(1, 20):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
print(ans)