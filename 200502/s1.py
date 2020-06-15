import re
x = input()
y = input()
if x in y:
    if len(re.findall(x+'(.*)', y)[0]) == 1:
        print('Yes')
    else:
        print('No')
else:
    print('No')
