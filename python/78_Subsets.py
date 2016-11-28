#!/usr/bin/env python
# -*- coding: utf-8 -*-

"78. Subsets"
__author__ = 'Tom Gou'

"""
Given a set of distinct integers, nums,
return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

和39 combination sum类似
iteration way is hard to understand
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsets_2(nums)

    #recursion way
    def subsets_1(self, nums):
        ret = []
        self.subsets_helper(sorted(nums), [], ret)
        return ret
    def subsets_helper(self, nums, res, ret):
        ret.append(res[:])

        for i, ele in enumerate(nums):
            res.append(ele)
            self.subsets_helper(nums[i+1:], res, ret)
            res.pop()

    #iteration way, hard to understand
    def subsets_2(self, nums):
        ret = [[]]
        for i in sorted(nums):
            print "i",i
            res = []
            for ele in ret:
                print ele
                res.append(ele[:])
                ele.append(i)
                res.append(ele[:])
            print "ret",ret
            ret = res[:]
        return ret




def main():
    newclass = Solution()

    nums = [1,2,3]

    print newclass.subsets(nums)









if __name__ =='__main__':
    main()