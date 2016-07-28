#!/usr/bin/env python
# -*- coding: utf-8 -*-

"67. Add Binary"
__author__ = 'Tom Gou'

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

这道题比较简单，遍历相加。
解法1是先遍历小长度，再把多余的长度加上
解法2是直接遍历大长度，在每次遍历过程中看a，b是否还存在，代码较少，时间复杂度高一些。
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.addBinary2(a, b)
    def addBinary1(self, a, b):
        an = len(a)
        bn = len(b)
        n = min(an, bn)
        carry = 0
        re = ""
        for i in range(1, n+1):
            digitsum = int(a[-i]) + int(b[-i]) + carry
            bit = digitsum % 2
            carry = digitsum / 2
            re = str(bit) + re
        if an < bn:
            for j in range(i, bn):
                digitsum = int(b[-j-1]) + carry
                bit = digitsum % 2
                carry = digitsum / 2
                re = str(bit) + re
            if carry == 1:
                re = "1" + re
        elif an > bn:
            for j in range(i, an):
                digitsum = int(a[-j-1]) + carry
                bit = digitsum % 2
                carry = digitsum / 2
                re = str(bit) + re
            if carry == 1:
                re = "1" + re
        else:
            if carry == 1:
                re = "1" + re

        return re

    def addBinary2(self, a, b):
        an = len(a)
        bn = len(b)
        carry = 0
        re = ""
        i = 1
        while i <= max(an, bn):
            digitsum = carry
            if i <= an:
                digitsum += int(a[-i])
            if i <= bn:
                digitsum += int(b[-i])
            bit = digitsum % 2
            carry = digitsum / 2
            i += 1
            re = str(bit) + re

        if carry == 1:
            re = "1" + re

        return re







def main():
    newclass = Solution()

    print  newclass.addBinary("11", "1")
    print  newclass.addBinary("100", "110010")
    print  newclass.addBinary("101111", "10")





if __name__ =='__main__':
    main()