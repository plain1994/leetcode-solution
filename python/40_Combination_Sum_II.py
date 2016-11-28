#!/usr/bin/env python
# -*- coding: utf-8 -*-

"40. Combination Sum II"
__author__ = 'Tom Gou'

"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

这道题与39combination Sum 类似，
使用dfs，值得记忆。
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if target - num < 0 or (i > 0 and candidates[i] == candidates[i-1]):
                continue
            res.append(num)
            self.combinationSum_1(candidates[i+1:], target - num, res, ret)
            res.pop()









def main():
    newclass = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    print newclass.combinationSum2(candidates, target)

    candidates1 = [1]
    target1 = 1

    print newclass.combinationSum2(candidates1, target1)








if __name__ =='__main__':
    main()