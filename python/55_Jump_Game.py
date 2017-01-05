#!/usr/bin/env python
# -*- coding: utf-8 -*-

"55. Jump Game"
__author__ = 'Tom Gou'

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

这道题比较简单，使用贪心算法，
每次跳跃1步，如果新步数大于剩余步数，更换为新步数；
如果步数小于0且没到最后一个元素，失败

还可以用动态规划，以后再看
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) == 1:
            return True

        num1 = nums[0]

        for n in nums:
            num1 -= 1
            if num1 < 0:
                return False
            if num1 < n:
                num1 = n

        return True



def main():
    newclass = Solution()

    nums1 = [2,3,1,1,4]

    nums2 = [3,2,1,0,4]

    print newclass.canJump(nums1)
    print newclass.canJump(nums2)

if __name__ =='__main__':
    main()