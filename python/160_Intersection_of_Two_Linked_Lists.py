#!/usr/bin/env python
# -*- coding: utf-8 -*-

"160. Intersection of Two Linked Lists"
__author__ = 'Tom Gou'

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

这道题非常简单，使用双指针法，首先遍历list a和b，
得到其长度差。然后两个指针同时从heada，headb走，长的list提前多走一个
长度差，步数为1，就可以相遇在交汇点。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None:
            return None
        if headB is None:
            return None

        na = 0
        nb = 0
        pa = headA
        pb = headB

        while headA.next is not None:
            headA = headA.next
            na += 1

        while headB.next is not None:
            headB = headB.next
            nb += 1


        if na <= nb:
            for i in range(nb - na):
                pb = pb.next
        else:
            for i in range(na - nb):
                pa = pa.next

        while pa != pb:
            pa = pa.next
            pb = pb.next

        return pa




def main():
    newclass = Solution()

    listnode1 = ListNode(1)
    listnode2 = ListNode(2)
    listnode3 = ListNode(3)
    listnode4 = ListNode(4)
    listnode5 = ListNode(5)

    listnode1.next = listnode2
    listnode2.next = listnode3
    listnode3.next = listnode4
    listnode4.next = listnode5


    listnode11 = ListNode(11)
    listnode12 = ListNode(12)
    listnode13 = ListNode(13)

    listnode11.next = listnode12
    listnode12.next = listnode13
    listnode13.next = listnode3



    print newclass.getIntersectionNode(listnode1, listnode11).val


if __name__ =='__main__':
    main()