X=int(input())
Y=list(input())
if X >= len(Y):
    print(''.join(Y[0:X]))
else:
    print(''.join(Y[0:X])+'...')
