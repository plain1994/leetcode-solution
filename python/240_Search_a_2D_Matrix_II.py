#!/usr/bin/env python
# -*- coding: utf-8 -*-

"240. Search a 2D Matrix II"
__author__ = 'Tom Gou'

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false

这道题主要按照矩阵的顺序来进行搜索。
从左下角开始遍历，大于当前的话向右走，小于当前的话向上走。
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.searchMatrix1(matrix, target)

    def searchMatrix1(self, matrix, target):
        rows = len(matrix)
        colomns = len(matrix[0])
        i = rows - 1
        j = 0
        while i >= 0 and j < colomns:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j += 1
            else:
                i -= 1

        return False


def main():
    newclass = Solution()

    print  newclass.searchMatrix([[1, 4], [2, 5]], 4)
    print  newclass.searchMatrix([[-5]], -2)
    print  newclass.searchMatrix([[-1], [-1]], 0)






if __name__ =='__main__':
    main()