#!/usr/bin/env python
# -*- coding: utf-8 -*-

"102. Binary Tree Level Order Traversal"
__author__ = 'Tom Gou'

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

这道题要求二叉树的层次遍历，可以通过前序遍历加记录来实现。
每遍历一个节点，就把该节点放到对应的数组里。
数组个数可以提前计算二叉树深度来判断，也可以加入判断，
在数组个数不够时加入一个新数组。

解法1用到的前序遍历是递归实现的。

解法2使用一个队列来实现，先进先出。
从root开始，把当前节点放入队列，记录后出队，
然后把当前节点的左右子节点入队，持续这个过程直到先前队列被清空。

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
        return res

    def preOrder(self, root, level, res):
        if root:
            if len(res)<level+1:
                res.append([])
            res[level].append(root.val)
            self.preOrder(root.left, level+1, res)
            #print "0"
            #print level
            #print res
            self.preOrder(root.right, level+1, res)
            #print "1"
            #print level
            #print res

    def levelOrder2(self, root):
        res = []
        if root is None:
            return res
        queue = [root, ]
        while len(queue)>0:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop()
                level.append(node.val)
                if node.left is not None:
                    queue.insert(0, node.left)
                if node.right is not None:
                    queue.insert(0, node.right)
            res.append(level[:])
        return res




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



    print newclass.levelOrder2(treenode1)



if __name__ =='__main__':
    main()