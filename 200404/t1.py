#!/usr/bin/env python
import sys

if __name__ == '__main__':
    nums = input().split()
    a = nums[0]
    b = nums[1]
    c = nums[2]

    a = nums[1]
    b = nums[0]

    a = nums[2]
    c = nums[1]
    print(int(a),int(b),int(c))
    sys.exit()
