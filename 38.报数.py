#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
class Solution:
    def countAndSay(self, n: int) -> str:
        def count(s, n):
            if n-1:
                counter = 0
                tmp = s[0]
                res = ''
                for ss in s:
                    if ss != tmp:
                        res = res + str(counter) + tmp
                        tmp = ss
                        counter = 0
                    if ss == tmp:
                        counter = counter + 1
                res = res + str(counter) + tmp

                return count(res, n-1)
            else:
                return s
        
        return count('1', n)


