#!/usr/bin/env python
# -*- coding: utf-8 -*-

"64. Minimum Path Sum"
__author__ = 'Tom Gou'

"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

这道题和Unique Paths差不多，
需要加入每个位置的数据

dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]



def main():
    newclass = Solution()

    grid = [[0,0,0],[0,1,0],[0,0,0]]

    print newclass.minPathSum(grid)








if __name__ =='__main__':
    main()