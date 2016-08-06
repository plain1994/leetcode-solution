#!/usr/bin/env python
# -*- coding: utf-8 -*-

"119. Pascal's Triangle II"
__author__ = 'Tom Gou'

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

可以直接在Pascal's Triangle 1代基础上修改，使用past记录之前一行的数组；
为了优化空间复杂度，可以在同一个数组中操作，此时应注意新数组的生成需要从后
往前，否则会影响数字大小。

"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        """
        #解法一，空间复杂度较高，直接在Pascal's Triangle 1代基础上修改
        past = []
        for i in range(rowIndex+1):
            current = [1]
            for j in range(1,i):
                current.append(past[j-1] + past[j])
            if i >= 1:
                current.append(1)
            past = current
        return current
        """
        #解法二，O(k)的空间复杂度，速度会变慢，数组从后往前生成
        A = [1]
        for i in range(rowIndex+1):
            for j in range(1,i):
                current = A[i-j-1] + A[i-j]
                A[i-j] = current
            if i >=1:
                A.append(1)

        return A


def main():
    newclass = Solution()
    print newclass.getRow(0)
    print newclass.getRow(1)
    print newclass.getRow(2)
    print newclass.getRow(3)
    print newclass.getRow(4)




if __name__ =='__main__':
    main()