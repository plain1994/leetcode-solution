#!/usr/bin/env python
# -*- coding: utf-8 -*-

"74. Search a 2D Matrix"
__author__ = 'Tom Gou'

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

这道题可以直接遍历解决，一行一列，时间O(M+N)空间O(1)
还可以加入二分查找，时间复杂度变为O(logMN)
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.searchMatrix2(matrix, target)

    def searchMatrix1(self, matrix, target):
        rows = len(matrix)
        colomns = len(matrix[0])
        row = 0
        i = 0
        while i < rows:
            if target <  matrix[i][0]:
                row = i
                break
            i += 1

        j = 0
        while j < colomns:
            if target == matrix[row-1][j]:
                return True
            j += 1

        return False

    def searchMatrix2(self, matrix, target):
        rows = len(matrix)
        colomns = len(matrix[0])
        row = 0
        l1 = 0
        r1 = rows - 1
        if rows == 2:
            if matrix[row][0] <= target:
                row = 0
            if matrix[row+1][0] <= target:
                row = 1
        while l1 + 1 < r1:
            m1 = (l1 + r1)/2
            if target == matrix[m1][0]:
                return True
            elif target > matrix[m1][0]:
                l1 = m1
            else:
                r1 = m1

        l2 = 0
        r2 = colomns - 1
        if colomns == 1:
            if matrix[row][0] == target:
                return True
            else:
                return False
        if colomns == 2:
            if matrix[row][0] == target:
                return True
            elif matrix[row][1] == target:
                return True
            else:
                return False
        while l2 + 1 < r2:
            m2 = (l2 + r2)/2
            if target == matrix[row][m2]:
                return True
            elif target > matrix[row][m2]:
                l2 = m2
            else:
                r2 = m2
        return False




def main():
    newclass = Solution()

    print  newclass.searchMatrix([[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    print  newclass.searchMatrix([[1]], 1)
    print  newclass.searchMatrix([[1, 1]], 2)
    print  newclass.searchMatrix([[1, 1]], 1)
    print  newclass.searchMatrix([[1], [3]], 3)






if __name__ =='__main__':
    main()