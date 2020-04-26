import itertools
N = list(input())
# Ns = ''.join(N)
M = list(map(str, list(range(len(N)))))
S = list(itertools.combinations(M,2))
count = 0
for _, combi in enumerate(S):
    X,Y = map(int,combi)
    if Y - X > 2:
        A = N[X:Y+1]
        B = int(''.join(A))
        # print(A,B)
        if B%2019 == 0:
            count += 1
print(count)
