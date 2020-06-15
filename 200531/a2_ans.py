n = int(input())
a = input().split(" ")

sum = 1
for i in a:
  sum = sum * int(i)
  if sum > 1000000000000000000:
    break

if "0" in a:
  print(0)
elif sum > 1000000000000000000:
  print(-1)
else:
  print(sum)
