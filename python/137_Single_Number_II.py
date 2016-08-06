#!/usr/bin/env python
# -*- coding: utf-8 -*-

"137. Single Number II"
__author__ = 'Tom Gou'

"""未完成
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = [0 for i in xrange(n)]
        print d

        for num in nums:
            for j in xrange(n):
                if (((1 << j) & num) > 0):
                    d[j] += 1
        ans = 0
        for j in xrange(n):
            t = d[j] % 3
            if (t == 1):
                ans = ans + (1 << j)
            elif (t != 0):
                return -1
        return ans

def main():
    newclass = Solution()

    print  newclass.singleNumber([1,2,3,4,5,6,3,4,6,5,1,1,3,5,4,6])






if __name__ =='__main__':
    main()