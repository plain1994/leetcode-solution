#!/usr/bin/env python
# -*- coding: utf-8 -*-

"257. Binary Tree Paths"
__author__ = 'Tom Gou'

"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

题目要求给出二叉树从根到叶的所有路径，
可以用dfs深度优先搜索，使用递归编写，
增加当前点，遍历先左再右，到叶节点时输出一条路径。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        if root is None:
            return result
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, tmp):
        tmp.append(str(node.val))

        if node.left is None and node.right is None:
            result.append('->'.join(tmp))
            tmp.pop()
            return
        if node.left:
            self.dfs(node.left, result, tmp)

        if node.right:
            self.dfs(node.right, result, tmp)

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

    treenode11 = TreeNode(1)
    treenode12 = TreeNode(2)
    treenode13 = TreeNode(3)

    treenode15 = TreeNode(5)


    treenode11.left = treenode12
    treenode11.right = treenode13
    treenode12.left = None
    treenode12.right = treenode15




    print newclass.binaryTreePaths(treenode11)







if __name__ =='__main__':
    main()