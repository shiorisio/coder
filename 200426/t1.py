X, Y = map(int, input().split())
if X > Y:
    print('safe')
elif X <= Y:
    print('unsafe')
