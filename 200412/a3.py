from fractions import gcd
a = int(input())
ans = 0
for i in range(1,a+1):
  for j in range(1,a+1):
    for k in range(1,a+1):
        # ans = ans + np.gcd.reduce([i, j, k])
        ans = ans + gcd(gcd(i, j),k)
print(ans)
