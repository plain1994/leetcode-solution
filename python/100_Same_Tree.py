#!/usr/bin/env python
# -*- coding: utf-8 -*-

"100. Same Tree"
__author__ = 'Tom Gou'

"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)





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

    treenode11 = TreeNode(1)
    treenode12 = TreeNode(2)
    treenode13 = TreeNode(3)
    treenode14 = TreeNode(4)
    treenode15 = TreeNode(5)
    treenode16 = TreeNode(6)
    treenode17 = TreeNode(7)

    treenode11.left = treenode12
    treenode11.right = treenode13
    treenode12.left = treenode14
    treenode12.right = treenode15
    treenode13.left = treenode16
    treenode13.right = treenode17



    print newclass.isSameTree(treenode1, treenode11)



if __name__ =='__main__':
    main()