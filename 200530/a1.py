H1, M1, H2, M2, K = map(int, input().split())

a = 0
if H1 < H2:
    a = (H2-H1)*60+M2-M1
else:
    a = M2-M1

print(a-K)
