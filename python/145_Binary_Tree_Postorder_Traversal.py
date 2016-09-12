#!/usr/bin/env python
# -*- coding: utf-8 -*-

"145. Binary Tree Postorder Traversal"
__author__ = 'Tom Gou'

"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorderTraversal_rec(root, res)
        return res

    def postorderTraversal_rec(self, root, res):
        if root is None:
            return
        self.postorderTraversal_rec(root.left, res)
        self.postorderTraversal_rec(root.right, res)
        res.append(root.val)


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



    print newclass.postorderTraversal(treenode1)



if __name__ =='__main__':
    main()