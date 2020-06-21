import sys
input = sys.stdin.readline
c = list(map(int, input().split()))
n = list(map(str, input().split()))
a = 0
for x, i in enumerate(c):
    if n[x] == 'Alice':
        a = a + i
print(a)
