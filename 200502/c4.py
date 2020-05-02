a, b, n = map(int, input().split())
print(max(list(map(lambda x:(a*x)//b-a*(x//b), range(1, n+1)))))
