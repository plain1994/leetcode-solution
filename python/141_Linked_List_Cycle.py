#!/usr/bin/env python
# -*- coding: utf-8 -*-

"141. Linked List Cycle"
__author__ = 'Tom Gou'

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

这道题比较简单，使用两个指针，fast指针每次走两步，
slow指针每次走一步，如果一段时间后两个指针重合，则存在环。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False




def main():
    newclass = Solution()

    listnode1 = ListNode(1)
    listnode2 = ListNode(2)
    listnode3 = ListNode(3)
    listnode4 = ListNode(4)


    listnode1.next = listnode2
    listnode2.next = listnode3
    listnode3.next = listnode4


    print newclass.hasCycle(listnode1)


if __name__ =='__main__':
    main()