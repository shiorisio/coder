#!/usr/bin/env python
import sys

if __name__ == '__main__':
    nums = input().split()
    a = nums[0]
    b = nums[1]

    while int(a) - int(b) < 0:
        x = int(a) - int(b)
        a = x - int(b)
    print(a - int(b))
    sys.exit()
