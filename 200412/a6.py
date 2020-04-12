a = int(input())
b = list(map(int,input().split()))

if a%2 == 0:
    p = 0
    q = 0
    for i in range(a):
        if i%2 == 0:
            p = p + b[i]
        elif i%2 == 1:
            q = q + b[i]
    if p > q:
        print(p)
    else:
        print(q)
elif a%2 == 1:
    p = 0
    q = 0
    pList = []
    qList = []
    ab = a//2
    for i in range(a):
        if i%2 == 0:
            p = p + b[i]
            pList.append(b[i])
        elif i%2 == 1:
            q = q + b[i]
            qList.append(b[i])
    if len(pList) > ab:
        pansList = []
        for _,i in enumerate(pList):
            pansList.append(p-i)
        if max(pansList) > q:
            print(max(pansList))
        else:
            print(q)
    elif len(qList) > ab:
        qansList = []
        for _,i in enumerate(qList):
            qansList.append(q-i)
        if max(qansList) > p:
            print(max(qansList))
        else:
            print(p)
    else:
        if p > q:
            print(p)
        else:
            print(q)
