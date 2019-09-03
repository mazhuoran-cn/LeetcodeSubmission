#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def is_valued(combination, n):
            left = right = 0
            for s in combination:
                if s == '(':
                    left = left+1
                else:
                    right = right + 1
            return True if right <= left and left <= n and right <= n else False

        def backtrack(combination, n):
            if len(combination) == n*2:
                res.append(combination)
            else:
                if is_valued(combination+'(', n):
                    backtrack(combination+'(', n)
                if is_valued(combination+')', n):
                    backtrack(combination+')', n)

        backtrack("", n)
        return res
