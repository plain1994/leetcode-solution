#!/usr/bin/env python
# -*- coding: utf-8 -*-

"142. Linked List Cycle II"
__author__ = 'Tom Gou'

"""
Given a linked list, return the node where the cycle
 begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

这道题不难，但是没有理解为什么要在找到循环后，
把fast放到head上，然后和slow同时一步一步走，
直到相遇。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        slow = head.next
        fast = head.next.next

        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow






def main():
    newclass = Solution()

    listnode1 = ListNode(1)
    listnode2 = ListNode(2)
    listnode3 = ListNode(3)
    listnode4 = ListNode(4)


    listnode1.next = listnode2
    listnode2.next = listnode3
    listnode3.next = listnode4
    listnode4.next = listnode1


    print newclass.detectCycle(listnode1).val


if __name__ =='__main__':
    main()