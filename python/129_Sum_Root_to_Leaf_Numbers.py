#!/usr/bin/env python
# -*- coding: utf-8 -*-

"129. Sum Root to Leaf Numbers"
__author__ = 'Tom Gou'

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.


题目与257 paths类似，
通过dfs找到path后再记录
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        numlist = []
        if root is None:
            return 0
        self.dfs(root, numlist, [])
        sum = 0
        for num in numlist:
            sum += num
        return sum

    def dfs(self, root, numlist, tmp):
        tmp.append(root.val)

        if root.left is None and root.right is None:
            tmpsum = 0
            for num in tmp:
                tmpsum = tmpsum*10 + num
            numlist.append(tmpsum)
            tmp.pop()
            return

        if root.left:
            self.dfs(root.left, numlist, tmp)
        if root.right:
            self.dfs(root.right, numlist, tmp)

        tmp.pop()





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





    print newclass.sumNumbers(treenode1)







if __name__ =='__main__':
    main()