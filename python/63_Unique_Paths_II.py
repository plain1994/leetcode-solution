#!/usr/bin/env python
# -*- coding: utf-8 -*-

"63. Unique Paths II"
__author__ = 'Tom Gou'

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

这道题基于unique paths，增加了障碍物，
具体在程序中，设置障碍屋的个数为0。
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for j in range(n)]for i in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] +dp[i][j-1]

        return dp[m-1][n-1]





def main():
    newclass = Solution()

    grid = [[0,0,0],[0,1,0],[0,0,0]]

    print newclass.uniquePathsWithObstacles(grid)








if __name__ =='__main__':
    main()