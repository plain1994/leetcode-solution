#!/usr/bin/env python
# -*- coding: utf-8 -*-

"99. Recover Binary Search Tree"
__author__ = 'Tom Gou'

"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?


这道题简单的解法是使用中序遍历，时间O(N)空间O(N)
中序遍历后bst可以得到递增序列，我们可以从中找到错误节点。

另外如果使用空间O(1)的话，我们需要使用Morris 中序遍历，这个之后再进行编写。


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.last = None
        self.wrongs = [None, None]
        self.recover_helper(root)
        self.wrongs[0].val, self.wrongs[1].val = self.wrongs[1].val, self.wrongs[0].val



    def recover_helper(self, root):
        if root is None:
            return

        self.recover_helper(root.left)

        if self.last is not None and self.last.val > root.val:
            if not self.wrongs[0]:
                self.wrongs[0] = self.last
            self.wrongs[1] = root
        self.last = root

        self.recover_helper(root.right)











def main():
    newclass = Solution()


    treenode2 = TreeNode(2)
    treenode3 = TreeNode(3)
    treenode4 = TreeNode(6)
    treenode5 = TreeNode(5)
    treenode6 = TreeNode(4)
    treenode7 = TreeNode(7)

    treenode5.left = treenode3
    treenode5.right = treenode6
    treenode3.left = treenode2
    treenode3.right = treenode4
    treenode6.left = None
    treenode6.right = treenode7



    print newclass.recoverTree(treenode5)
    print treenode5.right.val






if __name__ =='__main__':
    main()