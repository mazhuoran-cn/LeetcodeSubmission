/*
 * @lc app=leetcode.cn id=2 lang=java
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode tmp = res;
        int flag = 0;
        while(l1!=null || l2!=null){
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int sum = x + y + flag;
            flag = sum / 10;
            tmp.next = new ListNode(sum%10);
            if (l1!=null) l1 = l1.next;
            if (l2!=null) l2 = l2.next;
            tmp = tmp.next;
        }
        if(flag==1){
            tmp.next = new ListNode(flag);
        }
        return res.next;
    }
}
// @lc code=end

