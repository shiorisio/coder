X=int(input())
c = 0
a = 100
while True:
    a = int(a * 1.01)
    c += 1
    if a >= X:
        print(c)
        break
