import sys
n = int(input())
c = 0
for i in range(n):
    d = list(map(int, input().split()))
    if d[0] == d[1]:
        c = c + 1
        if c >= 3:
            print('Yes')
            sys.exit()
    else:
        c = 0
if c >= 3:
    print('Yes')
else:
    print('No')
