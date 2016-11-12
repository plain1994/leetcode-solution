#!/usr/bin/env python
# -*- coding: utf-8 -*-

"114. Flatten Binary Tree to Linked List"
__author__ = 'Tom Gou'

"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

这道题本质上是一个二叉树前序遍历，
前序上左右，中序左上右，后序左右上，名称与上节点位置相关。

将结果连成一个链表。

使用栈简单实现，先进后出，先进右再进左。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        ns = []
        dummy = TreeNode(0)

        ns.append(root)

        while len(ns)!= 0:
            p = ns.pop()

            dummy.right = p
            dummy = p

            if p.right is not None:
                ns.append(p.right)
                p.right = None #将之前点的右子树变为空，避免影响最终结果

            if p.left is not None:
                ns.append(p.left)
                p.left = None











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
    treenode11.left = treenode12
    treenode11.right = None


    newclass.flatten(treenode11)

    print treenode11.val
    print treenode11.right.val
    print treenode11.right.right
    #print treenode1.right.right.right.val
    #print treenode1.right.right.right.right.val
    #print treenode1.right.right.right.right.right.val





if __name__ =='__main__':
    main()