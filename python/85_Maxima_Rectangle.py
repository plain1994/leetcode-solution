#!/usr/bin/env python
# -*- coding: utf-8 -*-

"85. Maximal Rectangle"
__author__ = 'Tom Gou'

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

这道题的难度也比较大，很难想到思路。
在84. Largest Rectangle in Histogram中，我们使用栈来解决最大矩形的问题，这里把问题转化为84题。

对于矩阵中的每一行，都生成一个最大矩形问题，最后总的时间复杂度是O(n2)
具体的，每一行生成一个数组，数组的每个值是其对应位置向上延伸后1的个数，遇到0停止。

"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        h = [0 for i in range(col+1)]
        max_area = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    h[j] = 0
                else:
                    h[j] += 1
            print h
            max_area = max(max_area, self.largestRectangleArea(h))

        return max_area

    def largestRectangleArea(self, h):
        stack = []
        max_area = 0
        i = 0
        while i < len(h):
            if len(stack) == 0 or h[i] >= h[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                height = h[stack.pop()]
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, width * height)
        return max_area


def main():
    newclass = Solution()

    print  newclass.maximalRectangle(["10100","10111","11111","10010"])



if __name__ =='__main__':
    main()