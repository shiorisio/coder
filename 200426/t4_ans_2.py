s = input()
n = len(s)

m = 2019
cnt = [0]*(m+1)

ans = 0
p = 1
cur = 0
for i in reversed(range(n)):
    cur += p*int(s[i])
    cur %= m
    p *= 10
    p %= m

    if cur == 0:
        ans += 1
    ans += cnt[cur]
    cnt[cur] += 1

print(ans)
