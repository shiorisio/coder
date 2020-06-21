import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
q = int(input())
# c = [fun(a) for i in range(int(input())]
xs = [list(map(int, input().split())) for _ in range(q)]
for i in range(q):
    # x,y = map(int, input().split())
    a = [xs[i][1] if b == xs[i][0] else b for b in a]
    print(sum(a))
