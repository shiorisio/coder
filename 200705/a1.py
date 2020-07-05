s = int(input())
if s%1000 == 0:
    print((s//1000)*1000-s)
else:
    print((s//1000+1)*1000-s)
