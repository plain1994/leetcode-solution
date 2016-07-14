#!/usr/bin/env python
# -*- coding: utf-8 -*-

'66. Plus One'
__author__ = 'Tom Gou'

"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

从后往前遍历数组，注意加法进位。注意第一个数字如果要进位的话，需要插入一个数字。
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        carry = 1
        while i >= 0 and carry == 1:
            number = digits[i] + 1
            digits[i] = number % 10
            carry = number/10
            i -= 1

        if carry == 1:
            digits.insert(0,1)
        return digits

        """这个逻辑设计不简洁
        n = len(digits)
        number = digits[n-1] + 1
        if number < 10:
            digits[n-1] = number
        i = 0
        while number == 10 and i < n-1:
            digits[n-1-i] = 0
            number = digits[n-2-i] + 1
            print "number:",number
            i += 1
        if number == 10:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[n-1-i] = number

        return digits
        """

def main():
    newclass = Solution()
    print newclass.plusOne([1,1,1,2,2,9])
    print newclass.plusOne([9])




if __name__ =='__main__':
    main()