#!/usr/bin/env python
# -*- coding: utf-8 -*-

"107. Binary Tree Level Order Traversal II"
__author__ = 'Tom Gou'

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

较为简单的想法是对层次遍历的结果进行翻转。如102 binary tree level order traversal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preOrder(root, 0, res)
        res.reverse()#res[::-1]
        return res

    def preOrder(self, root, level, res):
        if root:
            if len(res)<level+1:
                res.append([])
            res[level].append(root.val)
            self.preOrder(root.left, level+1, res)
            self.preOrder(root.right, level+1, res)




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



    print newclass.levelOrder1(treenode1)



if __name__ =='__main__':
    main()