#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        buffer = [(None, -1)]
        res = []
        for i, ss in enumerate(s):
            if ss == '(':
                buffer.append((ss, i))
            elif ss == ')':
                if buffer and buffer[-1][0] == '(':
                    buffer.pop()
                else:
                    buffer.append((ss, i))
        buffer.append((None, len(s)))
        for i in range(1, len(buffer)):
            res.append(buffer[i][1]-buffer[i-1][1]-1)

        return sorted(res, reverse=True)[0]
