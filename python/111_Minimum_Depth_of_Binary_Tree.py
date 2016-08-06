#!/usr/bin/env python
# -*- coding: utf-8 -*-

"111. Minimum Depth of Binary Tree"
__author__ = 'Tom Gou'

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
这道题与104 maximum depth of binary tree类似，通过递归遍历来做。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        if root.left != None and root.right == None:
            return self.minDepth(root.left) + 1

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return min(left_depth, right_depth) + 1




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



    print newclass.minDepth(treenode0)





if __name__ =='__main__':
    main()