#!/usr/bin/env python
# -*- coding: utf-8 -*-

"231. Power of Two"
__author__ = 'Tom Gou'

"""
Given an integer, write a function to determine if it is a power of two.

这道题不难，最好想到的做法是一直对数字除以2（余数为0），看最后剩下的数值是否为1,如方法0

另外，可以使用位移操作，方法1是使用位移生成2的幂，然后比较n。
具体的，2的幂用二进制来看都是1开头，后面数字全是0，所以没位移一次，数字翻倍一次。

方法2比较巧妙，效率高。2的幂n都是1000这种形式，这里把n-1进行按位与。
因为n-1是0111的形式，如果按位与结果为0，则n为2的幂。
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.isPowerOfTwo0(n)
    def isPowerOfTwo0(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        if n == 1:
            return True
        else:
            return False

    def isPowerOfTwo1(self, n):
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            ans = ans << 1
        return False

    def isPowerOfTwo2(self, n):
        if n <= 0:
            return False
        if n & (n-1) == 0:
            return True
        else:
            return False


def main():
    newclass = Solution()

    print  newclass.isPowerOfTwo(4)
    print  newclass.isPowerOfTwo(7)
    #print  newclass.isPowerOfTwo(8)




if __name__ =='__main__':
    main()