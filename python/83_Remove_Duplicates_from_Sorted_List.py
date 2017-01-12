#!/usr/bin/env python
# -*- coding: utf-8 -*-

"83. Remove Duplicates from Sorted List"
__author__ = 'Tom Gou'

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

这道题很简单，遍历判断就行
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        p = head
        while p is not None and p.next is not None:
            if p.val == p.next.val:
                tmp = p.next.next
                p.next = tmp
            else:
                p = p.next

        ''' testing
        p = head
        while p is not None and p.next is not None:
            print p.val

            p = p.next
        print p.val
        '''

        return head




def main():
    newclass = Solution()

    listnode1 = ListNode(1)
    listnode2 = ListNode(1)
    listnode3 = ListNode(2)
    listnode4 = ListNode(3)
    listnode5 = ListNode(3)

    listnode1.next = listnode2
    listnode2.next = listnode3
    listnode3.next = listnode4
    listnode4.next = listnode5


    listnode11 = ListNode(11)
    listnode12 = ListNode(11)
    listnode13 = ListNode(11)
    listnode14 = ListNode(11)

    listnode11.next = listnode12
    listnode12.next = listnode13
    listnode13.next = listnode14



    print newclass.deleteDuplicates(listnode1)


if __name__ =='__main__':
    main()