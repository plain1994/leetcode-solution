#!/usr/bin/env python
# -*- coding: utf-8 -*-

"46. Permutations"
__author__ = 'Tom Gou'

"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

比较难理解，dfs递归求解
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute_1(nums)

    def permute_1(self, nums):
        ret = []
        self.permute_helper(nums, [], ret)
        return ret

    def permute_helper(self, nums, res, ret):
        if len(nums) == 0:
            ret.append(res[:])
            return

        for i, n in enumerate(nums):
            res.append(n)
            #print "i", i
            #print "res",res
            #print "nums",nums
            #print "nums1",nums[:i]
            #print "nums2", nums[i+1:]
            self.permute_helper(nums[:i] + nums[i+1:], res, ret)
            res.pop()


def main():
    newclass = Solution()

    nums = [1,2,3]

    print newclass.permute(nums)


if __name__ =='__main__':
    main()