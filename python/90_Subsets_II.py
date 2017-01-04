#!/usr/bin/env python
# -*- coding: utf-8 -*-

"90. Subsets II"
__author__ = 'Tom Gou'

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

这道题与78 subsets类似，加入了一个判断，在遍历子节点时，
如果发现相等的，只遍历一个，后续跳过。用了continue

迭代方法比较难，暂时不看。
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsWithDup_1(nums)

    #recursion way
    def subsetsWithDup_1(self, nums):
        ret = []
        self.subsetsWithDup_rec(sorted(nums), [], ret)
        return ret

    def subsetsWithDup_rec(self, nums, res, ret):
        ret.append(res[:])

        for i, ele in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res.append(ele)
            self.subsetsWithDup_rec(nums[i+1:], res, ret)
            res.pop()

    #iteration way
    def subsetsWithDup_2(self, nums):
        ret = [[]]
        for i in sorted(nums):
            res = []
            for ele in ret:
                if len(ele) == 0 or ele[-1] != i:
                    res.append(ele[:])
                ele.append(i)
                res.append(ele[:])
            ret = res
        return ret



def main():
    newclass = Solution()

    nums = [1,2,2]

    print newclass.subsetsWithDup(nums)









if __name__ =='__main__':
    main()