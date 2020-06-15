n,m,q = map(int, input().split())
# blist = [0] * n
flist = [[]] * m
for i in range(q):
    a = list(input().split())
    ans = 0
    if int(a[0]) == 1:
        for _,i in enumerate(flist):
            if int(a[1]) in i:
                ans = ans + (n-len(i))
        print(ans)
    elif int(a[0]) == 2:
        flist[int(a[2])-1] += [int(a[1])]
