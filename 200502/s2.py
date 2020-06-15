X, Y, Z, K = map(int, input().split())
if X >= K:
    print(K)
elif X+Y >= K:
    print(X)
elif X+Y+Z >= K:
    print(X-(K-X-Y))
