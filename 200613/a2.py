a,v = map(int, input().split())
b,w = map(int, input().split())
t = int(input())
'''import sys
x = 0
while x<=t:
    if a == b:
        print('YES')
        sys.exit()
    else:
        a = a+v
        b = b+w
        x = x+1
print('NO')'''
if v-w != 0:
    '''if a-b > 0:'''
    if (a-b)/(w-v) <= t and (a-b)/(w-v) >= 1:
        print('YES')
    else:
        print('NO')
    '''elif b-a > 0:
        if (b-a)/(v-w) <= t and (b-a)/(v-w) >= 1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')'''
else:
    print('NO')
'''    if not b-a > 0 and w-v > 0:
        if (a-b)/(v-w) > t:
            print('NO')
        elif (a-b)/(w-v) < t:
            print('YES')
        else:
            print('YES')
    else:
        print('NO')
else:
    print('NO')'''
