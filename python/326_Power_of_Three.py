#!/usr/bin/env python
# -*- coding: utf-8 -*-

"326. Power of Three"
__author__ = 'Tom Gou'

"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

这道题简单解法可以一直对数字除以3，看最后结果是不是1，如解法0

解法1利用了整数的限制范围，整数是32位的max = 2^32/2 -1
log3max = 19.56，因此范围内的最大3的幂整数为3^19 =1162261467，
所有的3的幂都应该整除该数。
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.isPowerOfThree1(n)
    def isPowerOfThree0(self, n):
        if n == 0:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return  True
        else:
            return False
    def isPowerOfThree1(self, n):
        if n == 0:
            return False
        if 1162261467 % n == 0:
            return True
        else:
            return False


def main():
    newclass = Solution()

    print  newclass.isPowerOfThree(4)
    print  newclass.isPowerOfThree(3)





if __name__ =='__main__':
    main()