#!/usr/bin/env python
# -*- coding: utf-8 -*-

"120. Triangle"
__author__ = 'Tom Gou'

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


我们可以容易得到dp方程：

#自顶向下的顺序
dp[m+1][n] = min(dp[m][n], dp[m][n-1]) + triangle[m+1][n]    if n > 0
dp[m+1][0] = dp[m][0] + triangle[m+1][0]


#自底向上的顺序更为简单
dp[m][n] = min(dp[m+1][n], dp[m+1][n+1]) + triangle[m][n]


"""
import sys

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.minimumTotal_2(triangle)

    #自顶向下的顺序
    def minimumTotal_1(self, triangle):
        n = len(triangle)

        if n == 0:
            return 0

        total = [sys.maxint for a in range(n)]
        total[0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i, -1, -1):
                if j == 0:
                    total[j] = total[j] + triangle[i][j]
                else:
                    total[j] = min(total[j-1], total[j]) + triangle[i][j]

        mintotal = total[0]
        for i in range(n):
            mintotal = min(mintotal, total[i])

        return mintotal

    #自底向上的顺序更为简单
    def minimumTotal_2(self, triangle):
        n = len(triangle)

        if n == 0:
            return 0

        dp = triangle[n-1]

        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]












def main():
    newclass = Solution()

    triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]

    print newclass.minimumTotal(triangle)








if __name__ =='__main__':
    main()