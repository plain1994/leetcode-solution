#!/usr/bin/env python
# -*- coding: utf-8 -*-

"109. Convert Sorted List to Binary Search Tree"
__author__ = 'Tom Gou'

"""
Given a singly linked list where elements are sorted in
ascending order, convert it to a height balanced BST.

解法思路：
对于二叉树，左子树小于根节点，右子树大于根节点。
链表转换为平衡二叉树关键在于找到中间节点：
我们可以用fast，slow指针来解决，fast每次走两步，slow每次走一步，
fast走到结尾，那么slow就是中间节点了。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.build(head, None)
    def build(self, start, end):
        if start == end:
            return None
        fast = start
        slow = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        node.left = self.build(start, slow)
        node.right = self.build(slow.next, end)

        return node


def main():
    newclass = Solution()

    listnode1 = ListNode(1)
    listnode2 = ListNode(2)
    listnode3 = ListNode(3)
    listnode4 = ListNode(4)
    listnode5 = ListNode(5)
    listnode6 = ListNode(6)
    listnode7 = ListNode(7)

    listnode1.next = listnode2
    listnode2.next = listnode3
    listnode3.next = listnode4
    listnode4.next = listnode5
    listnode5.next = listnode6
    listnode6.next = listnode7



    print newclass.sortedListToBST(listnode1).val



if __name__ =='__main__':
    main()