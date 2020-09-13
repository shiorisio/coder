import numpy
s = list(map(int, input().split()))
a = []
for i,t in enumerate(s):
    if t != max(s) and t != min(s):
        a.append(t)
print(int(numpy.average(a)))
