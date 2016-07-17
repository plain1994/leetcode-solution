#!/usr/bin/env python
# -*- coding: utf-8 -*-

"153. Find Minimum in Rotated Sorted Array"
__author__ = 'Tom Gou'

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
待查数组已经排好顺序。
使用二分法来做这个题，具体的，将l，r与m进行对比，最小数在数值下降的半边。
每次迭代后，更新m的值。
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        m = (l + r) / 2
        if n ==2:
            return min(nums[0],nums[1])
        while l + 1 < r:
            if nums[l] < nums[m] and nums[m] > nums[r]:
                l = m
            elif nums[l] > nums[m] and nums[m] < nums[r]:
                r = m
            else:
                return min(nums[l],nums[m])
            m = (l + r) / 2
        return nums[r]


def main():
    newclass = Solution()

    print  newclass.findMin([4, 5, 6, 7, 0, 1, 2])
    print  newclass.findMin([1, 2])
    print  newclass.findMin([1, 2, 3])

if __name__ =='__main__':
    main()