#!/usr/bin/env python
# -*- coding: utf-8 -*-

"45. Jump Game II"
__author__ = 'Tom Gou'

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

这道题不难，用贪心算法

使用两个变量，cur记录当前的步数到达的位置，
next记录下一步能到达的最远位置（用index加步数），
当当前位置到达最后就跳出循环。


还可以用动态规划，dp方程
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        step = 0
        cur = 0
        nex = 0

        i = 0
        while i < n:
            if cur >= n - 1:
                break
            while i <= cur:
                nex = max(nex, nums[i] + i)
                i += 1

            step += 1
            cur = nex

        return step



def main():
    newclass = Solution()

    nums1 = [2,3,1,1,4]
    nums2 = [0]


    print newclass.jump(nums1)
    print newclass.jump(nums2)

if __name__ =='__main__':
    main()