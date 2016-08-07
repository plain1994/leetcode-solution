#!/usr/bin/env python
# -*- coding: utf-8 -*-

"106. Construct Binary Tree from Inorder and Postorder Traversal"
__author__ = 'Tom Gou'

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

这道题要求根据中序遍历和后序遍历来生成二叉树。
                1
        --------|-------
        2               3
    ----|----       ----|----
    4       5       6       7

前序遍历 1245367
中序遍历 4251637
后续遍历 4526731

具体的方法是：
1.首先找到后序遍历的最后一个，这个数是树的根
2.然后在中序遍历中找到根的位置，根左为左子树，根右为右子树。
3.进行递归。

递归的方法和细节比较巧妙，值得记忆。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)

        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root





def main():
    newclass = Solution()


    treenode = newclass.buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1])

    print treenode.val
    treenode = treenode.left
    print treenode.val
    treenode = treenode.right
    print treenode.val





if __name__ =='__main__':
    main()