#!/usr/bin/env python
# -*- coding: utf-8 -*-

"104. Maximum Depth of Binary Tree"
__author__ = 'Tom Gou'

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

这道题比较简单，用一个递归来遍历二叉树，到达叶子节点时，记录深度返回。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1




def main():
    newclass = Solution()

    treenode0 = TreeNode(0)
    treenode1 = TreeNode(1)
    treenode2 = TreeNode(2)
    treenode3 = TreeNode(3)
    treenode4 = TreeNode(4)

    treenode0.left = treenode1
    treenode0.right = treenode2
    treenode1.left = treenode3
    treenode1.right = treenode4



    print newclass.maxDepth(treenode0)





if __name__ =='__main__':
    main()