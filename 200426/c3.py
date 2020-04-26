N = int(input())
A = input()
B = []
atemp = A.split()
c = 0
d = 0
ans = []
atempstr = map(str,atemp)
print(atempstr)
print(int(max(atemp)))
for i in range(int(max(atemp))):
    ans.append(atempstr.count(str(i+1)))
ans.append(0)

print(ans)
