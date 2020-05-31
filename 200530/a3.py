def check(M, a):
    for i,b in enumerate(M):
        a = a - int(b)
    return a

def popall(M):
    c = []
    for i in range(0,len(M)):
        if i > 0:
            a = M[0:i] + M[i+1::]
        elif i == 0:
            a = M[i+1::]
        c.append(''.join(a))
    return c

def ckall(c):
    ans = []
    for _,i in enumerate(c):
        ans.append(check(i,0))
    return ans.index(min(ans)), c[ans.index(min(ans))]

def efun(N,a):
    b = ckall(popall(N[0::2]))[0]
    if int(b) > 0:
        rN = N[0:b] + N[b+1::]
    elif int(b) == 0:
        rN = N[b+1::]
    a = a + int(ckall(popall(N[0::2]))[1])
    return rN,a

if __name__ == '__main__':
    N = list(input())
    a = 0
    while True:
        N,a = efun(N,a)
        if len(N) == 2:
            # print(''.join(N))
            print(a)
            break
