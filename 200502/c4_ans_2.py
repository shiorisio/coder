import math
a, b, n = map(int, input().split())

x = min(b-1, n)
print(math.floor(a*x/b) - a*math.floor(x/b))
