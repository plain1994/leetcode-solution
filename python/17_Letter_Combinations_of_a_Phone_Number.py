#!/usr/bin/env python
# -*- coding: utf-8 -*-

"17. Letter Combinations of a Phone Number"
__author__ = 'Tom Gou'

"""
Given a digit string, return all possible letter combinations that
the number could represent.

A mapping of digit to letters (just like on the telephone buttons)
is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer
could be in any order you want.

这道题不难，时间复杂度on3，用字典存字母。
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        self.digit_map = {'2':'abc',
                          '3':'def',
                          '4':'ghi',
                          '5':'jkl',
                          '6':'mno',
                          '7':'pqrs',
                          '8':'tuv',
                          '9':'wxyz'
                          }
        return self.letterCombinations_1(digits)

    def letterCombinations_1(self, digits):
        ret = ['']
        for digit in digits:
            res = []
            for comb in ret:
                for char in self.digit_map[digit]:
                    res.append(comb + char)
            ret = res
        return ret


    #recursion way to do this
    def letterCombinations_2(self, digits):
        ret = []
        self.letterCombinations_rec(0, digits, '', ret)
        return ret
    def letterCombinations_rec(self, i, digits, res, ret):
        if i == len(digits):
            ret.append(res[:])
            return
        for char in self.digit_map[digits[i]]:
            self.letterCombinations_rec(i+1, digits, res+char, ret)







def main():
    newclass = Solution()

    digits = "23"

    print newclass.letterCombinations(digits)









if __name__ =='__main__':
    main()