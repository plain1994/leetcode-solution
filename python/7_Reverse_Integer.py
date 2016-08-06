#!/usr/bin/env python
# -*- coding: utf-8 -*-

"7. Reverse Integer"
__author__ = 'Tom Gou'

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

这道题主要是数学问题，较为简单的方法是：
前一位得到的数字乘10，再加上新得到的数字。

另外题目剧透中说了需要考虑32-bit整数溢出的情况，
因此将结果与2**32-1的大小进行判断。
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return (-1) * self.reverse((-1) * x)

        num = 0
        while x > 0:
            num = num * 10 + x % 10
            x /= 10

        if num > 2**31 -1:
            num = 0
        return num







def main():
    newclass = Solution()

    print  newclass.reverse(0)
    print  newclass.reverse(100)
    print  newclass.reverse(123)
    print  newclass.reverse(1534236469)
    print  newclass.reverse(-123)




if __name__ =='__main__':
    main()