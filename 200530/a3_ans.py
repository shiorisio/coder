def solve():
    n = int(input())
    av = list(map(int, input().split(' ')))
    cur = 1
    ans = 0
    s = sum(av)
    for i in range(n+1):
        if cur < av[i]: return -1
        ans += cur
        s -= av[i]
        cur -= av[i]
        if (s <= cur * 2):
            j = 1
            while i + j < n + 1:
                ans += j * av[i + j]
                j += 1
            break
        cur *= 2
    return ans

print(solve())
