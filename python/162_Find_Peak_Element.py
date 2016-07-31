#!/usr/bin/env python
# -*- coding: utf-8 -*-

"162. Find Peak Element"
__author__ = 'Tom Gou'

"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

这道题目不难，寻找数组中的peak。
可以直接遍历解决，如方法1，时间复杂度O(n)
也可以用二分法，如方法2，时间复杂度O(log n)

具体的，如果m大于两边的数，则为peak；
m小于左，则peak在左半边；m小于右，则在右半边。
注意判断时加上边界条件，避免数组索引溢出范围外。
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findPeakElement2(nums)

    def findPeakElement1(self, nums):
        tmp = nums[0]
        n = len(nums)
        i = 0

        while tmp <= nums[i]:
            if i == n -1:
                return i
            tmp = nums[i]
            i += 1
        return i - 1

    def findPeakElement2(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m =(l + r) / 2
            if (m == 0 or nums[m-1]<nums[m]) and (m == n-1 or nums[m]>nums[m+1]):
                return m
            elif m > 0 and nums[m-1]>nums[m]:
                r = m - 1
            elif m < n and nums[m]<nums[m+1]:
                l = m + 1




def main():
    newclass = Solution()

    #print  newclass.findPeakElement([1, 2, 3, 1])
    #print  newclass.findPeakElement([1, 2, 3, 4])
    print  newclass.findPeakElement([1, 2])



if __name__ =='__main__':
    main()