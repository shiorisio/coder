x,y = map(int, input().split())
p = input().split()
p1 = list(map(int, p))
p1.sort()
a = 0
for i in range(y):
    a = a + p1[i]
print(a)
