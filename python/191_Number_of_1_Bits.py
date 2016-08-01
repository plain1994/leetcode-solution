#!/usr/bin/env python
# -*- coding: utf-8 -*-

"191. Number of 1 Bits"
__author__ = 'Tom Gou'

"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

这道题较为简单，用到了位操作，
为了求整数n包含二进制1的个数，我们把n与1做二进制的与运算，即可判断其最低位是否为1，并计数；
然后把n向右移动一位，重复与操作，直到n变为0停止。
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1
        return count


def main():
    newclass = Solution()

    print  newclass.hammingWeight(4)




if __name__ =='__main__':
    main()