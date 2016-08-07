#!/usr/bin/env python
# -*- coding: utf-8 -*-

"105. Construct Binary Tree from Preorder and Inorder Traversal"
__author__ = 'Tom Gou'

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
if len(inorder) == 0:
            return None

        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        return root
这道题要求使用前序遍历和中序遍历，思路和106 constrcut binary tree from inorder and postorder traversal一样。
具体的：
1.通过前序遍历找到根节点
2.通过根节点将中序遍历分为两部分

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        return root




def main():
    newclass = Solution()
    treenode = newclass.buildTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])

    print treenode.val
    treenode = treenode.left
    print treenode.val
    treenode = treenode.right
    print treenode.val





if __name__ =='__main__':
    main()