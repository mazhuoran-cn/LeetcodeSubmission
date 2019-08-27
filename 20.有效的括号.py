#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        buff = []
        for ss in s:
            if ss in '({[':
                buff.append(ss)
            elif ss == ')':
                if buff and buff[-1] == '(':
                    buff.pop()
                else:
                    return False
            elif ss == '}':
                if buff and buff[-1] == '{':
                    buff.pop()
                else: 
                    return False
            elif ss == ']':
                if buff and buff[-1] == '[':
                    buff.pop()
                else:
                    return False
        return True if not buff else False
