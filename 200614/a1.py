s = list(map(int, input().split()))
for i,y in enumerate(s):
    if int(y) == 0:
        print(i+1)
