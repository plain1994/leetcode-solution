#!/usr/bin/env python
# -*- coding: utf-8 -*-

"77. Combinations"
__author__ = 'Tom Gou'

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

这道题用递归来求解，类似dfs，较为难想
python容易超时，需要精简算法

"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #leetcode的python又超时了。。。
        return self.combine_1([], 1, [], n, k)

    def combine_1(self, ret, start, sofar, n, k):
        for i in range(start, n-k+2):
            if k == 1:
                ret.append(sofar + [i])
            else:
                self.combine_1(ret, i+1,sofar+[i], n, k-1)

        return ret








def main():
    newclass = Solution()

    n = 4
    k = 2

    print newclass.combine(n, k)








if __name__ =='__main__':
    main()