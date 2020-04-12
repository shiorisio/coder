a = input()
x = int(a)//100
y = (int(a)-x*100)//10
z = int(a) - y*10 - x*100
if x == 7 or y == 7 or z == 7:
    print('Yes')
else:
    print('No')
