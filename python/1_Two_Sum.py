#!/usr/bin/env python
# -*- coding: utf-8 -*-

"1. Two Sum"
__author__ = 'Tom Gou'

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.

本题如果使用暴力法的话时间复杂度为O(n2)，为了优化时间复杂度到O(n)，
我们使用hashmap来运算，牺牲一定的空间复杂度。
具体在Python中，使用字典dict，是一组键值对，如d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
查询值是否存在用value in d，查询值对应的键key = d.get(value)
"""

class Solution(object):
    """
    def twoSumBruce():
        nums = [2, 7, 11, 15]

        target = 26

        n = len(nums)
        flag = False
        for i in range(n):
            print "i:", i + 1
            for j in range(n - i - 1):
                print "j:", j + i + 2
                if (nums[i] + nums[j + i + 1] == target):
                    flag = True
                    break
            if flag == True: break

        return [i + 1, j + i + 2]
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]   nums = [3, 2, 4]
        :type target: int       target = 6
        :rtype: List[int]
        """
        d = {}
        n = len(nums)

        i = 0
        for number in nums:
            d[number] = i
            i = i+1

        for j in range(n):
            rest = target - nums[j]
            if rest in d :
                key = d.get(rest)
                if key != j:
                    break

        return [j, key]






def main():
    newclass = Solution()

    print  newclass.twoSum([2, 7, 11, 15], 9)

if __name__ =='__main__':
    main()