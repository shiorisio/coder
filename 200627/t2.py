s = list(input())
t = list(input())
a = 0
for i, _ in enumerate(s):
    if s[i] != t[i]:
        a = a+1
print(a)
