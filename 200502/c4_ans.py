import math
A, B, N = map(int,input().split())

def f(x):
  return math.floor((A*x)/B)-A*math.floor(x/B)

if  N >= (B-1):
  print(f(B-1))
else:
  print(f(N))
