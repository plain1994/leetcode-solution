#!/usr/bin/env python
# -*- coding: utf-8 -*-

"98. Validate Binary Search Tree"
__author__ = 'Tom Gou'

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

这道题要求判断二叉树是否是二叉查找树，
即满足左小于中，小于右。
做法比较简单，使用递归进行。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, -sys.maxint, sys.maxint)
    def valid(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)











def main():
    newclass = Solution()

    treenode1 = TreeNode(1)
    treenode2 = TreeNode(2)
    treenode3 = TreeNode(3)
    treenode4 = TreeNode(4)
    treenode5 = TreeNode(5)
    treenode6 = TreeNode(6)
    treenode7 = TreeNode(7)

    treenode1.left = treenode2
    treenode1.right = treenode3
    treenode2.left = treenode4
    treenode2.right = treenode5
    treenode3.left = treenode6
    treenode3.right = treenode7



    print newclass.isValidBST(treenode1)






if __name__ =='__main__':
    main()