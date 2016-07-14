#!/usr/bin/env python
# -*- coding: utf-8 -*-

"118. Pascal's Triangle"
__author__ = 'Tom Gou'

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

解法根据生成规律：
    A[i][j] = A[i-1][j-1] + A[i-1][j]
    第k层有k个元素
    每层第一个以及最后一个元素值为1
一行一行生成即可
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        A = []
        for i in range(numRows):
            current = [1]
            for j in range(1,i):  #range(start,stop,step)不包含stop，比如range(1,1)不存在
                current.append(A[i-1][j-1] + A[i-1][j])
            if i>= 1:
                current.append(1)
            A.append(current[:])

        return A

def main():
    newclass = Solution()
    print newclass.generate(5)
    print newclass.generate(7)




if __name__ =='__main__':
    main()