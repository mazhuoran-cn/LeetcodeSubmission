#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        group = list()
        while 1:
            group.append(s[:numRows])
            group.append(s[numRows:numRows*2-2])
        

