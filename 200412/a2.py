a = input()
aList = []
for i in range(1,int(a)+1):
    if i%3 == 0 and i%5 == 0:
        pass
        # print('FizzBuzz')
    elif i%3 == 0:
        pass
        # print('Fizz')
    elif i%5 == 0:
        pass
        # print('Buzz')
    else:
        aList.append(i)
        # print(i)
ans = 0
for _,b in enumerate(aList):
    ans = ans + b
print(ans)
