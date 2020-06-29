#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = list()
        l2_num = list()
        while l1:
            l1_num.append(str(l1.val))
            l1 = l1.next
        while l2:
            l2_num.append(str(l2.val))
            l2 = l2.next
        l1_num = int(''.join(l1_num)[::-1])
        l2_num = int(''.join(l2_num)[::-1])
        res_num = str(l1_num + l2_num)[::-1]
        res = ListNode(int(res_num[0]))
        tmp = res
        for num in res_num[1:]:
            tmp.next = ListNode(int(num))
            tmp = tmp.next
        return res
        




