#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = ListNode(None)
        ref = res
        while lists:
            lists.sort(key = lambda x: x.val)
            ref.next = ListNode(lists[0].val)
            ref = ref.next
            if lists[0].next:
                lists[0] = lists[0].next
            else:
                lists.pop(0)
                
        return res.next
        