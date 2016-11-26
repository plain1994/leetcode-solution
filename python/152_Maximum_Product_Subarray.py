#!/usr/bin/env python
# -*- coding: utf-8 -*-

"152. Maximum Product Subarray"
__author__ = 'Tom Gou'

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.


这道题不难，需要考虑的是负数乘负数会变成正数，可能得到最大值，
因此我们还维护一个最小值。dp方程为：

maxdp[i+1] = max(max(maxdp[i]*a[i+1],a[i+1]),mindp[i]*a[i+1])
mindp[i+1] = min(min(mindp[i]*a[i+1],a[i+1]),maxdp[i]*a[i+1])
dp[i+1] = max(dp[i], maxdp[i+1])
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [None for j in range(len(nums))]
        maxdp = [None for j in range(len(nums))]
        mindp = [None for j in range(len(nums))]

        dp[0] = nums[0]
        maxdp[0] = nums[0]
        mindp[0] = nums[0]

        for i in range(1,len(nums)):
            maxdp[i] = max(max(maxdp[i-1]*nums[i],nums[i]), mindp[i-1]*nums[i])
            mindp[i] = min(min(mindp[i-1]*nums[i],nums[i]), maxdp[i-1]*nums[i])
            dp[i] = max(dp[i-1],maxdp[i])

        return dp[-1]







def main():
    newclass = Solution()

    grid = [2,3,-2,4]

    print newclass.maxProduct(grid)








if __name__ =='__main__':
    main()