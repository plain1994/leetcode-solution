#!/usr/bin/env python
# -*- coding: utf-8 -*-

"39. Combination Sum"
__author__ = 'Tom Gou'

"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]

类似dfs，先加入一个数字，递归调用，然后再pop出该数字
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.combinationSum_1(sorted(candidates), target, [], ret)
        return ret

    def combinationSum_1(self, candidates, target, res, ret):
        if target == 0:
            ret.append(res[:])
            return
        for i, num in enumerate(candidates):
            if target - num < 0:
                continue
            res.append(num)
            self.combinationSum_1(candidates[i:], target - num, res, ret)
            res.pop()






def main():
    newclass = Solution()

    candidates = [2, 3, 6, 7]
    target = 7

    print newclass.combinationSum(candidates, target)








if __name__ =='__main__':
    main()