import sys
input = sys.stdin.readline
N = int(input())
s = set()
for _ in range(N):
  s.add(input()[: -1])
print(len(s))
