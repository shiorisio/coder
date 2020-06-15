x,y = map(int, input().split())
if y >= x*2 and x*4 >= y:
    if (x*4-y)%2 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
