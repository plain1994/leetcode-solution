#!/usr/bin/env python
# -*- coding: utf-8 -*-

"268. Missing Number"
__author__ = 'Tom Gou'

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

这道题要求O(n)的时间复杂度，解法用到了异或操作。本质和136题single number一样。
异或操作是可交换操作(1)a^b=b^a (2)0^a=a (3)a^a=0

首先对1到n所有数字做异或操作，
然后对数组中的所有数字做异或操作，得到的结果就是没有配对的数字，
即漏掉的数字。
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n+1):
            ans = ans ^ i
        for num in nums:
            ans = ans ^ num

        return ans




def main():
    newclass = Solution()

    print  newclass.missingNumber([0, 1, 3])




if __name__ =='__main__':
    main()