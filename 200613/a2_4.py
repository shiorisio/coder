a,v = map(int, input().split())
b,w = map(int, input().split())
t = int(input())
import sys
x = 0
while x<t:
    if a+v == b+w:
        print('YES')
        sys.exit()
    else:
        a = a+v
        b = b+w
        x = x+1
print('NO')
