n = int(input())
a = list(map(int, input().split()))
b = 1
import sys
for x,y in enumerate(a):
    if y == 0:
        print('0')
        sys.exit()
    b = b*y
if b > 10**18:
    print('-1')
else:
    print(b)
