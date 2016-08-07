#!/usr/bin/env python
# -*- coding: utf-8 -*-

"102. Binary Tree Level Order Traversal"
__author__ = 'Tom Gou'

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

这道题判断二叉树是否对称。
方法1比较简单，用到递归，递归比较左右两个节点，
然后比较左节点的左孩子与右节点的右孩子，
再比较左节点的右孩子和右节点的左孩子。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetric_lr(root.left, root.right)
    def isSymmetric_lr(self, l, r):
        if not l and not r:
            return True
        if not l or not r or l.val != r.val:
            return False
        return self.isSymmetric_lr(l.left, r.right) and self.isSymmetric_lr(l.right, r.left)





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



    print newclass.isSymmetric1(treenode1)



if __name__ =='__main__':
    main()