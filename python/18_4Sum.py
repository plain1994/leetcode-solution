#!/usr/bin/env python
# -*- coding: utf-8 -*-

"18. 4Sum"
__author__ = 'Tom Gou'

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
题目有两种解法，一种是与3Sum类似，多一层循环，时间复杂度O(n3)。
具体的是加入j这个数字，在i与l和r之间，循环过程与i类似。

另一种解法使用hashmap来减少时间复杂度到O(n2)
具体的，首先把两两数字和存在dict中，key为和，value为两个坐标，
转换4Sum为2Sum，相同和的在value中增加坐标对；
然后按照2Sum方法搜索，rest=target-nums[i]-nums[j]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.fourSum_1(nums,target)
    def fourSum_1(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        s = set()
        d = {}

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] not in d:
                    d[nums[i] + nums[j]] = [(i,j)]
                else:
                    d[nums[i] + nums[j]].append((i,j))

        for i in range(n):
            for j in range(i+1, n-1):
                rest = target - nums[i] - nums[j]
                if rest in d:
                    for k in d[rest]:
                        if k[0] > j:
                            s.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))

        return [list(i) for i in s]



    def fourSum_2(self, nums, target):
        # 与3Sum类似的解法，时间复杂度O(n3)
        nums.sort()
        n = len(nums)
        returnlist = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = n - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum < target:
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        returnlist.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return returnlist

def main():
    newclass = Solution()

    print  newclass.fourSum([1, 0, -1, 0, -2, 2], 0)

if __name__ =='__main__':
    main()