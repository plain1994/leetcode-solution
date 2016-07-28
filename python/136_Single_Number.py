#!/usr/bin/env python
# -*- coding: utf-8 -*-

"136. Single Number"
__author__ = 'Tom Gou'

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

这道题要求O(n)的时间复杂度，解法用到了异或操作。
异或操作是可交换操作(1)a^b=b^a (2)0^a=a (3)a^a=0

整个算法对所有的元素做异或运算，即a1^a2^a3^a4^...
可将相同元素交换到相邻位置，得结果0
最后计算结果仅剩0和单一元素。
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans


def main():
    newclass = Solution()

    print  newclass.singleNumber([1,2,3,4,5,6,3,4,6,5,1])






if __name__ =='__main__':
    main()