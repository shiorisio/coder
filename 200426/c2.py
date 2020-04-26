N, M = map(int, input().split())
A = input()
B = []
atemp = A.split()
c = 0
for i, num in enumerate(atemp):
    B.append(atemp[i])
    c += int(num)

if N-c < 0:
    print('-1')
else:
    print(N-c)
