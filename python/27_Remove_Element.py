#!/usr/bin/env python
# -*- coding: utf-8 -*-

'27. Remove Element'
__author__ = 'Tom Gou'

"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

解法较为简单，使用两个数组下标，一个用来遍历原数组，一个用来记录不等于val的值。
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        j = 0
        for num in nums:
            if num != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i

        """
        //用enumerate函数似乎要慢一些
        i = 0
        for j, num in enumerate(nums):
            if num != val:
                nums[i] = nums[j]
                i += 1

        return i
        """



def main():
    newclass = Solution()
    print newclass.removeElement([3,2,2,3],3)


if __name__ =='__main__':
    main()