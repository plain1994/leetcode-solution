#!/usr/bin/env python
# -*- coding: utf-8 -*-

"95. Unique Binary Search Trees II"
__author__ = 'Tom Gou'

"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


这道题乍一看无从下手， 但从bst的性质我们可以知道：
对于以i为根节点的bst，其左子树在[0, i-1]区间，其右子树在[i+1, n]区间；
若左子树有m种排列方式，右子树有n种排列方式，则该bst的总排列方式为m*n

所以我们只需要得到i的左子树和右子树的所有排列，就能得到i的所有排列，使用递归搞掂。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateTrees_1(1, n)

    def generateTrees_1(self, start, stop):
        if start > stop:
            return [None]

        re = []
        for i in range(start, stop+1):
            l = self.generateTrees_1(start, i-1)
            r = self.generateTrees_1(i+1, stop)
            for j in range(0, len(l)):
                for k in range(0, len(r)):
                    node = TreeNode(i)
                    node.left = l[j]
                    node.right = r[k]
                    re.append(node)

        return re











def main():
    newclass = Solution()

    n = 3

    print newclass.generateTrees(n)








if __name__ =='__main__':
    main()