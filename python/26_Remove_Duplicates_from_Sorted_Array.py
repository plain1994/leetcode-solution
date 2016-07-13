#!/usr/bin/env python
# -*- coding: utf-8 -*-

'26. Remove Duplicates from Sorted Array'
__author__ = 'Tom Gou'

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

解法较为简单，使用两个游标，一个用来遍历数组，一个记录新的不重复坐标。
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        if len(nums)>0:
            past = nums[0]
            for num in nums:
                if j > 0:
                    if num != past:
                        i += 1
                        nums[i] = num

                past = num
                j += 1
        else:
            i = -1

        return i+1




def main():
    newclass = Solution()
    print newclass.removeDuplicates([1,1,2])
    print newclass.removeDuplicates([])


if __name__ =='__main__':
    main()