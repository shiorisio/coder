N, M=map(int, input().split())
A=list(map(int, input().split()))
S=sum(A)
A.sort()
if A[-M]>=S/(4*M):
    print('Yes')
else:
    print('No')
