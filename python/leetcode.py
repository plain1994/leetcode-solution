#!/usr/bin/env python
# -*- coding: utf-8 -*-

'data clean for louvain_java'
__author__ = 'Tom Gou'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def py2addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        heado = head
        add = 0
        while True:
            listnode = ListNode((l1.val+l2.val+add)%10)
            add = (l1.val+l2.val+add)/10
            print "l1:", l1.val
            print "l2:", l2.val
            print "l:", listnode.val
            head.next = listnode
            head = listnode
            if (l1.next == None) and (l2.next == None) and (add==0):
                break
            if(l1.next == None):
                l1 = ListNode(0)
            else:
                l1 = l1.next
            if (l2.next == None):
                l2 = ListNode(0)
            else:
                l2 = l2.next

        return heado.next




    def py1bruce():
        nums = [2, 7, 11, 15]

        target = 26

        n = len(nums)
        flag = False
        for i in range(n):
            print "i:", i + 1
            for j in range(n - i - 1):
                print "j:", j + i + 2
                if (nums[i] + nums[j + i + 1] == target):
                    flag = True
                    break
            if flag == True: break

        return [i + 1, j + i + 2]

    def py1dicttwoSum(self, nums, target):
        """
        :type nums: List[int]   nums = [3, 2, 4]
        :type target: int       target = 6
        :rtype: List[int]
        """
        d = {}
        n = len(nums)

        i = 0
        for number in nums:
            d[number] = i
            i = i+1

        for j in range(n):
            rest = target - nums[j]
            if rest in d :
                key = d.get(rest)
                if key != j:
                    break

        return [j, key]






def main():
    newclass = Solution()
    listnode1 = ListNode(2)
    listnode2 = ListNode(4)
    listnode3 = ListNode(3)
    listnode4 = ListNode(5)
    listnode5 = ListNode(6)
    listnode6 = ListNode(4)
    listnode1.next = listnode2
    listnode2.next = listnode3


    listnode4.next = listnode5
    listnode5.next = listnode6

    a1 =  newclass.py2addTwoNumbers(listnode1, listnode4)

    print a1.val
    a1 = a1.next
    print a1.val
    a1 = a1.next
    print a1.val
    a1 = a1.next

if __name__ =='__main__':
    main()