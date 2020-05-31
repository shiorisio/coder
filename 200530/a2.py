N = list(input())
for i,a in enumerate(N):
    if a == "?":
        N[i] = "D"
print(''.join(N[0:len(N)]))
