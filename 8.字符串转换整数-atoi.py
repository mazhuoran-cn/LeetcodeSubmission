#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        nums = '0123456789'

        def first_str(str, start_flag=False, num=0, symbol=1):
            if not str:
                return num*symbol
            # 遇到非' +-0123456798'字符
            elif not start_flag and str[0] not in nums+' -+':
                return symbol*num if start_flag else 0
            # 遇到开始部分为' '
            elif not start_flag and str[0] == ' ':
                return first_str(str[1:], False)
            # 遇到'+'
            elif not start_flag and str[0] == '+':
                return first_str(str[1:], True)
            # 遇到'-'
            elif not start_flag and str[0] == '-':
                return first_str(str[1:], True, symbol=-1)
            # 开始处理数字后遇到非数字字符
            elif start_flag and str[0] not in nums:
                return num*symbol
            elif str[0] in nums:
                num = 10*num + nums.index(str[0])
                if num*symbol < INT_MIN:
                    return INT_MIN
                elif num*symbol > INT_MAX:
                    return INT_MAX
                else:
                    return first_str(str[1:], True, num, symbol)

        return first_str(str)



