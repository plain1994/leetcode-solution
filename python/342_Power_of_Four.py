#!/usr/bin/env python
# -*- coding: utf-8 -*-

"342. Power of Four"
__author__ = 'Tom Gou'

"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

这道题目是231 power of two的延伸，
解法0用到了循环，太简单就不说了。

4的幂也是2的幂，但区别是4的幂在二进制中，1在奇数位上。
解法1就在判断2的幂的基础上，判断n的奇数位是否为1，
0x55555555 = 1010101010101010101010101010101
因此与操作可以判断奇数位情况。

解法2简单，在判断2的幂的基础上，判断n-1是否被3整除。
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.isPowerOfFour1(num)
    def isPowerOfFour0(self, num):
        if num == 0:
            return False
        while num % 4 == 0:
            num /= 4
        if num == 1:
            return True
        else:
            return False
    def isPowerOfFour1(self, num):
        if (num > 0) and (num & (num-1) == 0) and (num & 0x55555555 != 0):
            return True
        else:
            return False

    def isPowerOfFour2(self, num):
        if (num > 0) and (num & (num - 1) == 0) and ((num-1)%3 == 0):
            return True
        else:
            return False




def main():
    newclass = Solution()

    print  newclass.isPowerOfFour(4)
    print  newclass.isPowerOfFour(3)





if __name__ =='__main__':
    main()