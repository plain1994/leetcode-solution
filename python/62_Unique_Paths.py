#!/usr/bin/env python
# -*- coding: utf-8 -*-

"62. Unique Paths"
__author__ = 'Tom Gou'

"""
A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point
in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

这是典型的dp问题，要到i，j这个点，机器人可以先到i－1，j
或i，j－1

得到dp方程：
dp[i][j] = dp[i-1][j] + dp[i][j-1]

程序中先把边界初始为1，然后递归计算其他。
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


def main():
    newclass = Solution()

    m = 20
    n = 10

    print newclass.uniquePaths(m, n)








if __name__ =='__main__':
    main()