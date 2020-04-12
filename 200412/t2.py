#!/usr/bin/env python
import sys

if __name__ == '__main__':

    NM = input().split()
    nums = input().split()

    numsl = []
    for _,a in enumerate(nums):
        numsl.append(int(a))

    N = NM[0]
    M = NM[1]
    sum = 0

    if int(N) > 100:
        print('No')
        sys.exit()
    if 0 > int(M):
        print('No')
        sys.exit()
    if int(M) > int(N):
        print('No')
        sys.exit()

    for i,a in enumerate(nums):
        sum = sum + int(a)

    numsr = sorted(numsl,reverse=True)

    y = 0
    for i,a in enumerate(nums):
        if int(a) >= int(numsr[int(M)-1]):
            if int(a) > int(sum)//(4*int(M)):
                y = y + 1

    if y >= int(M):
        print('Yes')
    else:
        print('No')
