#!/usr/bin/env python
# -*- coding: utf-8 -*-

"15. 3Sum"
__author__ = 'Tom Gou'

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

题目要求升序，所以我们首先对数组进行排序
计算的具体过程：
    从0到n-3遍历第一个数字i，然后另外两个数字l和r从i和n-1向中间逼近
    若和小于0，将l的位置升一位；若大于0，将r的位置降一位
    若和等于0，两个数字同时向中间逼近一位，当两数字相遇时跳出循环
因为结果是非重复的，在遇到临近的相同数字需要跳过
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        returnlist = []

        for i in range(n - 2):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i]+nums[l]+nums[r]<0:
                    l += 1
                elif nums[i]+nums[l]+nums[r]>0:
                    r -= 1
                else:
                    returnlist.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return returnlist


def main():
    newclass = Solution()

    print  newclass.threeSum([-1, 0, 1, 2, -1, -4])
    print  newclass.threeSum([-4, -3, 0, 1, 2, 2, 3, 4])

if __name__ =='__main__':
    main()