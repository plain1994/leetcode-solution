#!/usr/bin/env python
# -*- coding: utf-8 -*-

"35. Search Insert Position"
__author__ = 'Tom Gou'

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

这道题比较简单，遍历数组，使用二分法可以降低时间复杂度到O(log n)
如果没有查找到数字，最后返回l
因为该数字一定在l与r的区间之间。
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l


def main():
    newclass = Solution()

    print  newclass.searchInsert([1, 3, 5, 6], 5)



if __name__ =='__main__':
    main()