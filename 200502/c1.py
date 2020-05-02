X = int(input())
Y, Z = map(int, input().split())
a = Y%X
if a != 0 and Z >= Y-a+X:
    print('OK')
elif a == 0:
    print('OK')
else:
    print('NG')
