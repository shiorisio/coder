import math
a,r,n = map(int, input().split())
if a == 0 or r == 0:
    print('0')
else:
    if n-1 > math.log(1000000000/a, r):
        print('large')
        #    if b > 1000000000:
        #        print('large')
    else:
        print(a*(r**(n-1)))
