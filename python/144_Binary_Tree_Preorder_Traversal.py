#!/usr/bin/env python
# -*- coding: utf-8 -*-

"144. Binary Tree Preorder Traversal"
__author__ = 'Tom Gou'

"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
这里简单地用递归来处理，前序遍历为中左右。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorderTrazversal_rec(root, res)
        return res

    def preorderTraversal_rec(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.preorderTraversal_rec(root.left, res)
        self.preorderTraversal_rec(root.right, res)








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



    print newclass.preorderTraversal(treenode1)



if __name__ =='__main__':
    main()