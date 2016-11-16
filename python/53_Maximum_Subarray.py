#!/usr/bin/env python
# -*- coding: utf-8 -*-

"53. Maximum Subarray"
__author__ = 'Tom Gou'

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


这道题是经典的dp问题，不难得出dp方程：
dp[i+1] = max(dp[i], dp[i]+a[i+1])

另外还有二分法，以后再探究。

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        cursum = 0
        for num in nums:
            cursum += num
            maxsum = max(maxsum, cursum)
            if cursum < 0:
                cursum = 0
        return maxsum




def main():
    newclass = Solution()

    grid = [-2,1,-3,4,-1,2,1,-5,4]

    print newclass.maxSubArray(grid)








if __name__ =='__main__':
    main()