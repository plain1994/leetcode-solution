#!/usr/bin/env python
# -*- coding: utf-8 -*-

"23. Merge k Sorted Lists"
__author__ = 'Tom Gou'

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Hide Company Tags

这道题不是很难，不过编写的时候比较麻烦。

首先写好一个合并两个list的模块merge2List，
然后递归调用，把lists的前一半和后一半合并，放在前一半的位置，
接着在对前一半进行递归操作。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0:
            return None

        while n > 1:
            k = (n + 1) / 2
            for i in range(0, n/2, 1):
                lists[i] = self.merge2List(lists[i], lists[i + k])
            n = k

        return lists[0]

    def merge2List(self, l1, l2):
        dummy = ListNode(0)
        p = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1 is not None:
            p.next = l1
        elif l2 is not None:
            p.next = l2

        return dummy.next

def main():
    newclass = Solution()
    lists = []
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

    lists.append(listnode1)
    lists.append(listnode4)


    print newclass.mergeKLists(lists).val




if __name__ =='__main__':
    main()