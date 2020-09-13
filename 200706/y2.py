a = 0
p = 0
bt = 0
b = [0]
n = int(input())
for i in range(n):
    s = str(input())
    if s == 'add':
        a = a + 1
        bt = a
    elif s == 'pin':
        b.append(a)
    elif s == 'rollback':
        a = b[-1]
        if len(b) > 1:
            b.pop()
    elif s == 'print':
        print(a)
