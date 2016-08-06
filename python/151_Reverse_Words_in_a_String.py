#!/usr/bin/env python
# -*- coding: utf-8 -*-

"151. Reverse Words in a String"
__author__ = 'Tom Gou'

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

这道题较为简单，
解法1使用python的split和join方法，极为简洁；
解法2读入字符串，再一个一个的word生成新字符串。

"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.reverseWords1(s)

    def reverseWords1(self,s):
        return " ".join(s.split()[::-1])
        #join是split的逆方法
        # [::-1]是列表的分片方法，第一个:表示全部列表，第二个：-1代表步长，从右开始

    def reverseWords2(self,s):
        allwords = ''
        word = ''
        for char in s:
            if char != ' ':
                word += char
            else:
                if word != '':
                    allwords = " " + word + allwords
                word = ''

        if word != '':
            allwords = word + allwords
        else:
            allwords = allwords[1:]

        return allwords



def main():
    newclass = Solution()

    print  '"'+newclass.reverseWords("the sky is blue")+'"'
    print  '"'+newclass.reverseWords(" ")+'"'
    print  '"' + newclass.reverseWords("1 ") + '"'



if __name__ =='__main__':
    main()