h1, m1, h2, m2, k = map(int, input().split())
l = h2 * 60 + m2 - h1 * 60 - m1
print(max(0, l - k))
