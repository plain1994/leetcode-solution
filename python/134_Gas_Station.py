#!/usr/bin/env python
# -*- coding: utf-8 -*-

"134. Gas Station"
__author__ = 'Tom Gou'

"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.


如果total小于0的话肯定不能走完，返回－1

假设我们现在走到第i个加油站，此时油量为sum，如果sum＋gas[i]-cost[i] < 0
则无法继续前进，起点肯定在i＋1及其后面，因为i及之前的点都试过了。
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum = 0
        total = 0
        k = 0
        for i in range(0, len(gas)):
            sum += gas[i] - cost[i]

            if sum < 0:
                k = i + 1
                sum = 0

            total += gas[i] - cost[i]

        if total < 0:
            return -1
        else:
            return k



def main():
    newclass = Solution()

    nums1 = [4]
    nums2 = [5]


    print newclass.canCompleteCircuit(nums1, nums2)


if __name__ =='__main__':
    main()