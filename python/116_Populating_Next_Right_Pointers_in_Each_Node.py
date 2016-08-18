#!/usr/bin/env python
# -*- coding: utf-8 -*-

"116. Populating Next Right Pointers in Each Node"
__author__ = 'Tom Gou'

"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

这道题要求在完全二叉树中加入next指针。
具体的生成规律：
1.root左的next是root的右。
2.root右的next是root的next的左。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None or root.left is None:
            return
        root.left.next = root.right
        if root.right is not None and root.next is not None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)




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



    print newclass.connect(treenode1)



if __name__ =='__main__':
    main()