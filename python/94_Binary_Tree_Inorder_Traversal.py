#!/usr/bin/env python
# -*- coding: utf-8 -*-

"94. Binary Tree Inorder Traversal"
__author__ = 'Tom Gou'

"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

这里先简单用递归做一下，中序遍历，左中右，append在中间。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderTraversal_rec(root, res)
        return res

    def inorderTraversal_rec(self, root, res):
        if root is None:
            return
        self.inorderTraversal_rec(root.left, res)
        res.append(root.val)
        self.inorderTraversal_rec(root.right, res)

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



    print newclass.inorderTraversal(treenode1)



if __name__ =='__main__':
    main()