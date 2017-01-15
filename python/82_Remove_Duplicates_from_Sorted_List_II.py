#!/usr/bin/env python
# -*- coding: utf-8 -*-

"82. Remove Duplicates from Sorted List II"
__author__ = 'Tom Gou'

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

这道题不是很难，不过要梳理好逻辑。
如果遇到相同元素，用while循环一直判断下一个元素，直到遇到不相同元素再停止循环
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

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        p = head
        while p is not None and p.next is not None:
            if p.val == p.next.val:
                value = p.val
                tmp = p.next.next
                while tmp is not None:
                    if tmp.val != value:
                        break
                    tmp = tmp.next

                prev.next = tmp
                p = tmp

            else:
                prev = p
                p = p.next


        #testing
        '''
        p = dummy
        while p is not None and p.next is not None:
            print p.val

            p = p.next
        print p.val
        '''

        return dummy.next


def main():
    newclass = Solution()

    listnode1 = ListNode(1)
    listnode2 = ListNode(2)
    listnode3 = ListNode(3)
    listnode4 = ListNode(3)
    listnode5 = ListNode(4)
    listnode6 = ListNode(4)
    listnode7 = ListNode(5)

    listnode1.next = listnode2
    listnode2.next = listnode3
    listnode3.next = listnode4
    listnode4.next = listnode5
    listnode5.next = listnode6
    listnode6.next = listnode7


    listnode11 = ListNode(11)
    listnode12 = ListNode(11)
    listnode13 = ListNode(11)
    listnode14 = ListNode(12)
    listnode15 = ListNode(13)

    listnode11.next = listnode12
    #listnode12.next = listnode13
    #listnode13.next = listnode14
    #listnode14.next = listnode15


    print newclass.deleteDuplicates(listnode11)


if __name__ =='__main__':
    main()