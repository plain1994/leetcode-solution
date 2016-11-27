#!/usr/bin/env python
# -*- coding: utf-8 -*-

"96. Unique Binary Search Trees"
__author__ = 'Tom Gou'

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


这道题乍一看无从下手， 但从bst的性质我们可以知道：
对于以i为根节点的bst，其左子树在[0, i-1]区间，其右子树在[i+1, n]区间；
若左子树有m种排列方式，右子树有n种排列方式，则该bst的总排列方式为m*n

dp方程为：

dp[i] = sum(dp[j]*dp[i-j-1])

"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j]*dp[i-j-1]

        return dp[n]








def main():
    newclass = Solution()

    n = 3

    print newclass.numTrees(n)








if __name__ =='__main__':
    main()