s = list(input())
if s[-1] != 's':
    print(''.join(s) + 's')
elif s[-1] == 's':
    print(''.join(s) + 'es')
