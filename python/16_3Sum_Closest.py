#!/usr/bin/env python
# -*- coding: utf-8 -*-

"16. 3Sum Closest"
__author__ = 'Tom Gou'

"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

解法与3Sum类似，结果只有一个因此可以去掉检测重复的地方。
使用past记录上一轮的sum和，和这一轮进行对比。
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        last = nums[0] + nums[1] +nums[n - 1]

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(sum - target) < abs(last - target):
                    last = sum

                if sum == target:
                    return target
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return last


def main():
    newclass = Solution()

    print  newclass.threeSumClosest([-1, 2, 1, -4], 1)

if __name__ =='__main__':
    main()