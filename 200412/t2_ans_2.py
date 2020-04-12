N, M = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)

count = 0
for i in A:
    if i >= s/(4*M):
        count += 1
print("YNeos"[count < M::2])
