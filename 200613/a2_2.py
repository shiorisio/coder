a,v = map(int, input().split())
b,w = map(int, input().split())
t = int(input())
if v-w != 0 and v >= 1 and w >= 1:
    if (a-b)/(w-v) <= t and (a-b)/(w-v) > 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
