#!/usr/bin/env python
# -*- coding: utf-8 -*-

"21. Merge Two Sorted Lists"
__author__ = 'Tom Gou'

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

解法较为简单，合并两个链接表。
注意l1 = l1.next
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        cu = re
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cu.next = l1
                l1 = l1.next
            else:
                cu.next = l2
                l2 = l2.next
            cu = cu.next

        if l1 != None:
            cu.next = l1
        if l2 != None:
            cu.next = l2

        return re.next

def main():
    newclass = Solution()
    listnode1 = ListNode(2)
    listnode2 = ListNode(4)
    listnode3 = ListNode(5)
    listnode4 = ListNode(3)
    listnode5 = ListNode(4)
    listnode6 = ListNode(6)
    listnode1.next = listnode2
    listnode2.next = listnode3

    listnode4.next = listnode5
    listnode5.next = listnode6


    re = newclass.mergeTwoLists(listnode1, listnode4)
    print re
    print re.val
    re = re.next
    print re.val
    re = re.next
    print re.val
    re = re.next
    print re.val
    re = re.next
    print re.val
    re = re.next
    print re.val



if __name__ =='__main__':
    main()