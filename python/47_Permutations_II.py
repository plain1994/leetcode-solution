#!/usr/bin/env python
# -*- coding: utf-8 -*-

"47. Permutations II"
__author__ = 'Tom Gou'

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

与46 Permutations类似， 加入了判断是否元素重复
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permuteUnique_1(nums)

    def permuteUnique_1(self, nums):
        ret = []
        self.permuteUnique_helper(sorted(nums), [], ret)
        return ret

    def permuteUnique_helper(self, nums, res, ret):
        if len(nums) == 0:
            ret.append(res[:])
            return

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res.append(n)
            self.permuteUnique_helper(nums[:i]+nums[i+1:], res, ret)
            res.pop()


def main():
    newclass = Solution()

    nums = [1,1,2]

    print newclass.permuteUnique(nums)


if __name__ =='__main__':
    main()