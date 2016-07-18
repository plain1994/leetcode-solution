#!/usr/bin/env python
# -*- coding: utf-8 -*-

"153. Find Minimum in Rotated Sorted Array"
__author__ = 'Tom Gou'

"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

解法与153. Find Minimum in Rotated Sorted Array基本一致，加入判断是否重复
具体的，判断l与l+1的值是否相等，如果相等，l+1；r也做相同处理
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
        if n == 2:
            return min(nums[0], nums[1])
        while l + 1 < r:
            if nums[l] == nums[l+1]:
                l += 1
            if nums[r] == nums[r-1]:
                r -= 1
            if nums[l] < nums[m] and nums[m] > nums[r]:
                l = m
            elif nums[l] > nums[m] and nums[m] < nums[r]:
                r = m
            elif nums[l] < nums[m] and nums[m] < nums[r]:
                return min(nums[l], nums[m])
            m = (l + r) / 2
        return min(nums[r], nums[l])


def main():
    newclass = Solution()

    print  newclass.findMin([4, 5, 6, 7, 0, 1, 2])
    print  newclass.findMin([1, 2])
    print  newclass.findMin([1, 2, 3])
    print  newclass.findMin([1, 1, 3])
    print  newclass.findMin([3, 1, 1])


if __name__ =='__main__':
    main()