#!/usr/bin/env python
# -*- coding: utf-8 -*-

"108. Convert Sorted Array to Binary Search Tree"
__author__ = 'Tom Gou'

"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

解法思路：
对于二叉树，左子树小于根节点，右子树大于根节点。
链表转换为平衡二叉树关键在于找到中间节点：
我们可以用fast，slow指针来解决，fast每次走两步，slow每次走一步，
fast走到结尾，那么slow就是中间节点了。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build(nums, 0, len(nums))

    def build(self, nums, start, end):
        if start >= end:
            return None
        mid = start + (end - start)/2

        node = TreeNode(nums[mid])
        node.left = self.build(nums, start, mid)
        node.right = self.build(nums, mid+1, end)
        return node



def main():
    newclass = Solution()

    nums = [1, 2, 4]
    print newclass.sortedArrayToBST(nums).val



if __name__ =='__main__':
    main()