from collections import deque
n,m,k = map(int, input().split())
a = deque(map(int, list(input().split())))
b = deque(map(int, list(input().split())))
t = 0
c = 0
while k <= 1000000000 and n <= 200000 and m <= 200000:
    if c < n+m:
        if len(b) == 0 and t + a[0] <= k and a[0] <= 1000000000:
            t = t + a[0]
            a.popleft()
            c = c + 1
        elif len(a) == 0 and t + b[0] <= k and b[0] <= 1000000000:
            t = t + b[0]
            b.popleft()
            c = c + 1
        elif len(a) > 0 and len(b) > 0:
            if a[0] <= b[0] and a[0] <= 1000000000 and b[0] <= 1000000000 and t + a[0] <= k:
                t = t + a[0]
                a.popleft()
                c = c + 1
            elif a[0] > b[0] and a[0] <= 1000000000 and b[0] <= 1000000000 and t + b[0] <= k:
                t = t + b[0]
                b.popleft()
                c = c + 1
            else:
                break
        else:
            break
    else:
        break
print(c)
