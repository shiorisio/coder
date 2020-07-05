a = 0
w = 0
t = 0
r = 0
n = int(input())
for i in range(n):
    s = str(input())
    if s == 'AC':
        a = a + 1
    elif s == 'WA':
        w = w + 1
    elif s == 'TLE':
        t = t + 1
    elif s == 'RE':
        r = r + 1
print('AC x ' + str(a))
print('WA x ' + str(w))
print('TLE x ' + str(t))
print('RE x ' + str(r))
